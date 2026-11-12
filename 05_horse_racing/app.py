from flask import Flask, render_template, session, redirect, url_for
import game

app = Flask(__name__)
app.secret_key = "скачки-секрет-123"

def load_state():
    """Достаёт состояние из session и приводит ключи positions к int."""
    state = session.get("game")
    if state is None:
        return None
    state["positions"] = {int(k): v for k, v in state["positions"].items()}
    return state

def save_state(state):
    """Кладёт состояние в session (Flask сам сделает JSON)."""
    session["game"] = state

@app.route("/")
def index():
    state = load_state()
    if state is None:
        state = game.new_game()
        save_state(state)
    return render_template("index.html", state=state,
                           horses=game.HORSES,
                           track=range(1, game.FINISH_POSITION + 1))

@app.route("/roll", methods=["POST"])
def roll():
    state = load_state()
    if state is None:
        return redirect(url_for("index"))
    game.apply_roll(state)
    save_state(state)
    return redirect(url_for("index"))

@app.route("/reset", methods=["POST"])
def reset():
    session["game"] = game.new_game()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)