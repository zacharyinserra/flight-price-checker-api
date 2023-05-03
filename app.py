from flask import Flask
import requests, os

app = Flask(__name__)

# https://rapidapi.com/DataCrawler/api/skyscanner50/
# https://helpdesk.privateinternetaccess.com/kb/articles/pia-desktop-command-line-interface-2


@app.route('/')
def hello_world():
    return 'This is my first API call!'


def get_flight_details(origin, destination, depart_date, return_date):
    leg1 = {'origin': origin, 'destination': destination, 'date': depart_date}
    leg2 = {'origin': destination, 'destination': origin, 'date': return_date}
    legs = '[{}, {}]'.format(leg1, leg2)

    url = "https://skyscanner50.p.rapidapi.com/api/v1/getFlightDetails"

    params = {"itineraryId": "<REQUIRED>", "legs": legs, "adults": "1", "currency": "USD", "countryCode": "US", "market": "en-US"}

    headers = {"X-RapidAPI-Key": os.environ.get('X_RAPIDAPI_KEY'), "X-RapidAPI-Host": os.environ.get('X_RAPIDAPI_HOST')}


if __name__ == '__main__':
    get_flight_details('LOND', 'NYCA', '2023-02-07', '2023-02-14')
    app.run(port=8888)