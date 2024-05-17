import csv
import AssetRate


def average(lst):
    return round(sum(lst) / len(lst))


class USD:
    def get_data():
        def csv_dict_returner():
            usd_date_list = []

            with open("USD_IRR.csv", encoding="utf-8-sig") as my_csv:
                csv_dict = csv.DictReader(my_csv)
                for row in csv_dict:
                    dict_daily_model = {"date": "value", "price": "value"}
                    dict_daily_model["date"] = row["Date"][:-3]
                    dict_daily_model["price"] = round(float(row["Price"]))
                    usd_date_list.append(dict_daily_model)

            return usd_date_list

        def data_list_returner():
            dict_monthly_model = {"month": "value", "data": "value"}
            month_list = ["1360/7"]
            data_list = []
            rate_list = []

            for i in csv_dict_returner():
                if i["date"] in month_list:
                    rate_list.append(i["price"])
                else:
                    if rate_list:
                        dict_monthly_model["month"] = month_list[-1]
                        dict_monthly_model["data"] = rate_list
                        data_list.append(dict_monthly_model)
                        rate_list = []

                    month_list.append(i["date"])
                    rate_list.append(i["price"])
                    dict_monthly_model = {"month": i["date"], "data": rate_list}

            if rate_list:
                dict_monthly_model["data"] = rate_list
                data_list.append(dict_monthly_model)

            return data_list

        def main_list_returner():
            dict_monthly_model = {
                "year": "value",
                "month": "value",
                "average": "value",
                "change": "value",
            }
            main_list = []
            previous_price = average(
                data_list_returner()[0]["data"]
            )  # quantification because of the first block of database

            for j in data_list_returner():
                dict_monthly_model["year"] = j["month"][:4]
                dict_monthly_model["month"] = j["month"][5:]
                dict_monthly_model["average"] = average(j["data"])
                dict_monthly_model["change"] = round(
                    (dict_monthly_model["average"] - previous_price) / previous_price, 2
                )

                if dict_monthly_model["change"] == 0:
                    dict_monthly_model["change"] = 0
                # avoiding -0

                main_list.append(dict_monthly_model)

                previous_price = dict_monthly_model["average"]
                dict_monthly_model = {
                    "year": "value",
                    "month": "value",
                    "average": "value",
                    "change": "value",
                }

            return main_list

        def asset_rate_writing():
            asset_rate_list = []

            for k in main_list_returner():
                asset_rate_list.append(
                    AssetRate.AssetRate(
                        k["year"], k["month"], k["average"], k["change"]
                    )
                )

            return asset_rate_list

        return asset_rate_writing()
