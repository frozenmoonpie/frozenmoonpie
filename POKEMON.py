import random

class Pokemon:
    def __init__(self, name, attack, defense, health):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.health = health

    def is_alive(self):
        return self.health > 0

    def revive(self):
        self.health = max(1, self.health * 0.5)  # Revive with 50% health

    def attempt_attack(self, other: "Pokemon") -> bool:
        """
        Attempt an attack on another Pokemon.
        """
        coefficient_of_luck = round(random.uniform(0.7, 1.3), 1)
        damage = round(self.attack * coefficient_of_luck)

        if damage > other.defense:
            health_loss = damage - other.defense
            other.health -= health_loss
            return True
        else:
            return False

def main():
    # Create two random Pokémon
    pokemon1 = Pokemon("Pikachu", random.randint(40, 60), random.randint(30, 50), random.randint(30, 50))
    pokemon2 = Pokemon("Bulbasaur", random.randint(40, 60), random.randint(30, 50), random.randint(30, 50))

    round_count = 0

    while pokemon1.is_alive() and pokemon2.is_alive() and round_count < 10:
        round_count += 1
        print(f"\nRound {round_count}")

        # Pokemon 1 attacks Pokemon 2
        if pokemon1.attempt_attack(pokemon2):
            print(f"{pokemon1.name} attacks {pokemon2.name}!")

            if not pokemon2.is_alive():
                print(f"{pokemon2.name} fainted.")
                if random.choice([True, False]):
                    pokemon2.revive()
                    print(f"{pokemon2.name} is revived with 50% health!")

        # Check if Pokemon 2 is still alive
        if pokemon2.is_alive():
            # Pokemon 2 attacks Pokemon 1
            if pokemon2.attempt_attack(pokemon1):
                print(f"{pokemon2.name} attacks {pokemon1.name}!")

                if not pokemon1.is_alive():
                    print(f"{pokemon1.name} fainted.")
                    if random.choice([True, False]):
                        pokemon1.revive()
                        print(f"{pokemon1.name} is revived with 50% health!")

    # Determine the winner or declare a tie
    if pokemon1.is_alive() and not pokemon2.is_alive():
        print(f"\n{pokemon1.name} wins!")
    elif not pokemon1.is_alive() and pokemon2.is_alive():
        print(f"\n{pokemon2.name} wins!")
    else:
        print("\nIt's a tie!")

if __name__ == "__main__":
    main()
