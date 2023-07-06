from flask import Flask
import archive

def create_app():
    app = Flask(__name__, template_folder='./templates')
    # relai = Relai(mqtt_host)
    # initialize db here too
    archive.setup()

    from views import views

    app.register_blueprint(views, url_prefix="/")

    return app


if __name__ == "__main__":
    app= create_app()
    app.run(debug=True)