from flask import Flask, render_template, jsonify, request
from flask_socketio import SocketIO, send 

#initializing application 
app = Flask(__name__)
app.config['SECRET'] = "secret!123"
socketio = SocketIO(app, cors_allowed_origins="*")

#calling sockets to store and display messages 
@socketio.on('message')
def handle_message(message):
    print("Recived message " + message)
    if message != "User connected! ":
        send(message, broadcast = True)

#calling the home page route 
@app.route('/')
def home():
    return render_template('home.html')
#going to the about page 
@app.route('/about')
def about():
    return render_template('about.html')


#calling the chat route 
@app.route('/chat')
def index():
    return render_template("index.html")


#calling the api methods 
@app.route('/api', methods= ['GET','POST'])
def api():
    if (request.method == 'POST'):
        some_json = request.get_json()
        return jsonify({'you sent': some_json}), 201
    else:
        return jsonify({"about": "Hello world!"})
#calling the multi api     
@app.route('/multi/<int:num>', methods=['GET'])
def get_multiply10(num):
    return jsonify({'result': num*10})

#initializing main 
if __name__ == "__main__":
    socketio.run(app, host="localhost")
    #socketio.run(app, host="192.168.56.1")
