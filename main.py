from flask import Flask, flash, redirect, render_template, request, session, abort
from bokeh.embed import server_document
# import bokeh
app = Flask(__name__)

@app.route("/")
def main():
    script=server_document("http://graphsmart2.herokuapp.com/app")
    return render_template('flaskbokeh1.html',bokS=script)

if __name__ == "__main__":
    app.run()


#bokeh serve serv_1.py --allow-websocket-origin=127.0.0.1:5000
