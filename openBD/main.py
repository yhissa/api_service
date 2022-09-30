from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route('/')
def home():
    #https://api.openbd.jp/v1/ get?isbn=978-4-7808-0204-7&pretty
    isbn = "978-4-8222-9227-0"
    event_endpoint = f"https://api.openbd.jp/v1/get?isbn={isbn}&pretty"
    print(event_endpoint)
    response = requests.get(event_endpoint)
    print(response)
    results = response.json()
    print(results[0]['summary'])
    return render_template("index.html", results=results[0]['summary'])
    #return render_template("index.html", results=results[0]['summary'], price=results[0]['onix']['ProductSupply']['SupplyDetail']['Price']['PriceAmount'])


if __name__ == '__main__':
    app.run(debug=True)
