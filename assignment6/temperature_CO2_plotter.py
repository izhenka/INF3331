import pandas as pd
import matplotlib.pyplot as plt

# pd.set_option('display.mpl_style', 'default')  # Make the graphs a bit prettier
plt.rcParams['figure.figsize'] = (15, 5)

def plot_temperature(year_from, year_to, month):
    """
    Generates a plot of time vs. temperature
    Args:
        month: [1-12] which month to plot temperatures for 
        year_from, year_to: Time range to plot
        y-axis min, max
    """
    assert(month>=1 and month<=12)
    
    data = pd.read_csv('temperature.csv', sep=',')
    data = data.set_index('Year')
    
    
    data = data.loc[year_from:year_to]
    data = data.iloc[:, month-1]
    plot = data.plot(kind="line", title = "Temperature in {} vs. time".format(month_from_int(month)))
    plot.set_ylabel("Temperature, $^\circ$C")
    plt.show()





def plot_CO2():
    return ""


def month_from_int(number):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return months[number-1]
     
     
     
if __name__ == '__main__':
    plot_temperature(1867, 2017, 4)
     