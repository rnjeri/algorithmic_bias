from flask import Flask, render_template, request, make_response
import _pickle as pickle
from io import BytesIO
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import random
from IPython.html.widgets import interact
from matplotlib.legend_handler import HandlerLine2D
import matplotlib.pyplot as plt

app = Flask(__name__)
@app.route("/")
def main():
    return render_template('index.html')
@app.route("/about", methods=['GET', 'POST'])
def about_page():
    return render_template('about.html')

@app.route('/plot.png')
def plot():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    
    cost = 51775
    recidivism = 0.278
    xs =[1,2,3]
    ys = [i * cost * recidivism for i in xs]
    
    ppep_recidivism = 0.078
    y2 = [i * cost* ppep_recidivism for i in xs]
    

    line1, = axis.plot(xs, ys, label = 'general')
    line2, = axis.plot(xs, y2, label = 'ppep')
    plt.setp(line1, color='k', linewidth=2.0)
    plt.setp(line2, color='b', linewidth=2.0)
    axis.legend(handler_map={line1: HandlerLine2D(numpoints=4)})
    canvas = FigureCanvas(fig)
    output = BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response
    

if __name__ == "__main__":
    app.run(debug=True)

