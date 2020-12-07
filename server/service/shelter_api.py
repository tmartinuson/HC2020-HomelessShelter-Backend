import json

from flask import request
from server.service.app import app
from server.service.shelter_data import ShelterData, ShelterAlreadyExistsError, ShelterNotFoundError


@app.route('/shelter',  methods=['POST'])
def add_shelter():
    name = request.form['name']
    address_line_1 = request.form['address_line_1']
    address_line_2 = request.form['address_line_2']
    coordinate_x = request.form['coordinate_x']
    coordinate_y = request.form['coordinate_y']
    num_beds = request.form['num_beds']
    post_code = request.form['post_code']
    phone = request.form['phone']
    email = request.form['email']

    with ShelterData() as data:
        try:
            data.create(name, address_line_1, address_line_2, num_beds, coordinate_y
                        , coordinate_x, post_code, phone, email)
        except ShelterAlreadyExistsError:
            return json.dumps({'error': 'Shelter ' + name + ' already exists'})

    return json.dumps({'message': 'Shelter ' + name + ' added, thank you for using the app.'})


@app.route('/shelter/<name>',  methods=['GET'])
def fetch_shelter(name):
    with ShelterData() as data:
        shelter = data.get(name)

    return json.dumps(shelter.to_dict())


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
        try:
            data.update(name, num_beds)
        except ShelterNotFoundError:
            return json.dumps({'error': 'Shelter not found'})

    return json.dumps({'message': 'Shelter updated'})
