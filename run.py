from views import app
from app import freezer

if __name__ == '__main__':
    for url in freezer.all_urls():
        print(url)
    freezer.freeze()
    app.run(debug=True)
