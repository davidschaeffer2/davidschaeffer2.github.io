from views import app
from app import freezer

import os

if __name__ == '__main__':
    print('cwd: {}'.format(os.getcwd()))
    for url in freezer.all_urls():
        print(url)
    freezer.freeze()
    app.run(debug=True)
