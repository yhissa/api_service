from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route('/')
def home():
    isbn = "978-4-8222-9227-0"
    event_endpoint = f"https://api.openbd.jp/v1/get?isbn={isbn}&pretty"
    response = requests.get(event_endpoint)
    results = response.json()
    return render_template("index.html", results=results[0]['summary'],
                           price=results[0]['onix']['ProductSupply']['SupplyDetail']['Price'][0]['PriceAmount'])


if __name__ == '__main__':
    app.run(debug=True)
