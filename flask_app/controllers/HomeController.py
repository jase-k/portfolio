from flask import render_template
from flask_app import app



@app.route('/')
def showAllPhotos():
    return render_template('index.html')