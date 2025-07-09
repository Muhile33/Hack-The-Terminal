import random
import time
import os
from colorama import Fore, Style

# === Utility Functions ===
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_out(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def generate_math_question():
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    op = random.choice(['+', '-', '*', '//'])
    if op == '//' and b == 0:
        b = 1
    question = f"{a} {op} {b}"
    answer = eval(question)
    return question, answer

# === Login System ===
def login():
    clear()
    type_out(f"{Fore.GREEN}>>> WELCOME TO HACK THE TERMINAL{Style.RESET_ALL}", 0.02)
    type_out(f"{Fore.GREEN}>>> Secure Login Required\n{Style.RESET_ALL}", 0.02)

    # Fake credentials
    correct_username = "admin"
    correct_password = "rootaccess"

    for attempt in range(3):
        username = input(f"{Fore.YELLOW}Username> {Style.RESET_ALL}").strip()
        password = input(f"{Fore.YELLOW}Password> {Style.RESET_ALL}").strip()
        if username == correct_username and password == correct_password:
            type_out(f"{Fore.GREEN}\n✅ Access Granted. Welcome, Agent.\n{Style.RESET_ALL}", 0.02)
            return True
        else:
            type_out(f"{Fore.RED}❌ Invalid credentials.\n{Style.RESET_ALL}", 0.02)

    type_out(f"{Fore.RED}\n🚨 SYSTEM LOCKED — Unauthorized Access Detected 🚨{Style.RESET_ALL}", 0.02)
    return False

# === Main Game ===
def game():
    type_out(f"{Fore.GREEN}>>> INITIATING SERVER INTRUSION PROTOCOL{Style.RESET_ALL}")
    time.sleep(1)
    type_out(f"{Fore.GREEN}>>> Cracking firewall...{Style.RESET_ALL}")
    time.sleep(1)
    type_out(f"{Fore.GREEN}>>> Accessing math security node...{Style.RESET_ALL}")

    level = 1
    score = 0

    while True:
        print(f"\n[LEVEL {level}] Solve to continue:")
        question, answer = generate_math_question()
        print(f"{Fore.CYAN}🧠 {question}{Style.RESET_ALL}")
        try:
            user_input = input(f"{Fore.YELLOW}Answer> {Style.RESET_ALL}").strip()
            if user_input.lower() == "exit":
                break
            if int(user_input) == answer:
                type_out(f"{Fore.GREEN}✅ ACCESS GRANTED\n{Style.RESET_ALL}", 0.01)
                level += 1
                score += 10
            else:
                type_out(f"{Fore.RED}❌ ACCESS DENIED — TRACE DETECTED!\n{Style.RESET_ALL}", 0.01)
                break
        except ValueError:
            print(f"{Fore.RED}Invalid input. Numbers only!{Style.RESET_ALL}")

    print(f"\nFinal Score: {score}")
    type_out(f"{Fore.RED}>>> TERMINAL LOCKED. MISSION FAILED.{Style.RESET_ALL}" if score < 50 else f"{Fore.GREEN}>>> MISSION COMPLETE. SERVER BREACHED!{Style.RESET_ALL}")

# === Run Game ===
if __name__ == "__main__":
    if login():
        game()
