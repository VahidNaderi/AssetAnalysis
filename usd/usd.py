import csv
from statistics import mean
from common import asset_rate


class USD:
    def return_csv_list(self, file_name="USD_IRR.csv"):
        csv_list = []

        with open(file_name, encoding="utf-8-sig") as my_csv:
            csv_dict = csv.DictReader(my_csv)
            for row in csv_dict:
                daily_model = {
                    "date": row["Date"][:-3],
                    "price": round(float(row["Price"])),
                }
                csv_list.append(daily_model)

        return csv_list

    def return_daily_prices(self, csv_list):
        monthly_model = {"month": "value", "data": "value"}
        month_list = ["1360/7"]
        daily_prices = []
        rate_list = []

        for day in csv_list:
            if day["date"] in month_list:
                rate_list.append(day["price"])
            else:
                if rate_list:
                    monthly_model["month"] = month_list[-1]
                    monthly_model["data"] = rate_list
                    daily_prices.append(monthly_model)
                    rate_list = []

                month_list.append(day["date"])
                rate_list.append(day["price"])
                monthly_model = {"month": day["date"], "data": rate_list}

        if rate_list:
            monthly_model["data"] = rate_list
            daily_prices.append(monthly_model)

        return daily_prices

    def return_monthly_prices(self, daily_prices):
        monthly_model = {
            "year": "value",
            "month": "value",
            "average": "value",
            "change": "value",
        }
        monthly_prices = []
        previous_price = round(
            mean(daily_prices[0]["data"])
        )  # quantification because of the first block of database

        for month in daily_prices:
            monthly_model["year"] = month["month"][:4]
            monthly_model["month"] = month["month"][5:]
            monthly_model["average"] = round(mean(month["data"]))
            monthly_model["change"] = round(
                (monthly_model["average"] - previous_price) / previous_price, 2
            )

            if monthly_model["change"] == 0:
                monthly_model["change"] = 0
            # avoiding -0

            monthly_prices.append(monthly_model)

            previous_price = monthly_model["average"]
            monthly_model = {
                "year": "value",
                "month": "value",
                "average": "value",
                "change": "value",
            }

        return monthly_prices

    def write_asset_rate(self, monthly_prices):
        asset_rate_list = []

        for month_data in monthly_prices:
            asset_rate_list.append(
                asset_rate.AssetRate(
                    month_data["year"],
                    month_data["month"],
                    month_data["average"],
                    month_data["change"],
                )
            )

        return asset_rate_list

    def get_data(self):
        csv_list = self.return_csv_list()
        daily_prices = self.return_daily_prices(csv_list)
        monthly_prices = self.return_monthly_prices(daily_prices)
        asset_rate_list = self.write_asset_rate(monthly_prices)

        return asset_rate_list
