from flask import Flask, jsonify, json, render_template, request, url_for, redirect, flash

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("main.html")

@app.route('/healthz')
def healthcheck():
    response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json'
        )
    return response

@app.route('/metrics')
def metrics():
    response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json'
        )
    return response 

if __name__ == "__main__":
    app.run()
