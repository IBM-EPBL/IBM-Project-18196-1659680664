import os.path
from flask import Flask, render_template, request
import pickle
STATIC_DIR=os.path.abspath('../static')

app = Flask(__name__, template_folder='templates',static_folder=STATIC_DIR)


# @app.route('/')
# def home():

#     #return "<h1> HELLO </h1>"
#     return render_template('home.html')

@app.route('/',methods=["GET"])
def home():
    return render_template('home.html')


@app.route('/Index')
def Index():
    return render_template("Index.html")


@app.route('/data_predict', methods=['POST','GET'])
def data_predict():
    age = request.form['Age']
    gender = request.form['Gender']
    tb = request.form['Total_Bilirubin']
    db = request.form['Direct_Bilirubin']
    ap = request.form['Alkaline_Phosphotase']
    aa1 = request.form['Alamine_Aminotransferase']
    aa2 = request.form['Aspartate_Aminotransferase']
    tp = request.form['Total_Protiens']
    a = request.form['Albumin']
    agr = request.form['Albumin_and_Globulin_Ratio']

    data = [[float(age), float(gender), float(tb), float(db), float(ap), float(aa1), float(aa2), float(tp), float(a),
             float(agr)]]

    model = pickle.load(open('liver_analysis.pkl', 'rb'))
    prediction = model.predict(data)[0]

    if prediction == 1:
        return render_template("Chance.html")
    else:
        return render_template("noChance.html")


if __name__=="__main__":
    app.run(debug=True)