import tkinter as tk
import random

class Character:
    def __init__(self, health, attack_power):
        self.health = health
        self.attack_power = attack_power

class Game:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Simple RPG Game")

        self.story_text = tk.Text(self.root, width=50, height=10)
        self.story_text.pack()

        self.attack_button = tk.Button(self.root, text="Attack", command=self.attack)
        self.attack_button.pack()

        self.defend_button = tk.Button(self.root, text="Defend", command=self.defend)
        self.defend_button.pack()

        self.player = Character(100, 10)
        self.enemy = Character(100, 10)
        self.defending = False

        self.story_text.insert(tk.END, "A wild enemy appeared!\n")

    def attack(self):
        damage = self.player.attack_power
        self.enemy.health -= damage
        self.story_text.insert(tk.END, f"You attacked the enemy for {damage} damage.\n")
        self.check_win()
        self.enemy_turn()

    def defend(self):
        self.defending = True
        self.story_text.insert(tk.END, "You prepare to defend against the next attack.\n")
        self.enemy_turn()

    def enemy_turn(self):
        damage = self.enemy.attack_power
        if self.defending:
            damage //= 2
            self.defending = False
        self.player.health -= damage
        self.story_text.insert(tk.END, f"The enemy attacked you for {damage} damage.\n")
        self.check_win()

    def check_win(self):
        if self.player.health <= 0:
            self.story_text.insert(tk.END, "You have been defeated...\n")
            self.attack_button['state'] = tk.DISABLED
            self.defend_button['state'] = tk.DISABLED
        elif self.enemy.health <= 0:
            self.story_text.insert(tk.END, "You have defeated the enemy!\n")
            self.attack_button['state'] = tk.DISABLED
            self.defend_button['state'] = tk.DISABLED

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = Game()
    game.run()