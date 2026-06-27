from flask import Flask, render_template,request,session, redirect, url_for
from flask_socketio import join_room, leave_room, send, SocketIO


app = Flask(__name__)
app.config["SECRET_KEY"] = "fhffhffhfjsnnsfm"
socketio = SocketIO(app)
rooms = []
@app.route("/",methods=["POST","GET"])
def home():
    return render_template("home.html")

@app.route("/standby",methods=["POST","GET"])
def standby():
    name = request.args.get("name")
    room = request.args.get("room")
    print(name,room)
    rooms.append({"host":name,"room":room})
    return render_template("standby.html")


if __name__ == "__main__":
    socketio.run(app,debug=True)