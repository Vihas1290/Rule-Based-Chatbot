import colorama
from colorama import Fore, Style, init
import questionary


init(autoreset=True)

history = []

def choice():  
    ch = questionary.select(
        "Choice:",
        choices=['Start', 'Quit', 'Help', 'History']
    ).ask()
    
    if ch == 'Start':
        user_sen = input("Enter your sentence: ")
        if "sad" in user_sen.lower() or "unhappy" in user_sen.lower() or "depressed" in user_sen.lower() or "disappointed" in user_sen.lower():
            print(Fore.RED + "I'm sorry to hear that. Remember, it's okay to feel sad sometimes. If you need someone to talk to, consider reaching out to a friend or a professional.")
            history.append(user_sen)
            choice()
        elif "happy" in user_sen.lower() or "joyful" in user_sen.lower() or "excited" in user_sen.lower() or "content" in user_sen.lower():
            print(Fore.GREEN + "That's great to hear! Keep enjoying the good moments and spread positivity.")
            history.append(user_sen)
            choice()
        else:
            print(Fore.YELLOW + "Thank you for sharing. Remember, it's important to acknowledge your feelings.")
            history.append(user_sen)
            choice()
    elif ch == 'Quit':
        print(Fore.CYAN + "Goodbye! Take care of yourself.")
        exit()
    elif ch == 'Help':
        print(Fore.BLUE + "This is a simple emotional support program. You can share your feelings, and it will respond with supportive messages. Choose 'Start' to share your feelings, 'History' to see past entries, or 'Quit' to exit.")
        history.append("Help requested.")
        choice()
    elif ch == 'History':
        if history:
            print(Fore.MAGENTA + "Your past entries:")
            for entry in history:
                print(Fore.MAGENTA + f"- {entry}")
        else:
            print(Fore.YELLOW + "No history available.")
        choice()

if __name__ == "__main__":
    choice()