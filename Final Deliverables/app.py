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
    age = request.form.get('Age',False)
    gender = request.form.get('Gender',False)
    tb = request.form.get('Total_Bilirubin',False)
    db = request.form.get('Direct_Bilirubin',False)
    ap = request.form.get('Alkaline_Phosphotase',False)
    aa1 = request.form.get('Alamine_Aminotransferase',False)
    aa2 = request.form.get('Aspartate_Aminotransferase',False)
    tp = request.form.get('Total_Protiens',False)
    a = request.form.get('Albumin',False)
    agr = request.form.get('Albumin_and_Globulin_Ratio',False)

    data = [[float(age),float(gender), float(tb), float(db), float(ap), float(aa1), float(aa2), float(tp), float(a),
             float(agr)]]

    model = pickle.load(open('C:/Users/hp/Downloads/liver_disease_prediction/sample_proj-master/liver_analysis.pkl', 'rb'))
    prediction = model.predict(data)[0]

    if prediction == 1:
        return render_template("Chance.html")
    else:
        return render_template("noChance.html")


if __name__=="__main__":
    app.run(debug=True)