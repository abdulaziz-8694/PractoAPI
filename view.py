from init import *

@app.route('/', methods=['GET'])
def index():
    return 'Hello This API is a sample API for practo.'

@app.route('/doctors/', methods=['GET'])
def get_doctors():
    doctors = get_doctor_list(filename)
    if doctors == None:
        return 404
    return_data = []
    for doctor in doctors:
        data = {}
        data['uri'] = url_for('get_doctor',
                    doctor_id = doctor['id'])
        data['name'] = doctor['name']
        data['contact'] = doctor['contact']
        return_data.append(data)

    return jsonify({'Doctors': return_data})

@app.route('/doctors/<doctor_id>/', methods=['GET'])
def get_doctor(doctor_id):
    doctors = get_doctor_list(filename)
    for doctor in doctors:
        if doctor['id'] == doctor_id:
            return jsonify({ 'Doctor' : doctor})
    abort(404)

@app.route('/doctors/', methods=['POST'])
def create_doctor():
    doctors = get_doctor_list(filename)

    if request.json == None or 'name' not in request.json\
      or 'contact' not in request.json:
        abort(400)
    try:
        doctor_id = get_id(str(request.json['name']),
                            str(request.json['contact']))
        if id_exist(doctors, doctor_id):
            return jsonify({'error' : 'Doctor already exist'})


        data = dict(
                id = doctor_id,
                name = str(request.json['name']),
                qualifications = request.json['qualifications'] ,
                city = request.json['city'],
                location = request.json['location'],
                contact = str(request.json['contact'])
        )
    except KeyError as e:
        abort(400)
    # print data
    doctors.append(data)
    doctor_file_add = open('doctors.json', 'w')
    json.dump(doctors, doctor_file_add)

    return jsonify({"Error" : "None", 'Response' : 'OK'})

@app.route('/doctors/<doctor_id>/', methods=['PUT'])
def update_doctor(doctor_id):
    doctors = get_doctor_list(filename)
    if request.json == None:
        abort(400)
    for doc in doctors:
        if doc['id'] == doctor_id:
            for field in request.json:
                if field not in doc:
                    abort(400)
                doc[field] = request.json[field]
            doctor_file_update = open(filename,'w+')
            json.dump(doctors, doctor_file_update)
            doctor_file_update.close()
            return jsonify({"Error" : "None", "Response" : "OK"})


    abort(404)

@app.route('/doctors/<doctor_id>/', methods=['DELETE'])
def delete_doctor(doctor_id):
    doctors = get_doctor_list(filename)
    new_doctors = copy.deepcopy(doctors)
    error = False
    for i in xrange(len(doctors)):
        if doctors[i]['id'] == doctor_id:
            new_doctors.remove(new_doctors[i])
            doctor_file_delete = open(filename, 'w+')
            json.dump(new_doctors, doctor_file_delete)
            doctor_file_delete.close()
            return jsonify({"Error" : "None", "Response" : "OK"})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(400)
def bad_rquest(error):
    return make_response(jsonify({'error': 'Bad Request'}), 400)
