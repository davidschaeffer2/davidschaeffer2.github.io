from flask_app.app import freezer
from flask_app.views import app


if __name__ == '__main__':
    freezer.freeze()
    app.run(debug=True)
