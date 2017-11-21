import pandas as pd
import matplotlib.pyplot as plt

# pd.set_option('display.mpl_style', 'default')  # Make the graphs a bit prettier
plt.rcParams['figure.figsize'] = (15, 5)

def plot_temperature(year_from, year_to, month, y_min=None, y_max=None):
    """
    Generates a plot of time vs. temperature
    Args:
        month: [1-12] which month to plot temperatures for 
        year_from, year_to: Time range to plot
        y_min, y_max: y-axis min, max
    """
    assert(month>=1 and month<=12)
    
    data = pd.read_csv('temperature.csv', sep=',')
    data = data.set_index('Year')
    
    
    data = data.loc[year_from:year_to]
    data = data.iloc[:, month-1]
    plot = data.plot(kind="line", title = "Average temperature in {}".format(month_from_int(month)))
    plot.set_ylabel("Temperature, $^\circ$C")
    if y_min!=None and y_max!=None:
        plot.set_ylim(y_min,y_max)
    # plt.show()

def month_from_int(number):
    """
    Returns month's name from it's number
    """
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return months[number-1]



def plot_CO2(year_from, year_to, y_min=None, y_max=None):
    """
    Generates a plot of CO2 vs. temperature
    Args:
        year_from, year_to: Time range to plot
        y_min, y_max: y-axis min, max
    """
    
    data = pd.read_csv('co2.csv', sep=',')
    data = data.set_index('Year')
    
    
    data = data.loc[year_from:year_to]
    plot = data.plot(kind="line", title = "Yearly CO2-emissions")
    plot.set_ylabel("CO2-emission, mln tons")
    if y_min!=None and y_max!=None:
        plot.set_ylim(y_min,y_max)
    # plt.show()

     
     
     
if __name__ == '__main__':
    plot_temperature(1867, 2017, 4)
    plt.show()
    plot_CO2(1867, 2017)
    plt.show()

     