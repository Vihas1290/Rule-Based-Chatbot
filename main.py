import time, pandas as pd
from textblob import TextBlob
from colorama import init, Fore


# Init colors
init(autoreset=True)

# Load CSV (same error output)
try: df = pd.read_csv("./imdb_top_1000.csv")
except FileNotFoundError:
    print(Fore.RED + "Error: The file 'imdb_top_1000.csv' was not found."); raise SystemExit

# Unique genres
genres = sorted({g.strip() for xs in df["Genre"].dropna().str.split(", ") for g in xs})

def dots():
    """Prints ... with delay (AI thinking effect)."""
    for _ in range(3): print(Fore.YELLOW + ".", end="", flush=True); time.sleep(0.5)

def senti(p):
    """Polarity -> label."""
    return "Positive 😊" if p > 0 else "Negative 😞" if p < 0 else "Neutral 😐"

def recommend(genre=None, mood=None, rating=None, n=5):
    """Filter by genre/rating, shuffle, analyze Overview polarity, return n (title, polarity) or message."""
    d = df
    # 2) If genre: filter Genre contains (case-insensitive)
    if genre: d = d[d["Genre"].str.contains(genre, case=False, na=False)]
    if rating is not None: d = d[d["IMDB_Rating"] >= rating]
    if d.empty: return "No suitable movie recommendations found."
    need_nonneg = bool(mood)
    out = d.sample(frac=1).reset_index(drop=True)
    
    for _, r in d.iterrows():
        overview = r.get("Overview", "")
        if not overview: continue
        pol = TextBlob(overview).sentiment.polarity
        if not need_nonneg or pol >= 0:
            yield (r["Series_Title"], pol)
            n -= 1
            if n <= 0: break
    
    return out if out else "No suitable movie recommendations found."
    #out was type DataFrame | took bool
    pass

import rich
from rich import print

def show(recs, name):
    """Print in same format: header + numbered 🎥 lines with polarity + senti()."""
    rich.print(f"\n{name}, here are your movie recommendations:\n")
    for i, (t, p) in enumerate(recs, 1):
        rich.print(f"{i}. 🎥 {t} (Polarity: {p:.2f}, {senti(p)})")

def get_genre():
    """Print genres, then ask: Enter genre number or name: (repeat until valid)."""
    
    rich.print("[green]Available genres:[/green]")
    for i, g in enumerate(genres, 1):
        rich.print(f"{i}. [red]{g}[/red]")
    genre_input = input("Enter genre number or name: ")
    # On invalid: print "Invalid input. Try again.\n"
    if genre_input.isdigit():
        genre_index = int(genre_input) - 1
        if 0 <= genre_index < len(genres):
            return genres[genre_index]
    elif genre_input.title() in genres:
        return genre_input.title()
    print("Invalid input. Try again.\n")
    return get_genre()

def get_rating():
    
    """Ask rating or 'skip' (repeat until valid)."""
    if rating_input := input("Enter minimum IMDB rating (7.6-9.3) or 'skip': ").strip().lower():
        if rating_input == "skip":
            return None
        try:
            rating = float(rating_input)
            if 7.6 <= rating <= 9.3:
                return rating
            else:
                rich.print("Rating out of range. Try again.\n", style="bold_red")
        except ValueError:
            rich.print("Invalid input. Try again.\n", style="bold_red")
    # If skip -> None
    # Else float in 7.6..9.3
    # Out of range -> "Rating out of range. Try again.\n"
    # Bad float -> "Invalid input. Try again.\n"
    return get_rating()

# MAIN (students write)
# 1) Print welcome + ask name + greet
# 2) Print 🔍 line
# 3) genre = get_genre(); mood input
# 4) Print "Analyzing mood" + dots(); compute mood polarity + print mood line
# 5) rating = get_rating()
# 6) Print "Finding movies for {name}" + dots()
# 7) recs = recommend(...); if str print red else show()
# 8) Loop ask "Would you like more recommendations? (yes/no):"
#    - no -> print enjoy line + break
#    - yes -> recommend again + show
#    - else -> invalid choice line

def main():
    rich.print("[bold cyan]Welcome to the AI Movie Recommendation System![/bold cyan]")
    name = input("Please enter your name: ").strip()
    rich.print(f"Hello, [green]{name}[/green]! Let's find some great movies for you.\n")
    
    while True:
        rich.print("🔍 Let's start by selecting a genre.")
        genre = get_genre()
        
        mood_input = input("How are you feeling today? (happy/sad/neutral): ").strip().lower()
        rich.print("Analyzing mood", end="")
        dots()
        mood_polarity = TextBlob(mood_input).sentiment.polarity
        rich.print(f"\nYour mood polarity is: {mood_polarity:.2f} ({senti(mood_polarity)})\n")
        
        rating = get_rating()
        
        rich.print(f"Finding movies for [green]{name}[/green]", end="")
        dots()
        
        recs = list(recommend(genre=genre, mood=mood_input, rating=rating))
        if isinstance(recs, str):
            rich.print(f"[bold red]{recs}[/bold red]")
        else:
            show(recs, name)
        
        more = input("\nWould you like more recommendations? (yes/no): ").strip().lower()
        if more == "no":
            rich.print(f"Enjoy your movies, [green]{name}[/green]! 🎬")
            break
        elif more != "yes":
            rich.print("Invalid choice. Please enter 'yes' or 'no'.\n")
