import configparser
from flask import Flask, render_template
import requests

file = configparser.ConfigParser()
file.read('./config.txt', 'UTF-8')

app = Flask(__name__)


@app.route('/')
def home():
    applicationId = file['settings']['applicationId']
    genreId = file['settings']['genreId']
    page = file['settings']['page']
    endpoint = "https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628"
    parameter = {
        "format": "json",
        "genreId": genreId,
        "page": page,
        "applicationId": applicationId
    }
    print(endpoint)
    response = requests.get(endpoint, parameter)
    results = response.json()
    print(results)
    val = 0
    page_title = '楽天　書籍（PC・システム開発）ランキング'
    return render_template("index.html", results=results['Items'], val=val, page_title=page_title)


if __name__ == '__main__':
    app.run(debug=True)
