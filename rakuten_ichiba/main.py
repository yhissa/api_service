import configparser
from flask import Flask, render_template, request
import requests, sys, os
sys.path.append('/home/ranking100/mysite')

file = configparser.ConfigParser()
file.read('./config.txt', 'UTF-8')
# config = configparser.ConfigParser()
# config.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'config.txt'))

app = Flask(__name__)


@app.route('/')
def home(page=1):
    # applicationId = config.get('settings', 'applicationId')
    # genreId = config.get('settings', 'genreId_all_books')
    # page_title = config.get('settings', 'page_title_all_books')
    applicationId = file['settings']['applicationId']
    genreId = file['settings']['genreId_all_books']
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
    response_next = requests.get(endpoint, parameter)
    if response_next.status_code != 200:
        page_next = 'error'
    else:
        page_next = ''

    category = 'all_books'
    return render_template("index.html", results=results['Items'], val=val, page_title=page_title,
                           category=category, page=page, page_next=page_next)


@app.route('/genre/<string:category>')
def genre(category, page=1):
    if request.args.get('page') != None:
        page = request.args.get('page')
        print(page)
    # applicationId = config.get('settings', 'applicationId')
    # genreId = config.get('settings', f'genreId_{category}')
    # page_title = config.get('settings', f'page_title_{category}')
    applicationId = file['settings']['applicationId']
    genreId = file['settings'][f'genreId_{category}']
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
    # get the next page to confirm the next page exists.
    parameter = {
        "format": "json",
        "genreId": genreId,
        "page": int(page)+1,
        "applicationId": applicationId
    }
    response_next = requests.get(endpoint, parameter)
    if response_next.status_code != 200:
        page_next = 'error'
    else:
        page_next = ''

    return render_template("index.html", results=results['Items'], val=val, page_title=page_title,
                           category=category, page=page, page_next=page_next)


if __name__ == '__main__':
    app.run(debug=False)
