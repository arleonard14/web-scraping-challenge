{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "grand-plastic",
   "metadata": {},
   "outputs": [
    {
     "ename": "IndentationError",
     "evalue": "unexpected indent (<ipython-input-1-6085c67a069e>, line 21)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-1-6085c67a069e>\"\u001b[1;36m, line \u001b[1;32m21\u001b[0m\n\u001b[1;33m    print(\"It is scraping the Mars Data.\")\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mIndentationError\u001b[0m\u001b[1;31m:\u001b[0m unexpected indent\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask, render_template, redirect\n",
    "from flask_pymongo import PyMongo\n",
    "import mission_to_mars\n",
    "\n",
    "# Create an instance of Flask\n",
    "app = Flask(__name__)\n",
    "\n",
    "# Use PyMongo to establish Mongo connection\n",
    "mongo = PyMongo(app, uri=\"mongodb://localhost:27017/mars_app\")\n",
    "\n",
    "\n",
    "# Route to render index.html template using data from Mongo\n",
    "@app.route(\"/\")\n",
    "def index():\n",
    "    print(\"This is index.html\")\n",
    "    mars_data=mongo.db.mars_db.find_one()\n",
    "    return render_template(\"index.html\", data=mars_data)\n",
    "\n",
    "@app.route(\"/scrape\")\n",
    "def scrape():     ss\n",
    "    print(\"It is scraping the Mars Data.\")\n",
    "    mars_info=scrape_mars.title()\n",
    "    mars_info=scrape_mars.paragraph()\n",
    "    mars_info=scrape_mars.feat_img()\n",
    "    mars_info=scrape_mars.facts()\n",
    "    mars_info=scrape_mars.img_store()\n",
    "    mongo.db.mars_db.update({},mars_info,upsert=True)\n",
    "    return redirect(\"/\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    app.run(debug=True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cross-nepal",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "turkish-saudi",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
