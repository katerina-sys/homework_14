import json

import flask
from flask import Flask
import utils

app = Flask(__name__)



@app.route('/')
def page_main():
    return "<h3>Здесь вы найдете информацию о фильмах и сериалах на платформе Netflix<h3>"


@app.route('/movie/<title>')
def page_title(title):
    result = utils.search_of_title(title)
    return app.response_class(
        response=json.dumps(result),
        status=200
    )


@app.route('/movie/<year1>/to/<year2>')
def page_year(year1, year2):
    result = utils.search_by_release_year(year1, year2)
    return app.response_class(
        response=json.dumps(result),
        status=200
    )


@app.route('/rating/<rating>')
def page_rating(rating):
    result = utils.search_by_rating(rating)
    return app.response_class(
        response=json.dumps(result),
        status=200
    )


@app.route('/genre/<genre>')
def page_genre(genre):
    result = utils.search_by_listed_in(genre)
    return app.response_class(
        response=json.dumps(result),
        status=200
    )


if __name__ == '__main__':
    app.run()
