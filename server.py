"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return '''<!doctype html><html>Hi! This is the home page. 
    <a href="/hello">Give a Compliment</a>
    <a href="/hello">Give a Insult</a></html>'''


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/comp">What's your name? <input type="text" name="person">
          <br>
          <br>
          <label>Choose a word to describe your favorite person:</label>
          <select name="compliment-choice">
            <option value="placeholder">   </option>
            <option value="awesome">Awesome</option>
            <option value="neato">Neato</option>
            <option value="fantastic">Fantastic</option>
            <option value="smashing">Smashing</option>
          </select>
          <input type="submit" value="Compliment me!">
        </form>
        <form action="/diss">
        <label>Choose a word to describe your least favorite person:</label>
          <select name="insult-choice">
            <option value="placeholder">   </option>
            <option value="stinky">Stinky!</option>
            <option value="uncool">Uncool!</option>
            <option value="ridiculous">Ridiculous!/option>
            <option value="season">So last season!</option>
          </select>
          <input type="submit" value="Insult me!">
          <br>
          <br>
          </form>
      </body>
    </html>
    """


@app.route('/comp')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment-choice")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, compliment)


@app.route('/diss')
def insult_person():
    """Get user by name."""

    player = request.args.get("person")

    insult = request.args.get("insult-choice")

    return """
    <!doctype html>
    <html>
      <head>
        <title>An Insult</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, insult)

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
