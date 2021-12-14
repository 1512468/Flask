from flask import Flask

# create app 
app= Flask(__name__)

# config api 
@app.route('/news', methods=["GET"])
def get_news():
    pass 

@app.route('news/<int:news_id>', methods='GET')
def get_news_by_id(news_id):
    pass

@app.route('news/add', methods='POST')
def insert_news():
    pass

if __name__== "__main__":
    app.run()