from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def homepage():
    """Render the homepage"""
    return render_template('homepage.html')

@app.route('/games')
def list_all():
    """Render the list of all games"""
    return render_template('list.html')

@app.route('/games/<game_id>')
def one_game(game_id):
    """Render a single game page"""
    context = {
        'game_id': game_id
    }
    return render_template('one-game.html', **context)

if __name__ == '__main__':
    app.run(debug=True)
