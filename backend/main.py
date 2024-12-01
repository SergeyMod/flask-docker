
from app import create_flask_app

if __name__ == '__main__':
    # app.run(debug=False, host='0.0.0.0', port=80)
    create_flask_app().run(host='0.0.0.0', port=5000)
