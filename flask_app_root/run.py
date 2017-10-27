from flask_app_root.app import app, freezer


if __name__ == '__main__':
    freezer.freeze()
    app.run()
