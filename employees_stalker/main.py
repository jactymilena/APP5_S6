from flask import Flask
# import archive

def create_app():
    app = Flask(__name__, template_folder='./templates')

    from views import views

    app.register_blueprint(views, url_prefix="/")
    
    return app


if __name__ == "__main__":
    app= create_app()
    app.run(host='0.0.0.0', debug=True)