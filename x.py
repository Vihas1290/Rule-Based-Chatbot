import streamlit as st
import random
import json
import os
import time

# ====================== DATA ======================
CARX_DB = {
    "Common": ["Sparkplug", "Turbo", "Wheelie", "Bolt", "Revver", "Clutch", "Skid", "Piston", "Axle", "Gearhead", "Racer", "Drift", "Hauler", "Cruiser", "Hopper"],
    "Rare": ["Neon", "Shadowride", "Velocity", "Thunderbolt", "Frostbite", "Inferno", "Nightshade", "Blitz", "Phantom", "Overdrive", "Echo", "Surge", "Vortex", "Mirage", "Pulse"],
    "Epic": ["Apex", "Nova", "Eclipse", "Titan", "Fury", "Zenith", "Spectre", "Hyperion", "Ragnarok", "Oblivion"],
    "Legendary": ["Thunderforge", "Voidrider", "Starblaze", "Chronos", "Dracoforge", "Aetherwing", "Stormreaver", "Helios", "Abyss", "Eternity"],
    "Mythic": ["Omega Prime", "Celestial Drift", "Quantum Fury", "Eternal Gear", "Nebula King", "Chaos Engine", "Genesis Core"]
}

RARITY_COLOR = {"Common": "#aaaaaa", "Rare": "#3498db", "Epic": "#9b59b6", "Legendary": "#f1c40f", "Mythic": "#e74c3c"}
RARITY_EMOJI = {"Common": "⚪", "Rare": "🔵", "Epic": "🟣", "Legendary": "🟡", "Mythic": "🔴"}

class Carx:
    def __init__(self, name, rarity):
        self.name = name
        self.rarity = rarity
        self.level = 1
        self.base_rating = random.randint(40, 100) if rarity == "Common" else random.randint(55, 100) if rarity == "Rare" else random.randint(70, 100) if rarity == "Epic" else random.randint(80, 100) if rarity == "Legendary" else random.randint(90, 100)
        self.rating = self.base_rating * 3 + 10
        mult = {"Common":1.0, "Rare":1.4, "Epic":1.9, "Legendary":2.6, "Mythic":3.5}[rarity]
        self.max_hp = int(80 * mult) + random.randint(-10, 20)
        self.dmg = int(18 * mult) + random.randint(-3, 6)

    def to_dict(self):
        return {"name": self.name, "rarity": self.rarity, "level": self.level, "rating": self.rating}

# ====================== GAME ======================
def load_game():
    if os.path.exists("poxgo_save.json"):
        try:
            with open("poxgo_save.json", "r") as f:
                data = json.load(f)
                st.session_state.coins = data.get("coins", 500)
                st.session_state.elixir = data.get("elixir", 5)
                st.session_state.collection = {}
                for k, v in data.get("collection", {}).items():
                    carx = Carx(v["name"], v["rarity"])
                    carx.level = v["level"]
                    carx.rating = v["rating"]
                    st.session_state.collection[k] = carx
        except:
            init_game()
    else:
        init_game()

def init_game():
    st.session_state.coins = 500
    st.session_state.elixir = 5
    st.session_state.collection = {}
    st.session_state.battle_log = []

def save_game():
    data = {
        "coins": st.session_state.coins,
        "elixir": st.session_state.elixir,
        "collection": {k: v.to_dict() for k, v in st.session_state.collection.items()}
    }
    with open("poxgo_save.json", "w") as f:
        json.dump(data, f)

# ====================== SELL FUNCTION ======================
def sell_carx(carx_name):
    for key, carx in list(st.session_state.collection.items()):
        if carx.name.lower() == carx_name.lower():
            gain = {"Common":2, "Rare":5, "Epic":12, "Legendary":25, "Mythic":60}[carx.rarity]
            st.session_state.elixir += gain
            del st.session_state.collection[key]
            save_game()
            st.success(f"💰 Sold **{carx.name}** for **{gain} Elixir**!")
            return True
    return False

# ====================== UI ======================
st.set_page_config(page_title="PoxGo", page_icon="🚗", layout="wide")
st.title("🚗 PoxGo - Carx Collector")

if 'collection' not in st.session_state:
    load_game()

tab1, tab2, tab3, tab4, tab5 = st.tabs(["🎰 Open Pack", "📦 Collection", "⚔️ Battle", "📜 Battle Log", "🛠️ Management"])

with tab1:
    st.header("🎉 Carx Capsule Opening")
    if st.button("🚀 OPEN CARX CAPSULE", type="primary", use_container_width=True):
        if st.session_state.elixir >= 3:
            st.session_state.elixir -= 3
            roll = random.random() * 100
            rarity = "Common" if roll < 40 else "Rare" if roll < 70 else "Epic" if roll < 85 else "Legendary" if roll < 95 else "Mythic"
            name = random.choice(CARX_DB[rarity])
            key = f"{name}_{rarity}"
            new_carx = Carx(name, rarity)

            placeholder = st.empty()
            with placeholder.container():
                st.success(f"**{RARITY_EMOJI[rarity]} {rarity.upper()} CARX UNLOCKED!**")
                st.markdown(f"""<div style="background-color:{RARITY_COLOR[rarity]}; color:white; padding:30px; border-radius:20px; text-align:center; font-size:32px; margin:20px 0;">
                    {RARITY_EMOJI[rarity]} {rarity} {RARITY_EMOJI[rarity]}
                </div>""", unsafe_allow_html=True)
                st.markdown(f"# **{name}**")
                c1, c2, c3, c4 = st.columns(4)
                with c1: st.metric("**HP**", new_carx.max_hp)
                with c2: st.metric("**DMG**", new_carx.dmg)
                with c3: st.metric("**Power**", new_carx.rating)
                with c4: st.metric("**Level**", "1")
                st.warning("⏳ Reveal stays for 30 seconds...")
                for i in range(30, 0, -1):
                    st.caption(f"Continuing in {i} seconds...")
                    time.sleep(1)

            if key not in st.session_state.collection:
                st.session_state.collection[key] = new_carx
                st.session_state.elixir += 1
                st.balloons()
            else:
                st.session_state.coins += 100
            st.session_state.coins += random.choice([150, 300, 550, 700])
            save_game()
            st.rerun()
        else:
            st.error("Not enough Elixir!")

    st.metric("Elixir", st.session_state.elixir)
    st.metric("Coins", st.session_state.coins)

with tab2:
    st.header("Your Collection")
    if st.session_state.collection:
        for key, carx in sorted(st.session_state.collection.items(), key=lambda x: (-["Common","Rare","Epic","Legendary","Mythic"].index(x[1].rarity), -x[1].rating)):
            with st.expander(f"{RARITY_EMOJI[carx.rarity]} {carx.name} ({carx.rarity}) - Lv.{carx.level}"):
                st.write(f"**HP:** {carx.max_hp} | **DMG:** {carx.dmg} | **Power:** {carx.rating}")
    else:
        st.info("Open packs to build your collection!")

with tab3:
    st.header("⚔️ Interactive Battle")
    if not st.session_state.collection:
        st.warning("Collect some Carx first!")
    else:
        selected_name = st.selectbox("Choose your Carx", [c.name for c in st.session_state.collection.values()])
        player = next(c for c in st.session_state.collection.values() if c.name == selected_name)

        if st.button("Start New Battle vs AI", type="primary"):
            opp_rarity = random.choices(["Common","Rare","Epic","Legendary","Mythic"], weights=[40,30,15,10,5])[0]
            opponent = Carx(random.choice(CARX_DB[opp_rarity]), opp_rarity)

            st.session_state.battle_active = True
            st.session_state.player = player
            st.session_state.opponent = opponent
            st.session_state.player_hp = player.max_hp
            st.session_state.opp_hp = opponent.max_hp
            st.session_state.charge = 0
            st.session_state.battle_log = [f"⚔️ Battle Started: {player.name} vs {opponent.name}"]

        if st.session_state.get("battle_active", False):
            p = st.session_state.player
            o = st.session_state.opponent

            st.subheader(f"{p.name} HP: **{st.session_state.player_hp}** | {o.name} HP: **{st.session_state.opp_hp}**")
            st.write(f"Ultimate Charge: {st.session_state.charge}/2")

            action = st.text_input("Your move (1 = Main Attack, 2 = Ultimate if ready):", key="battle_input")

            if st.button("Submit Move"):
                if action in ["1", "2"]:
                    if action == "2" and st.session_state.charge >= 2:
                        dmg = int(p.dmg * 2.3) + random.randint(10, 25)
                        st.session_state.battle_log.append(f"💥 ULTIMATE! {p.name} deals {dmg} damage!")
                        st.session_state.opp_hp -= dmg
                        st.session_state.charge = 0
                    else:
                        dmg = p.dmg + random.randint(-5, 10)
                        st.session_state.battle_log.append(f"⚡ Main Attack! {p.name} deals {dmg} damage!")
                        st.session_state.opp_hp -= dmg
                        st.session_state.charge = min(st.session_state.charge + 1, 2)

                    st.session_state.battle_log.append(f"→ {o.name} HP: {max(0, st.session_state.opp_hp)}")

                    if st.session_state.opp_hp <= 0:
                        st.session_state.battle_log.append(f"🎉 **VICTORY! {p.name} WINS!**")
                        st.session_state.coins += 150
                        st.session_state.battle_active = False
                        save_game()
                        st.rerun()

                    ai_dmg = o.dmg + random.randint(-6, 14)
                    st.session_state.battle_log.append(f"Enemy {o.name} attacks for {ai_dmg} damage!")
                    st.session_state.player_hp -= ai_dmg
                    st.session_state.battle_log.append(f"→ {p.name} HP: {max(0, st.session_state.player_hp)}")

                    if st.session_state.player_hp <= 0:
                        st.session_state.battle_log.append(f"💀 **DEFEAT! {o.name} WINS.**")
                        st.session_state.battle_active = False
                        save_game()
                        st.rerun()

                    st.rerun()

            st.subheader("Current Battle Log")
            for line in st.session_state.get("battle_log", []):
                st.write(line)

with tab4:
    st.header("📜 Battle Log")
    if st.session_state.get("battle_log"):
        for line in st.session_state.battle_log:
            st.write(line)
    else:
        st.info("No active battle.")

with tab5:
    st.header("🛠️ Management")
    st.subheader("Sell Carx")
    if st.session_state.collection:
        carx_to_sell = st.selectbox("Select Carx to Sell", [carx.name for carx in st.session_state.collection.values()])
        if st.button("Sell Selected Carx"):
            if sell_carx(carx_to_sell):
                st.rerun()
    else:
        st.info("No Carx to sell.")

    st.subheader("Currency Conversion")
    if st.button("💱 200 Coins → 1 Elixir"):
        if st.session_state.coins >= 200:
            st.session_state.coins -= 200
            st.session_state.elixir += 1
            save_game()
            st.success("Converted successfully!")
            st.rerun()
        else:
            st.error("Not enough coins!")

st.sidebar.success(f"Total Carx: {len(st.session_state.collection)}")