from flask import Flask, render_template, Blueprint
from datetime import datetime
from flask import request

from models.relai import Relai
# from db.database import Database

relai = Relai()
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
    # TODO: 
    return render_template('control.html', nb_pers=2)


@views.route('/ids', methods = ['POST'])
def post_ids():
    if request.method == 'POST':
        data = request.data
        print(data)
        

        
@views.route('/relai',  methods = ['POST'])
def test():
    if request.method == 'POST':
        data = request.data
        print(data)
        # relai.publish_user('cc94b74a-f2ec-4c66-88fc-558813b475b0', datetime.now())

    return 'This is a relai test'


@views.route('/archive')
def get_archive():
    return 'This is an archive test'
