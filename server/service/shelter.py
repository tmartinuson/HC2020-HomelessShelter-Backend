from server.service.app import app
from server.service.shelter_data import ShelterData


@app.route('/shelter',  methods=['POST'])
def add_shelter():
    with ShelterData() as data:
        data.create('name', 'address', 123, 0, 0)

    return 'todo'


@app.route('/shelter/<name>',  methods=['GET'])
def fetch_shelter(name):
    return 'todo'


@app.route('/shelter',  methods=['GET'])
def fetch_list_shelter():
    return 'todo'


@app.route('/shelter/<name>',  methods=['PUT'])
def update_shelter(name):
    return 'todo'
