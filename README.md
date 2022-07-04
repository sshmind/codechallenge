codechallenge project


follow below steps to start codechallenge project:

step 1:
    to start project it's better idea to create a virtual environment and switch on it:
        
        a)[create virtual environment]: virtualenv .venv
        
        b)switch to virtual environment: [linux]$ source .venv/bin/activate / [windows]> .\.venv\Scripts\activate

step 2:
    install project requirements. project requirements saved in requirements.txt file:
    $ pip install -r requirements.txt

step 3:
    at the end we can run project:
    $ python manage.py runserver

step 4:
    you send request follow API list:
        - 127.0.0.1:8000/feed_news/ : save and reteurn 5 last news from https://feeds.npr.org/1004/feed.json
        - 127.0.0.1:8000/download_news_images/{int:count}
        count => number of Article records that you need save their images on your local system

