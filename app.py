import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('models/log_reg_model.pkl', 'rb'))
# random_forest_model = pickle.load(open('models/random_forest.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    # return request.form.values()
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    # final_scaled = sc_model.transform(final_features)
    prediction = model.predict(final_features)

    # output/= round(prediction[0], 2)
    if prediction == 1:
        answer = 'Individual with Hepatitis B infection'
    else :
        answer = 'Individual free from Hepatitis B infection:'
    return render_template('index.html', prediction_text = answer  )

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)

    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)