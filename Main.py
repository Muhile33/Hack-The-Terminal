import random
import threading
import time
from flask import Flask, Response
import json
from sympy import group

# Flask Server

app = Flask(__name__)

def load_cult_groups():
    with open("cult_groups.json", "r") as f:
        data = json.load(f)
    return data["groups"]

@app.route("/")
def index():
    # Dark web 
    return """
    <html>
    <head><title>DarkNet Cult Gateway</title></head>
    <body style="background:black; color:lime; font-family: monospace;">
        <h1>⛧ Dark Web Cult ⛧</h1>
        <p>Welcome, Seeker. You have found the hidden gate.</p>
        <h4>Join us at your own risk...</h4>
        <p><a href="/cultist" style="color:red;">[ Enter Chatroom ]</a></p>
        <br>
        <button style="background-color: black; color: red;">Reveal Cult Groups</button>
    </body>
    </html>
    """

@app.route("/cultist")
def cultist():
    groups = load_cult_groups()
    return Response("\n".join(groups), mimetype="text/plain")


# Math Quiz

def math_quiz(num_qs, difficulty=1):
    for i in range(num_qs):
        a, b = random.randint(1, 10*difficulty), random.randint(1, 10*difficulty)
        answer = a + b
        user = input(f"[Q{i+1}] Solve: {a} + {b} = ")
        if str(user).strip() != str(answer):
            print("❌ Wrong. Cult rejects you...")
            return False
    return True


# Main Game Flow

def start_flask_server():
    app.run(host="0.0.0.0", port=8080)

def main():
    print("""
          ██╗  ██╗ █████╗  ██████╗██╗  ██╗    ████████╗██╗  ██╗███████╗    ████████╗███████╗██████╗ ███╗   ███╗██╗███╗   ██╗ █████╗ ██╗     
          ██║  ██║██╔══██╗██╔════╝██║ ██╔╝    ╚══██╔══╝██║  ██║██╔════╝    ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║████╗  ██║██╔══██╗██║     
          ███████║███████║██║     █████╔╝        ██║   ███████║█████╗         ██║   █████╗  ██████╔╝██╔████╔██║██║██╔██╗ ██║███████║██║     
          ██╔══██║██╔══██║██║     ██╔═██╗        ██║   ██╔══██║██╔══╝         ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║██║╚██╗██║██╔══██║██║     
          ██║  ██║██║  ██║╚██████╗██║  ██╗       ██║   ██║  ██║███████╗       ██║   ███████╗██║  ██║██║ ╚═╝ ██║██║██║ ╚████║██║  ██║███████╗
          ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝       ╚═╝   ╚═╝  ╚═╝╚══════╝       ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝
                                                                                                                                                                                                                                                                                      
          """)                                                                                                                                                 
                                                                                                                                              

                                                                                                                                                       
                                                                                                                                                       

    print("Solve 5 challenges to gain entry...\n")

    if not math_quiz(5, difficulty=1):
        return

    threading.Thread(target=start_flask_server, daemon=True).start()
    time.sleep(2)

    print("[CULT] The ritual page has been summoned.")
    print("Run this in ANOTHER terminal to extract the names:\n")
    print("curl http://127.0.0.1:8080/\n")

    print("Meanwhile, survive 10 trials in the Black Market...\n")
    if not math_quiz(10, difficulty=9):
        return

    print("\n✅ You survived the Black Market trials...\n")

    expected_names = ["N_01yx", "0xion","0day_bl", "DarkEft", "Astxr0th" ]
    print("Enter the cult names (from the curl output), one by one:\n")
    for name in expected_names:
        user = input("> ").strip()
        if user != name:
            print("❌ Wrong name. The Cult disowns you.")
            return

    print("\n🎉 PRAISE THE INITIATE 🎉")
    print("You have earned your place among the shadows...\n")
    
    for i in range(3):
        print(f"Shutting down system in {3-i}...")
        time.sleep(1)

if __name__ == "__main__":
    main()
