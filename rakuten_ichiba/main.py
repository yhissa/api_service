import configparser
from flask import Flask, render_template
import requests

file = configparser.ConfigParser()
file.read('./config.txt', 'UTF-8')

app = Flask(__name__)


@app.route('/')
def home():
    applicationId = file['settings']['applicationId']
    genreId = file['settings']['genreId_all_books']
    page = file['settings']['page']
    page_title = file['settings']['page_title_all_books']
    endpoint = "https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628"
    parameter = {
        "format": "json",
        "genreId": genreId,
        "page": page,
        "applicationId": applicationId
    }
    response = requests.get(endpoint, parameter)
    results = response.json()
    val = 0
    return render_template("index.html", results=results['Items'], val=val, page_title=page_title)


@app.route('/genre/<string:category>')
def genre(category):
    applicationId = file['settings']['applicationId']
    genreId = file['settings'][f'genreId_{category}']
    page = file['settings']['page']
    page_title = file['settings'][f'page_title_{category}']
    endpoint = "https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628"
    parameter = {
        "format": "json",
        "genreId": genreId,
        "page": page,
        "applicationId": applicationId
    }
    response = requests.get(endpoint, parameter)
    results = response.json()
    val = 0
    return render_template("index.html", results=results['Items'], val=val, page_title=page_title)


if __name__ == '__main__':
    app.run(debug=True)
