import wx
import random

class Character:
    def __init__(self, health, attack_power):
        self.health = health
        self.attack_power = attack_power

class Game(wx.App):
    def OnInit(self):
        self.frame = wx.Frame(None, title="Simple RPG Game")
        self.panel = wx.Panel(self.frame)

        self.story_text = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.attack_button = wx.Button(self.panel, label="Attack")
        self.defend_button = wx.Button(self.panel, label="Defend")

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.story_text, 1, wx.EXPAND)
        self.sizer.Add(self.attack_button, 0, wx.EXPAND)
        self.sizer.Add(self.defend_button, 0, wx.EXPAND)

        self.panel.SetSizerAndFit(self.sizer)
        self.frame.Show()

        self.attack_button.Bind(wx.EVT_BUTTON, self.attack)
        self.defend_button.Bind(wx.EVT_BUTTON, self.defend)

        self.player = Character(100, 10)
        self.enemy = Character(100, 10)
        self.defending = False

        self.story_text.AppendText("A wild enemy appeared!\n")

        return True

    def attack(self, event):
        damage = self.player.attack_power
        self.enemy.health -= damage
        self.story_text.AppendText(f"You attacked the enemy for {damage} damage.\n")
        self.check_win()
        self.enemy_turn()

    def defend(self, event):
        self.defending = True
        self.story_text.AppendText("You prepare to defend against the next attack.\n")
        self.enemy_turn()

    def enemy_turn(self):
        damage = self.enemy.attack_power
        if self.defending:
            damage //= 2
            self.defending = False
        self.player.health -= damage
        self.story_text.AppendText(f"The enemy attacked you for {damage} damage.\n")
        self.check_win()

    def check_win(self):
        if self.player.health <= 0:
            self.story_text.AppendText("You have been defeated...\n")
            self.attack_button.Disable()
            self.defend_button.Disable()
        elif self.enemy.health <= 0:
            self.story_text.AppendText("You have defeated the enemy!\n")
            self.attack_button.Disable()
            self.defend_button.Disable()

if __name__ == "__main__":
    app = Game()
    app.MainLoop()