from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mission_to_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")


# Route to render index.html template using data from Mongo
@app.route("/")
def index():
    print("This is the index.html")
    mars_data=mongo.db.mars_db.find_one()
    return render_template("index.html", data=mars_data)

@app.route("/scrape")
def scrape():
    print("It is scraping the Mars Data.")
    mars_info = mission_to_mars.scrape_info()
    mongo.db.mars_db.update({},mars_info,upsert=True)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)