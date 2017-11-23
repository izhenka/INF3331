class Options:
    def __init__(self, year_from, year_to, month=None, y_min=None, y_max=None):
        self.year_from = year_from
        self.year_to = year_to
        self.month = month
        self.y_min = y_min
        self.y_max = y_max
        
        
    def render(self):
        
        # f"""
        # <form action="/newplot">
        # Year from: <input type="text" class="form-control" name="YearFrom" value="{self.year_from}"><br>
        # Year to: <input type="text" name="YearTo" value="{self.year_to}"><br>
        # Month(for temperature): <input type="text" name="Month" value="{self.month}"><br>
        # Y min: <input type="text" name="YMin" value="{self.y_min}"><br>
        # Y max: <input type="text" name="YMax" value="{self.y_max}"><br>
        # <input type="submit" value="Refresh">
        # </form>
        html = f"""
        <form action="/newplot">
            <div class="container" style="width: 500px; margin-left: 10px; margin-top: 20px;">
                <div class="form-row">
                  <div class="form-group col-md-6">
                    <label for="yearFrom">Year from</label>
                    <input type="text" class="form-control" id="yearFrom" placeholder="Enter year to plot from">
                  </div>
                  <div class="form-group col-md-6">
                    <label for="yearTo">Year to</label>
                    <input type="text" class="form-control" id="yearTo" placeholder="Enter year to plot to">
                  </div>
                </div>
                  <div class="form-group">
                    <label for="month">Month(for temperature)</label>
                    <select class="form-control" id="month">
                      <option value="1">January</option>
                      <option>2</option>
                      <option>3</option>
                      <option>4</option>
                      <option>5</option>
                      <option>6</option>
                      <option>7</option>
                      <option>8</option>
                      <option>9</option>
                      <option>10</option>
                      <option>11</option>
                      <option>12</option>
                    </select>
                  </div>
                  <div class="form-row">
                      <div class="form-group col-md-6">
                        <label for="yMin">Y-value min</label>
                        <input type="text" class="form-control" id="yMin" placeholder="Enter min y-value">
                      </div>
                      <div class="form-group col-md-6">
                        <label for="yMax">Y-value max</label>
                        <input type="text" class="form-control" id="yMax" placeholder="Enter max y-value">
                      </div>
                  </div>
                  <button type="submit" class="btn btn-primary">Refresh</button>
            </div>
        </form>        
        """
        return html