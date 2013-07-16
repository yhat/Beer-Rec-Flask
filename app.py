from flask import Flask, request, render_template, jsonify
from yhat import Yhat
import os


app = Flask(__name__)
yh = Yhat("greg", "fCVZiLJhS95cnxOrsp5e2VSkk0GfypZqeRCntTD1nHA")


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method=="GET":
        return render_template("home.html")
    else:
        data = request.form
        weights = [data['overall'], data['aroma'], data['palate'], data['taste']]
        weights = map(float, weights)
        data = {
            "beer": data['beer'],
            "weights": weights
        }
        results = yh.predict("PydataBeerRec", 6, data)

        return jsonify({"results": results})
    

if __name__ == '__main__':
    app.run(port=int(os.environ.get('PORT', 5000)))

