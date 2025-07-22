import random
import tkinter as tk

class Game:
    def __init__(self):
        self.user_score = 0
        self.bot_score = 0

    def get_bot_choice(self):
        return random.choice(['Rock', 'Paper', 'Scissor'])

    def get_result(self, user_choice, bot_choice):
        if user_choice == bot_choice:
            return "Draw"
        elif (user_choice == 'Rock' and bot_choice == 'Scissor') or \
             (user_choice == 'Paper' and bot_choice == 'Rock') or \
             (user_choice == 'Scissor' and bot_choice == 'Paper'):
            self.user_score += 1
            return "Win"
        else:
            self.bot_score += 1
            return "Lose"

class GameGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock Paper Scissor Game")
        self.game = Game()

        self.label = tk.Label(master, text="Choose Rock, Paper or Scissor", font=("Arial", 14))
        self.label.pack(pady=10)

        self.buttons_frame = tk.Frame(master)
        self.buttons_frame.pack()

        self.rock_btn = tk.Button(self.buttons_frame, text="Rock", width=10, command=lambda: self.play("Rock"))
        self.rock_btn.grid(row=0, column=0, padx=10)

        self.paper_btn = tk.Button(self.buttons_frame, text="Paper", width=10, command=lambda: self.play("Paper"))
        self.paper_btn.grid(row=0, column=1, padx=10)

        self.scissor_btn = tk.Button(self.buttons_frame, text="Scissor", width=10, command=lambda: self.play("Scissor"))
        self.scissor_btn.grid(row=0, column=2, padx=10)

        self.result_label = tk.Label(master, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(master, text="Your Score: 0 | Bot Score: 0", font=("Arial", 12))
        self.score_label.pack()

    def play(self, user_choice):
        bot_choice = self.game.get_bot_choice()
        result = self.game.get_result(user_choice, bot_choice)

        if result == "Draw":
            message = f"Both chose {user_choice}. It's a draw!"
        elif result == "Win":
            message = f"You chose {user_choice}, bot chose {bot_choice}. You Win!"
        elif result == "Lose":
            message = f"You chose {user_choice}, bot chose {bot_choice}. You Lost!"
        else:
            message = "Unexpected result."

        self.result_label.config(text=message)
        self.score_label.config(
            text=f"Your Score: {self.game.user_score} | Bot Score: {self.game.bot_score}"
        )

# Run the GUI
root = tk.Tk()
gui = GameGUI(root)
root.mainloop()
