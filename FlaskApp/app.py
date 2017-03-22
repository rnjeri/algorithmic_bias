from flask import Flask, render_template
import _pickle as pickle 
app = Flask(__name__)
@app.route("/")
def main():
    return render_template('index.html')
@app.route("/about", methods=['GET', 'POST'])
def about_page():
    return render_template('about.html')
if __name__ == "__main__":
    app.run()

