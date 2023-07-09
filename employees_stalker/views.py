from flask import Flask, render_template, Blueprint
from datetime import datetime
from flask import request, jsonify
import json

# from models.relai import Relai
from models.employees_manager import EmployeesManager
# from db.database import Database

# relai = Relai()
manager = EmployeesManager()
# db = Database('db/users.cvs')
views = Blueprint("views", __name__)

@views.route('/')
def hello():
    return render_template('index.html')


@views.route('/archive')
def archive():
    return render_template('archive.html', dogs=['dasha', 'luna'])


@views.route('/control')
def control():
    # TODO: get nnumber of active employees from employees manager
    return render_template('control.html', nb_pers=manager.employees_count())


@views.route('/ids', methods = ['POST'])
def post_ids():
    if request.method == 'POST':
        data = json.loads(request.data)
        print(data['ids'])
        manager.update(data['ids'])
        # relai.notify(manager.get_employees())
        return jsonify(isError= False, message= "Success", statusCode= 200, data= data), 200
        

     
# @views.route('/relai',  methods = ['POST'])
# def update_relai():
    # if request.method == 'POST':
        # data = request.data
        # print(data)
        # relai.publish_user('cc94b74a-f2ec-4c66-88fc-558813b475b0', datetime.now())

    # return 'This is a relai test'


@views.route('/archive')
def get_archive():
    return 'This is an archive test'
