# File: hello_world.py
from flask import Flask
from flask import url_for
from options import Options
from temperature_CO2_plotter import plot_temperature
from temperature_CO2_plotter import plot_CO2
import matplotlib.pyplot as plt
import uuid

app = Flask(__name__)

default_options =  Options(1867, 2017, 1, None, None)

@app.route("/")
def plot_with_default():
    return render_plots(default_options)

def render_plots(options):
    plot_temperature(default_options)
    temperature_url = save_plot_and_return_url()
    
    plot_CO2(default_options)
    co2_url = save_plot_and_return_url()
    
    body = f"""
    <h1>Visualization of temperature and CO2 data</h1>
    {default_options.render()}
    <img src="{temperature_url}" alt="Temperature vs. time plot" height="400" width="1200">
    <img src="{co2_url}" alt="CO2-emission vs. time plot" height="400" width="1200">
    """
    return render_page(body)

def render_page(body):
    html = f"""
    <!doctype html>
    <html lang="en">
      <head>
        <title>Plots</title>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css" integrity="sha384-PsH8R72JQ3SOdhVi3uxftmaW6Vc51MKb0q5P2rRUpPvrszuE4W1povHYgTpBfshb" crossorigin="anonymous">
      </head>
      <body>
        {body}

        <!-- Optional JavaScript -->
        <!-- jQuery first, then Popper.js, then Bootstrap JS -->
        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.3/umd/popper.min.js" integrity="sha384-vFJXuSJphROIrBnz7yo7oB41mKfc8JzQZiCq4NCceLEaO4IHwicKwpJf9c9IpFgh" crossorigin="anonymous"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/js/bootstrap.min.js" integrity="sha384-alpBpkh1PFOepccYVYDB4do5UnbKysX5WZXm3XxPqe5iKTfUKjNkCk9SaVuEZflJ" crossorigin="anonymous"></script>
      </body>
    </html>
    """
    return html


@app.route("/newplot")
def redraw():
    # TODO 
    # read parameters from requiest,
    # make new options
    # return render_plots(options)
    # check parameters?
    # try <input type="range" min="5" max="10" step="0.01">
    html = f"""
    <h1>Fuck you!</h1>
    """
    return html

def save_plot_and_return_url():
    uid = uuid.uuid4()
    plt.savefig(f"static/{uid}.png")
    plt.clf()
    plt.cla()
    return url_for('static', filename=f'{uid}.png')
        

if __name__ == "__main__":
    app.run()