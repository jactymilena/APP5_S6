from flask import Flask, render_template, Blueprint
from datetime import datetime
from flask import request, jsonify
import json

# from models.relai import Relai
from models.employees_manager import EmployeesManager
from models.archive import Archive
import consts
# from db.database import Database

archive = Archive()
manager = EmployeesManager()
views = Blueprint("views", __name__)

@views.route('/')
def home():
    return render_template('index.html')


@views.route('/archive')
def get_archive():
    return render_template('archive.html', data=archive.get_employees())


@views.route('/control')
def control():
    return render_template('control.html', nb_pers=manager.employees_count())


@views.route('/ids', methods = ['POST'])
def post_ids():
    if request.method == 'POST':
        data = json.loads(request.data)
        print(data['ids'])
        manager.update(data['ids'])
        # relai.notify(manager.get_employees())
        return jsonify(isError= False, message= "Success", statusCode= 200, data= data), 200
        