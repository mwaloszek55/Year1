from flask import Flask, render_template
from random import choice, randint

app = Flask(__name__)


@app.route("/rps/<player>")
def rps(player):
    poopylist = ["rock", "paper", "scissors"]
    computer = choice(poopylist)
    if player == "rock" and computer == "scissors":
        winner = player.title()
        return render_template("rps.html", player=player, computer=computer, winner=winner)
    if player == "rock" and computer == "paper":
        winner = computer.title()
        return render_template("rps.html", player=player, computer=computer, winner=winner)
    if player == "paper" and computer == "rock":
        winner = player.title()
        return render_template("rps.html", player=player, computer=computer, winner=winner)
    if player == "paper" and computer == "scissors":
        winner = computer.title()
        return render_template("rps.html", player=player, computer=computer, winner=winner)
    if player == "scissors" and computer == "paper":
        winner = player.title()
        return render_template("rps.html", player=player, computer=computer, winner=winner)
    if player == "scissors" and computer == "rock":
        winner = computer.title()
        return render_template("rps.html", player=player, computer=computer, winner=winner)
    if player == computer:
        return "DRAW!, NOBODY WINS TEHEE LOSERS"


@app.route("/could_it_be_me/<int:num_lines>")
def send_lottery_numbers(num_lines):
    line = []
    for _ in range(6):
        n = randint(1, 47)
        line.append(n)
    return render_template("lotto.html", line=line, num_lines=num_lines)



















