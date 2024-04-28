class AssetRate:
    def __init__(self, year, month, rate, rate_change):
        self.year = year
        self.month = month
        self.rate = rate
        self.rate_change = rate_change

today_asset_rate = AssetRate(year=1403, month=2, rate=620000, rate_change=None)


dollar_rates = []
for rate