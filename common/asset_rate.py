class AssetRate:
    def __init__(self, year, month, rate, rate_change):
        self.year = year
        self.month = month
        self.rate = rate
        self.rate_change = rate_change

    def __str__(self):
        return f"Year:{self.year}, Month:{self.month}, Rate:{self.rate}, Change:{self.rate_change}%"