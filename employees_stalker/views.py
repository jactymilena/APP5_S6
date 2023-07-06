from flask import Flask, render_template, Blueprint
from relai import Relai
from db.database import Database

relai = Relai()
db = Database('db/users.cvs')
views = Blueprint("views", __name__)

@views.route('/')
def hello():
    return render_template('index.html', dogs=['dasha', 'luna'])


@views.route('/control')
def get_control():
    return 'This is a control test'


@views.route('/relai')
def test():
    relai.publish_user('test', 'test')
    return 'This is a relai test'


@views.route('/archive')
def get_archive():
    return 'This is an archive test'
