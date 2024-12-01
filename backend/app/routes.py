from modules.modul import app_in

def route(app):
    app.register_blueprint(app_in)