import os
import requests

api_key = os.getenv("alpha_stock_api_key")
print(api_key)

class StockModel:
    @staticmethod
    def get_stock():
        url="https://www.alphavantage.co/query"
        #required
        parameters = {
            "function": "TIME_SERIES_DAILY",
            "symbol": "TSLA",
            "apikey": api_key
        }
       

        try:
            response = requests.get(url,params=parameters)
            response.raise_for_status()
            data = response.json()
        except requests.exceptions.Timeout:
            print("timed out")
        except requests.exceptions.RequestException as e:
            print(f"an error occured: {e}")
        return data
    