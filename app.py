from flask import Flask,render_template,jsonify
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

votes = {"option1" : 0, "option2": 0}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_votes")
def get_votes():
    return jsonify(votes),200

@socketio.on("vote")
def handle_vote(data):
    option = data['option']
    if option in votes:
        votes[option] += 1
        emit("vote_count", votes, broadcast=True)

if __name__ == "__main__":
    socketio.run(app,debug=True)