import json

from flask import request
from server.service.app import app
from server.service.shelter_data import ShelterData


@app.route('/shelter',  methods=['POST'])
def add_shelter():
    name = request.form['name']
    address = request.form['address']
    coordinate_x = request.form['coordinate_x']
    coordinate_y = request.form['coordinate_y']
    num_beds = request.form['num_beds']

    with ShelterData() as data:
        data.create(name, address, num_beds, coordinate_y, coordinate_x)

    return 'Shelter added, thank you for using this app.'


@app.route('/shelter/<name>',  methods=['GET'])
def fetch_shelter(name):
    with ShelterData() as data:
        shelter = data.get(name)

    return 'Shelter information: ' + shelter.to_string()


@app.route('/shelter',  methods=['GET'])
def fetch_list_shelter():
    with ShelterData() as data:
        shelter_list = data.get_list()

    shelter_dicts = []
    for shelter in shelter_list:
        shelter_dicts.append(shelter.to_dict())

    return json.dumps(shelter_dicts)


@app.route('/shelter/<name>',  methods=['PUT'])
def update_shelter(name):
    num_beds = request.form['num_beds']

    with ShelterData() as data:
        data.update(name, num_beds)

    return 'Shelter updated'