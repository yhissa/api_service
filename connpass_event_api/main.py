from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import requests


app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def home():
    event_endpoint = "https://connpass.com/api/v1/event/?keyword="
    parameter = "python"

    response = requests.get(event_endpoint+parameter)
    results = response.json()
    print(results['events'])
    return render_template("index.html", results=results['events'])


if __name__ == '__main__':
    app.run(debug=True)
