#name the file as main.py , uncomment the imports and basic functions, complete  the code by writing remainig functions 

import re, random
from colorama import Fore, init

init(autoreset=True)

history = []

def help():
     print(Fore.CYAN + "You can ask me about travel destinations or request a joke!")
     print(Fore.CYAN + "For example, you can type 'beach', 'mountain', 'city', or 'joke'.")
     print(Fore.CYAN + "Type 'packing' to end the conversation.")

destinations = {
     "beaches": ["Bali", "Maldives", "Phuket"],
     "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
     "cities": ["Tokyo", "Paris", "New York"]
 }
jokes = [
     "Why don't programmers like nature? Too many bugs!",
     "Why did the computer go to the doctor? Because it had a virus!",
     "Why do travelers always feel warm? Because of all their hot spots!"
]
def normalize_input(text):
     return re.sub(r"\s+", " ", text.strip().lower())

def chat():
     
     print(Fore.CYAN + "Hello! I'm your travel assistant. How can I help you today?") #info
     while True:
         user_input = input(Fore.GREEN + "You: ")
         normalized_input = normalize_input(user_input)

         if "beach" in normalized_input:
             print(Fore.YELLOW + f"Here are some beach destinations: {random.choice(destinations['beaches'])}")
             history.append(normalized_input)
         elif "mountain" in normalized_input:
             print(Fore.YELLOW + f"Here are some mountain destinations: {random.choice(destinations['mountains'])}")
             history.append(normalized_input)
         elif "city" in normalized_input:
             print(Fore.YELLOW + f"Here are some city destinations: {random.choice(destinations['cities'])}")
             history.append(normalized_input)
         elif "joke" in normalized_input:
             print(Fore.MAGENTA + random.choice(jokes))
             history.append(normalized_input)
         elif "packing" in normalized_input:
             print(Fore.CYAN + "Goodbye! Safe travels!")
             history.append(normalized_input)
             break
         elif "help" in normalized_input:
             help()
             history.append(normalized_input)
         elif "history" in normalized_input:
             print(Fore.CYAN + "Here's your conversation history:")
             for entry in history:
                 print(Fore.CYAN + f"- {entry}")
             history.append(normalized_input)
         else:
               print(Fore.RED + "I'm sorry, I didn't understand that. Can you please specify if you're looking for beaches, mountains, cities, or a joke?")
               history.append(normalized_input)


if __name__ == "__main__":
     chat()