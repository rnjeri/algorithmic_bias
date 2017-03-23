from flask import Flask, render_template, request
import _pickle as pickle
 
app = Flask(__name__)
@app.route("/")
def main():
    return render_template('index.html')
@app.route("/about", methods=['GET', 'POST'])
def about_page():
    return render_template('about.html')
@app.route('/calculate', methods=['POST'])
def solve():
    user_data = request.json
    gender, education, race, age = user_data['gender'], user_data['race'], user_data['education'], user_data['age']
    predicted_recidivism = model.predict_proba(gender, education, race, age)
    return jsonify({'predicted_recidivism': predicted_recidivism})
if __name__ == "__main__":
    app.run()

