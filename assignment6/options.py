class Options:
    def __init__(self, year_from, year_to, month=None, y_min=None, y_max=None):
        self.year_from = year_from
        self.year_to = year_to
        self.month = month
        self.y_min = y_min
        self.y_max = y_max

            
def render():
    html = f"""
    <form action="/newplot">
    Year from: <input type="text" name="YearFrom" value="{year_from}"><br>
    Year to: <input type="text" name="YearTo" value="{year_to}"><br>
    Month(for temperature): <input type="text" name="Month" value="{month}"><br>
    Y min: <input type="text" name="YMin" value="{y_min}"><br>
    Y max: <input type="text" name="YMax" value="{y_max}"><br>
    <input type="submit" value="Refresh">
    </form>
    """
    return html