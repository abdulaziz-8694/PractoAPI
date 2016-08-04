import json, hashlib
filename = 'doctors.json'
def get_id(name, contact):
    m = hashlib.md5()
    m.update(name + contact)
    return m.hexdigest()

def id_exist(doctors, doc_id):
    for doc in doctors:
        if doc['id'] == doc_id:
            return True
    return False

def get_doctor_list(filename):
    doctor_file = open(filename)
    doctors = json.load(doctor_file)
    doctor_file.close()
    return doctors
