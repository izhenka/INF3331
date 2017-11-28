# File: hello_world.py
from flask import Flask
from flask import url_for
from flask import request
from flask import render_template
from flask import send_from_directory
from options import Options
from temperature_CO2_plotter import plot_temperature
from temperature_CO2_plotter import plot_CO2
import matplotlib.pyplot as plt
import uuid

app = Flask(__name__)


@app.route("/", methods=['GET'])
def plot_with_default():
    default_options =  Options.get_defaults()
    return render_page(default_options)

def render_page(options):
    plot_temperature(options)
    temperature_url = save_plot_and_return_url()
    
    plot_CO2(options)
    co2_url = save_plot_and_return_url()
    
    return render_template('index.html', temperature_url=temperature_url, co2_url=co2_url, options=options)


@app.route("/", methods=['POST'])
def refresh():    
    options = get_options_from_request()
    error = options.check()
    if not error:
        return render_page(options)
    else:
        return f"<h1>Error! {error}</h1>"
    
    
def get_options_from_request():
    year_from = request.form["yearFrom"]
    year_to = request.form["yearTo"]
    month = request.form["month"]
    y_min = request.form["yMin"]
    y_max = request.form["yMax"]    
    y_min_co2 = request.form["yMinCO2"]
    y_max_co2 = request.form["yMaxCO2"]    
    options = Options(year_from, year_to, month, y_min, y_max, y_min_co2, y_max_co2)
    return options


def save_plot_and_return_url():
    uid = uuid.uuid4()
    plt.savefig(f"static/{uid}.png")
    plt.clf()
    plt.cla()
    return url_for('static', filename=f'{uid}.png')
        
        
@app.route("/doc_options", methods=['GET'])
def doc_options():
    return send_from_directory('static','options_doc.html')


@app.route("/doc_temperature_CO2_plotter", methods=['GET'])
def doc_plotter():
    return send_from_directory('static','temperature_CO2_plotter.html')


if __name__ == "__main__":
    app.run()