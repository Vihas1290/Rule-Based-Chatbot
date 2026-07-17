import random
import json
import os

# Carx Database
CARX_DB = {
    "Common": ["Sparkplug", "Turbo", "Wheelie", "Bolt", "Revver", "Clutch", "Skid", "Piston", "Axle", "Gearhead", "Racer", "Drift", "Hauler", "Cruiser", "Hopper"],
    "Rare": ["Neon", "Shadowride", "Velocity", "Thunderbolt", "Frostbite", "Inferno", "Nightshade", "Blitz", "Phantom", "Overdrive", "Echo", "Surge", "Vortex", "Mirage", "Pulse"],
    "Epic": ["Apex", "Nova", "Eclipse", "Titan", "Fury", "Zenith", "Spectre", "Hyperion", "Ragnarok", "Oblivion"],
    "Legendary": ["Thunderforge", "Voidrider", "Starblaze", "Chronos", "Dracoforge", "Aetherwing", "Stormreaver", "Helios", "Abyss", "Eternity"],
    "Mythic": ["Omega Prime", "Celestial Drift", "Quantum Fury", "Eternal Gear", "Nebula King", "Chaos Engine", "Genesis Core"]
}

RARITY_COLORS = {
    "Common": "\033[37m", "Rare": "\033[94m", "Epic": "\033[95m",
    "Legendary": "\033[93m", "Mythic": "\033[91m"
}
RESET = "\033[0m"

class Carx:
    def __init__(self, name, rarity):
        self.name = name
        self.rarity = rarity
        self.level = 1
        self.base_rating = random.randint(40, 100) if rarity == "Common" else \
                          random.randint(55, 100) if rarity == "Rare" else \
                          random.randint(70, 100) if rarity == "Epic" else \
                          random.randint(80, 100) if rarity == "Legendary" else \
                          random.randint(90, 100)
        self.rating = self.base_rating * 3 + 10

        # Stats by rarity
        rarity_mult = {"Common": 1.0, "Rare": 1.4, "Epic": 1.9, "Legendary": 2.6, "Mythic": 3.5}[rarity]
        self.hp = int(80 * rarity_mult) + random.randint(-10, 20)
        self.max_hp = self.hp
        self.dmg = int(18 * rarity_mult) + random.randint(-3, 6)

    def upgrade(self):
        if self.level >= 5:
            return False
        costs = [0, 200, 400, 600, 1000]
        cost = costs[self.level]
        return cost

    def to_dict(self):
        return {"name": self.name, "rarity": self.rarity, "level": self.level, "rating": self.rating}

    def heal(self):
        self.hp = self.max_hp

class PoxGoGame:
    def __init__(self):
        self.coins = 500
        self.elixir = 5
        self.collection = {}
        self.load_progress()

    def save_progress(self):
        data = {
            "coins": self.coins,
            "elixir": self.elixir,
            "collection": {k: v.to_dict() for k, v in self.collection.items()}
        }
        with open("poxgo_save.json", "w") as f:
            json.dump(data, f)

    def load_progress(self):
        if os.path.exists("poxgo_save.json"):
            try:
                with open("poxgo_save.json", "r") as f:
                    data = json.load(f)
                    self.coins = data.get("coins", 500)
                    self.elixir = data.get("elixir", 5)
                    for k, v in data.get("collection", {}).items():
                        carx = Carx(v["name"], v["rarity"])
                        carx.level = v["level"]
                        carx.rating = v["rating"]
                        self.collection[k] = carx
            except:
                pass

    def open_capsule(self):
        if self.elixir < 3:
            print("❌ Not enough Elixir!")
            return
        self.elixir -= 3
        print(f"\n💎 Spending 3 Elixir... ({self.elixir} left)")
        print("🎉 Opening Carx Capsule...")

        roll = random.random() * 100
        rarity = "Common" if roll < 40 else "Rare" if roll < 70 else "Epic" if roll < 85 else "Legendary" if roll < 95 else "Mythic"
        name = random.choice(CARX_DB[rarity])
        key = f"{name}_{rarity}"

        print(f"{RARITY_COLORS[rarity]}✨ You got a {rarity} Carx: {name}! ✨{RESET}")

        if key in self.collection:
            print("   (Duplicate - +100 bonus coins!)")
            self.coins += 100
        else:
            self.collection[key] = Carx(name, rarity)
            print("   🎊 New Carx unlocked! +1 Elixir bonus!")
            self.elixir += 1

        self.coins += random.choice([150, 300, 550, 700])
        print(f"   +Coins! Total: {self.coins}")
        self.save_progress()

    def show_collection(self):
        print("\n" + "="*60)
        print("YOUR CARX COLLECTION")
        print("="*60)
        if not self.collection:
            print("No Carx yet!")
            return
        sorted_carx = sorted(self.collection.values(), key=lambda x: (-["Common","Rare","Epic","Legendary","Mythic"].index(x.rarity), -x.rating))
        for carx in sorted_carx:
            color = RARITY_COLORS[carx.rarity]
            print(f"{color}{carx.name} ({carx.rarity}) Lv.{carx.level} | HP:{carx.hp} DMG:{carx.dmg} | Rating:{carx.rating}{RESET}")

    def upgrade_carx(self):
        self.show_collection()
        if not self.collection: return
        choice = input("\nEnter Carx name to upgrade (cancel): ").strip()
        if choice.lower() == 'cancel': return
        for key, carx in self.collection.items():
            if carx.name.lower() == choice.lower():
                cost = carx.upgrade()
                if not cost: print("Max level!"); return
                if self.coins >= cost:
                    self.coins -= cost
                    carx.level += 1
                    carx.rating = int(carx.base_rating * (1 + (carx.level-1)*0.2)) * 3 + 10
                    print(f"✅ Upgraded to Level {carx.level}!")
                    self.save_progress()
                else:
                    print("Not enough coins.")
                return
        print("Not found.")

    def sell_carx(self):
        self.show_collection()
        if not self.collection: return
        choice = input("\nEnter Carx name to SELL (cancel): ").strip()
        if choice.lower() == 'cancel': return
        for key, carx in list(self.collection.items()):
            if carx.name.lower() == choice.lower():
                gain = {"Common":2,"Rare":5,"Epic":12,"Legendary":25,"Mythic":60}[carx.rarity]
                self.elixir += gain
                del self.collection[key]
                print(f"💰 Sold for {gain} Elixir!")
                self.save_progress()
                return
        print("Not found.")

    def battle(self):
        if not self.collection:
            print("You need at least one Carx!")
            return
        self.show_collection()
        choice = input("\nChoose your Carx for battle: ").strip()
        player = next((c for c in self.collection.values() if c.name.lower() == choice.lower()), None)
        if not player:
            print("Carx not found.")
            return

        # AI Opponent
        opp_rarity = random.choices(["Common","Rare","Epic","Legendary","Mythic"], weights=[40,30,15,10,5])[0]
        opp_name = random.choice(CARX_DB[opp_rarity])
        opponent = Carx(opp_name, opp_rarity)

        print(f"\n⚔️  Battle: {player.name} (You) vs {opponent.name} (AI) ⚔️")

        player.heal()
        opponent.heal()

        while player.hp > 0 and opponent.hp > 0:
            print(f"\nYour {player.name} HP: {player.hp} | Enemy HP: {opponent.hp}")
            print("1. Main Attack")
            print("2. Ultimate Attack (Stronger)")
            act = input("Choose attack: ").strip()

            # Player Attack
            if act == "2":
                dmg = int(player.dmg * 1.8) + random.randint(5,15)
                print(f"💥 ULTIMATE! {player.name} deals {dmg} damage!")
            else:
                dmg = player.dmg + random.randint(-3,8)
                print(f"⚡ Main attack! {player.name} deals {dmg} damage!")
            opponent.hp -= dmg

            if opponent.hp <= 0:
                print(f"🎉 Victory! {player.name} defeated {opponent.name}!")
                self.coins += 120
                break

            # AI Attack
            ai_dmg = opponent.dmg + random.randint(-5,10)
            print(f"Enemy {opponent.name} attacks for {ai_dmg} damage!")
            player.hp -= ai_dmg

            if player.hp <= 0:
                print("💀 You lost the battle...")
                break

        self.save_progress()

    def show_stats(self):
        total = len(self.collection)
        mythic = sum(1 for c in self.collection.values() if c.rarity == "Mythic")
        print(f"\n📊 Total Carx: {total} | Mythic: {mythic} | Coins: {self.coins} | Elixir: {self.elixir}")

    def convert_coins_to_elixir(self):
        try:
            amount = int(input(f"\nHow many Elixir (200 Coins each)? You have {self.coins} Coins: "))
            if amount > 0 and self.coins >= amount * 200:
                self.coins -= amount * 200
                self.elixir += amount
                print(f"✅ +{amount} Elixir!")
                self.save_progress()
            else:
                print("Not enough coins.")
        except:
            print("Invalid input.")

def main():
    game = PoxGoGame()
    print("\n🚗 Welcome to PoxGo - Carx Collector! 🚗")
    print("💎 3 Elixir per pack | Sell Carx | Battle AI")

    while True:
        print("\n" + "-"*45)
        print("1. Open Capsule (3 Elixir)")
        print("2. View Collection")
        print("3. Upgrade Carx")
        print("4. Sell Carx for Elixir")
        print("5. Battle vs AI")
        print("6. Convert Coins → Elixir")
        print("7. Stats")
        print("8. Exit")
        choice = input("\nChoose action: ").strip()

        if choice == "1": game.open_capsule()
        elif choice == "2": game.show_collection()
        elif choice == "3": game.upgrade_carx()
        elif choice == "4": game.sell_carx()
        elif choice == "5": game.battle()
        elif choice == "6": game.convert_coins_to_elixir()
        elif choice == "7": game.show_stats()
        elif choice == "8":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()