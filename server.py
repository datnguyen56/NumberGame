from flask import Flask, render_template, request, redirect, session, Markup 
import random
app = Flask(__name__)
app.secret_key = "numbergame"

@app.route("/")
def number_game():
    guess_number = random.randrange(0,101)
    if "guess" not in session:
        session["guess"] = guess_number
    return render_template("index.html")

@app.route("/play", methods=["POST"])
def guess_play():
    guess_play = int(request.form["input_guess"])
    random_guess = session["guess"]
    box_color = ""
    box_text = ""
    reset_button = ""
    box_text2=""

    if guess_play == random_guess:
        box_color = "green"
        box_text = "Congratulation!"
        reset_button = Markup('<a href="/"><button type="submit" class="btn btn-primary subbut" value="Submit">Try Again</button><a>')
        return render_template("index.html", box_color=box_color, box_text=box_text,reset_button=reset_button)

    if guess_play > random_guess:
        box_color = "red"
        box_text = "Too high!"
        return render_template("index.html",box_color=box_color, box_text=box_text,reset_button=reset_button)

    if guess_play < random_guess:
        box_color = "red"
        box_text = "Too low!"
        return render_template("index.html", box_color=box_color, box_text=box_text,reset_button=reset_button)

if __name__=="__main__":
    app.run(debug=True)