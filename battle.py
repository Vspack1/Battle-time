import random

class Weapon:
    def __init__(self, name, cooldown):
        self.name = name
        self.cooldown = cooldown

class Character:
    def __init__(self, name, hp, atk, phys_def, magic_def, atk_speed, weapon):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.phys_def = phys_def
        self.magic_def = magic_def
        self.atk_speed = atk_speed
        self.weapon = weapon

    def attack(self, target):
        damage = max(1, self.atk - target.phys_def)  # Ensure at least 1 damage
        target.hp -= damage
        print(f"{self.name} attacks {target.name} for {damage} damage.")

class Assassin(Character):
    def skill(self, target):
        damage = self.atk
        self.hp += damage * 0.5  # 50% lifesteal
        target.hp -= damage
        print(f"{self.name} uses skill on {target.name} for {damage} damage and heals for {damage * 0.5}.")

class Guard(Character):
    def skill(self, target):
        damage = self.atk
        target.hp -= damage * 0.5  # Ignore 50% def
        print(f"{self.name} uses skill on {target.name} for {damage * 0.5} damage.")

class Tank(Character):
    def skill(self):
        print(f"{self.name} uses skill to absorb damage and convert to shield.")

class Sniper(Character):
    def skill(self):
        print(f"{self.name} uses skill to increase crit damage by 30% for 3 turns.")

class Magician(Character):
    def skill(self, targets):
        for target in targets:
            target.hp -= self.atk  # Deal magic damage, ignore phys def
            print(f"{self.name} uses skill on {target.name} for {self.atk} magic damage.")

class Support(Character):
    def skill(self):
        print(f"{self.name} uses skill to decrease damage taken by 50%.")

class Angel(Character):
    def skill(self, allies):
        for ally in allies:
            print(f"{self.name} uses skill to buff {ally.name}.")

class Demon(Character):
    def skill(self, enemies):
        for enemy in enemies:
            print(f"{self.name} uses skill to debuff {enemy.name}.")

class Medic(Character):
    def skill(self, allies):
        for ally in allies:
            ally.hp += self.atk  # Heal all units
            print(f"{self.name} uses skill to heal {ally.name} for {self.atk}.")

class Special(Character):
    def skill(self, target):
        print(f"{self.name} uses skill to apply a random effect on {target.name}.")

def choose_character():
    characters = [
        Assassin("Assassin", 100, 20, 10, 10, 5, Weapon("Dagger", 2)),
        Guard("Guard", 150, 15, 20, 10, 3, Weapon("Sword", 3)),
        Tank("Tank", 200, 10, 30, 20, 2, Weapon("Shield", 4)),
        Sniper("Sniper", 80, 25, 5, 10, 6, Weapon("Gun", 3)),
        Magician("Magician", 90, 18, 5, 20, 4, Weapon("Wand", 3)),
        Support("Support", 120, 10, 15, 15, 3, Weapon("Staff", 3)),
        Angel("Angel", 100, 12, 10, 15, 4, Weapon("Buff Staff", 3)),
        Demon("Demon", 100, 12, 10, 15, 4, Weapon("Debuff Staff", 3)),
        Medic("Medic", 110, 8, 10, 15, 3, Weapon("Heal Staff", 3)),
        Special("Special", 100, 15, 10, 10, 4, Weapon("Special Weapon", 3))
    ]

    print("Choose your character by entering the corresponding number:")
    for i, char in enumerate(characters):
        print(f"{i + 1}. {char.name}")

    choice = int(input("Enter your choice: ")) - 1
    return characters[choice]

def main():
    print("Player 1, choose your characters:")
    team1 = [choose_character() for _ in range(3)]

    print("Player 2, choose your characters:")
    team2 = [choose_character() for _ in range(3)]

    while team1 and team2:
        for char in team1:
            if team2:
                target = random.choice(team2)
                char.attack(target)
                if target.hp <= 0:
                    team2.remove(target)

        for char in team2:
            if team1:
                target = random.choice(team1)
                char.attack(target)
                if target.hp <= 0:
                    team1.remove(target)

    if team1:
        print("Team 1 wins!")
    else:
        print("Team 2 wins!")

if __name__ == "__main__":
    main()
