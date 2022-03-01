from flask import Flask
from flask import render_template
from flask import Response, request, jsonify, json
app = Flask(__name__)

books = {
    "father": {
        "id": "father",
        "title": "Father Comes Home From the Wars",
        "image": "https://images-na.ssl-images-amazon.com/images/I/81c8z1wKEeS.jpg",
        "summary": "Offered his freedom if he joins his master in the ranks of the Confederacy, Hero, a slave, must choose whether to leave the woman and people he loves for what may be another empty promise. As his decision brings him face to face with a nation at war with itself, the ones Hero left behind debate whether to escape or wait for his return, only to discover that for Hero, freedom may have come at a great spiritual cost. A devastatingly beautiful dramatic work, Father Comes Home from the Wars (Parts 1, 2, & 3) is the opening trilogy of a projected nine-play cycle that will ultimately take us into the present.",
        "author": "Suzan-Lori Parks",
        "amazon": "https://www.amazon.com/Father-Comes-Home-Wars-Parts/dp/1559365005",
        "thriftbooks": "https://www.thriftbooks.com/w/father-comes-home-from-the-wars-parts-1-2--3/9450243/item/25084086/?gclid=CjwKCAiAgvKQBhBbEiwAaPQw3OyFbjdy_3Tl6yyV1ZPSs-v_bTYAXUbT4-GcCIMhEnuG9fc69m6EXBoCn9EQAvD_BwE#idiq=25084086&edition=8808993"
    },
}


# ROUTES
@app.route('/')
def welcome():
    global books

    return render_template('home.html', books=books)  

@app.route('/view/<id>')
def view(id=None):
    global books

    book = books[id]

    return render_template('view.html', book=book)

# AJAX FUNCTIONS

if __name__ == '__main__':
   app.run(debug = True)




