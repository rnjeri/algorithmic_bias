from flask import Flask, render_template, request, jsonify
 
app = Flask(__name__)
@app.route("/")
def main():
    return render_template('index.html')
@app.route("/blog", methods=['GET', 'POST'])
def about_page():
    return render_template('blog.html')
@app.route("/contact", methods=['GET', 'POST'])
def contact_me():
    return render_template('contact.html')
@app.route("/about", methods=['GET', 'POST'])
def about_me():
    return render_template('about.html')
@app.route("/calculate", methods=["POST"])
def calculator():
    user_data = request.json
    age, gender, race = user_data['age'], user_data['gender'], user_data['race']
    predicted_recidivism = _calculate_overall_recidivism(age, gender, race)
    alt_life_recidivism = _alternate_life_recidivism(race, _calculate_overall_recidivism(age, gender, race))
    return jsonify({'predicted_recidivism': predicted_recidivism, 'alt_life_recidivism': alt_life_recidivism})
def _calculate_overall_recidivism(age, race, gender):
    return (_age_recidivism_prediction(age) +  _race_recidivism_prediction(race) + _gender_recidivism_prediction(gender))/3
def _alternate_life_recidivism(race, predicted_recidivism):
    if race == 'White':
        return predicted_recidivism /2
    elif race == 'Black':
        return predicted_recidivism *2
    else:
        return predicted_recidivism
def _gender_recidivism_prediction(gender):
    if gender == 'Female':
        return 20.1
    else:
        return 28.9
def _race_recidivism_prediction(race):
    if race == 'White':
        return 27.5
    elif race == 'Black':
        return 30.4
    elif race == 'Hispanic':
        return 24.6
    elif race == 'N. American Indian':
        return 34.2
    elif race== 'Asian/Pacific Islander':
        return 23.0
    else:
      return 17.6
def _age_recidivism_prediction(age):
    if age <= 19:
        return 29.3
    elif age >= 20 and age <= 24:
        return 33.9
    elif age >= 25 and age <= 29:
        return 30.8
    elif age >= 30 and age <= 34:
        return 30.0
    elif age >= 35 and age <= 39:
        return 30.2
    elif age >= 40 and age <= 44:
        return 25.1
    elif age >= 45 and age <= 49:
        return 23.1
    elif age >= 50 and age <= 54:
        return 17.8
    else:
        return 9.8
if __name__ == "__main__":
    app.run(debug=True)

