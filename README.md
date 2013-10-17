Beer-Rec-Flask
==============

A basic demo application for making beer recommendations using Yhat and scikit-learn.

###To Run
    pip install -r requirements.txt
    export YHAT_USERNAME="YOUR USERNAME"
    export YHAT_APIKEY="YOUR APIKEY" 
    python app.py

###Deploying on Heroku
    heroku create
    git push heroku master

###Resources for Recommender
- [Dataset](https://s3.amazonaws.com/demo-datasets/beer_reviews.tar.gz)
- [IPython Notebook](http://nbviewer.ipython.org/20a18d52c539b87de2af)
- [Standalone App Here](http://pydata-beer.herokuapp.com/)
