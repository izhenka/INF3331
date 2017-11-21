# File: hello_world.py
from flask import Flask
from flask import url_for
from temperature_CO2_plotter import plot_temperature
from temperature_CO2_plotter import plot_CO2
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route("/")
def hello():
    plot_temperature(1867, 2017, 4)
    plt.savefig("static/temperature.png")
    temperature_url = url_for('static', filename='temperature.png')
    
    plot_CO2(1867, 2017)
    plt.savefig("static/co2.png")
    co2_url = url_for('static', filename='co2.png')
    
    html = f"""
    <h1>Plots</h1>
    <img src="{temperature_url}" alt="Temperature vs. time plot" height="400" width="1200">
    <img src="{co2_url}" alt="CO2-emission vs. time plot" height="400" width="1200">
    """
    return html

if __name__ == "__main__":
    app.run()