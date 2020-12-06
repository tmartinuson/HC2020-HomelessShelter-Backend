from server.service.app import app


@app.route('/shelter',  methods=['POST'])
def add_shelter():
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
