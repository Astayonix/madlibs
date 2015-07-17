from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

#route to mablib page
@app.route('/madlib')
def show_madlib():
    player = request.args.get("person")
    colors = request.args.get("color")
    nouns = request.args.get("noun")
    adjectives = request.args.get("adjective")
    animals = request.args.get("animal")
    phenomenas = request.args.get("phenomena")
    verbs = request.args.get("verb")

    return render_template("madlib.html", person=player, color=colors, 
        noun=nouns,adjective=adjectives, animal=animals, 
        phenomena=phenomenas,verb=verbs)

#route to game page
@app.route('/game')
def show_game_form():
    player_choice = request.args.get("choice")
    if player_choice=="yes":
        return render_template("game.html")
    else:
        return render_template("goodbye.html")

# route to handle the landing page of a website.
@app.route('/')
def start_here():
    return "Hi! This is the home page."

# route to display a simple web page
@app.route('/hello')
def say_hello():
    return render_template("hello.html")

@app.route('/greet')
def greet_person():
    player = request.args.get("person")

    AWESOMENESS = [
        'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
        'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html", person=player, compliment=compliment)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
