from views import app
from app import freezer


if __name__ == '__main__':
    freezer.freeze()
    app.run()
