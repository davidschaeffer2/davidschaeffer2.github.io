import os

from flask_app.app import freezer
from flask_app.views import app

if __name__ == '__main__':
    print('cwd: {}'.format(os.getcwd()))
    for url in freezer.all_urls():
        print(url)
    freezer.freeze()
    app.run(debug=True)
