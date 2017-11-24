import pandas as pd
import matplotlib.pyplot as plt
from options import Options

# pd.set_option('display.mpl_style', 'default')  # Make the graphs a bit prettier
plt.rcParams['figure.figsize'] = (15, 5)

def plot_temperature(options):
    """
    Generates a plot of time vs. temperature
    Options:
        month: [1-12] which month to plot temperatures for 
        year_from, year_to: Time range to plot
        y_min, y_max: y-axis min, max
    """
    assert(options.month>=1 and options.month<=12)
    
    data = pd.read_csv('temperature.csv', sep=',')
    data = data.set_index('Year')
    
    data = data.loc[options.year_from:options.year_to]
    data = data.iloc[:, options.month-1]
    plot = data.plot(kind="line", title = "Average temperature in {}".format(month_from_int(options.month)))
    plot.set_ylabel("Temperature, $^\circ$C")
    plot.set_ylim(options.y_min,options.y_max)


def month_from_int(number):
    """
    Returns month's name from it's number
    """
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return months[number-1]


def plot_CO2(options):
    """
    Generates a plot of CO2 vs. temperature
    Options:
        year_from, year_to: Time range to plot
        y_min, y_max: y-axis min, max
    """
    
    data = pd.read_csv('co2.csv', sep=',')
    data = data.set_index('Year')
    
    data = data.loc[options.year_from:options.year_to]
    plot = data.plot(kind="line", title = "Yearly CO2-emissions")
    plot.set_ylabel("CO2-emission, mln tons")
    plot.set_ylim(options.y_min_co2, options.y_max_co2)
          
     
if __name__ == '__main__':
    plot_temperature(Options(1867, 2017, 4))
    plt.show()
    plot_CO2(Options(1867, 2017))
    plt.show()

     