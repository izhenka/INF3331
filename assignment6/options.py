from flask import render_template

class Options:
    
    default_year_from = 1867
    default_year_to = 2017
    default_month = 1
    default_y_min =  None
    default_y_max=  None
        
    def __init__(self, year_from=None, year_to=None, month=None, y_min=None, y_max=None, y_min_co2=None, y_max_co2=None):
        self.year_from = int(year_from) if year_from  else Options.default_year_from
        self.year_to = int(year_to) if year_to  else Options.default_year_to
        self.month = int(month) if month else Options.default_month
        self.y_min = int(y_min) if y_min else Options.default_y_min
        self.y_max = int(y_max) if y_max else Options.default_y_max
        self.y_min_co2 = int(y_min_co2) if y_min_co2 else Options.default_y_min
        self.y_max_co2 = int(y_max_co2) if y_max_co2 else Options.default_y_max

    @classmethod
    def get_defaults(cls):
        return cls()        
    
    
    def render(self):
        return render_template('options.html', options=self)
    
    
    def check(self):
        if self.year_from > self.year_to:
            return "Year from bigger then year to"
        elif self.month<1 or self.month>12:
            return "Wrong month number"
        elif not self.y_min == None and not self.y_max == None and self.y_min > self.y_max:
            return "Y-min is bigger than y-max for temperature"
        elif not self.y_min_co2 == None and not self.y_max_co2 == None and self.y_min_co2 > self.y_max_co2:
            return "Y-min is bigger than y-max for CO2"
        else:
            return ""
        
        
    def __repr__(self):
        return str(self.__dict__)
    
    def month_selected(self, month_number):
        return 'selected' if self.month == month_number else ''
        
        
def isint(value):
  try:
    int(value)
    return True
  except:
    return False
        

        