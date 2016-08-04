### README

#### Dependancies and modules
- [Python 2.7](https://www.python.org/downloads/release/python-2710/)
- [flask](https://pypi.python.org/pypi/Flask/0.11)
- json
- hashlib
- copy

#### Instructions
1. Make sure that all the dependancies are installed.
2. Run the flask app by the following command

    ```$ python run.py```
3. This will start the app on localhost and you can check the API calls using curl or postmaster.

4. Sample curl request

  ```$ curl -i http://localhost:5000/doctors```

#### API calls
- Get all doctors

  HTTP Method : ```GET```

  URI : ```API_endpoint/doctors/```
-  Get a doctor

  HTTP Method : ```GET```

  URI : ```API_endpoint/doctors/<doctor_id>/```
- Create a doctor

  - HTTP Method : ```POST```

  - URI : ```API_endpoint/doctors/```

  - Body : json in the following properties.
    - name (Name of the Doctor)
    - qualifications (Qualifations of the doctor)
    - contact (Contact number for doctor)
    - city (City where doctor is)
    - location (Locality in the area)


- Update a doctor
  - HTTP Method : ```PUT```

  - URI : ```API_endpoint/doctors/<doctor_id>/```

  - body: json with any of the property to change

- Delete a doctor
  - HTTP Method : ```DELETE```

  - URI : ```API_endpoint/doctors/<doctor_id>/```
