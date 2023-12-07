from flask import Flask, render_template, request, redirect, url_for
import requests
from api.helpers.BorgClass import BorgDB
from sample_data.fakeData import fakedata

from api.helpers.helpers import parse_postcode, postcode_to_coordinates, parallel_tfl_requests

# usage: flask --app=api/app.py run
app = Flask(__name__)

dbConnection = BorgDB()


@app.route("/")
def index():
    return render_template("index.html")

def test_db_connection():
    got_dbconnection = False
    try:
        dbConnection.get_connection()
        got_dbconnection = True
    except Exception as e:
        print(e)
        print("DB connection failed.")
    print("DB connected") if got_dbconnection else None


@app.route("/attractions", methods=["GET", "POST"])
def attractions_page():
    if request.method == 'GET':
        # return redirect("/", code=302)
        return render_template("index.html", error="That's not a postcode! Please try another.")
    postcode = request.form.get("inputPostCode")
    test_db_connection()

    attractions_list = get_attractions(postcode)
    if attractions_list == None:
        return render_template("index.html", error="That's not a postcode! Please try another.")

    return render_template(
        "attractions.html", post_code=postcode, attractions=attractions_list
    )


@app.route("/results", methods=["POST"])
def show_res():
    id_attr = request.form.get("id")
    post_code = parse_postcode(request.form.get("post_code"))

    attr_details = dbConnection.get_data_from_db('dbQueries',
                                                 'get_attr_details',
                                                 (id_attr,))[0]

    info = {'name': attr_details[1],
            'type': attr_details[2],
            'subtype': attr_details[3],
            'description': attr_details[4],
            'post_code': attr_details[5],
            'rating': attr_details[6]}

    route_details = get_route_details(post_code, info['post_code'])
    legs = route_details['legs']

    return render_template("results.html", info=info, legs=legs)


def get_attractions(postcode):  # should take in the start postcode
    latitude, longitude = postcode_to_coordinates(postcode)
    if latitude == None or longitude == None:
        return None
    query_results = dbConnection.get_data_from_db('dbQueries',
                                                  'get_attractions', params=(longitude,
                                                                             latitude,
                                                                             latitude))

    attraction_results = parallel_tfl_requests(postcode, query_results)
    attraction_results.sort(key=lambda x: x["duration"])
    return attraction_results


def get_route_details(postcode_source,
                      postcode_dest):  # should take in the start postcode
    postcode_source = parse_postcode(postcode_source)
    postcode_dest = parse_postcode(postcode_dest)
    response = requests.get(
        "https://api.tfl.gov.uk/journey/journeyresults/"
        + postcode_source
        + "/to/"
        + postcode_dest
    )
    data = {}
    if response.status_code == 200:
        data = response.json()["journeys"][0]
        return data
    return data
