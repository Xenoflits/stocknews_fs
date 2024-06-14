from flask import Blueprint, jsonify
from app.controllers import StockController
from flask_cors import CORS
from app.utility import Dates, Calculate

main = Blueprint('main', __name__)
CORS(main)

@main.route('/stockchallenge', methods=['GET'])
def get_stock():
    news = StockController.fetch_stock()
    yesterdayclose = news["Time Series (Daily)"][Dates.yesterday()]["4. close"]
    daybeforeyesterdayclose = news["Time Series (Daily)"][Dates.day_before_yesterday()]["4. close"]
    stock_data = {
        'yesterdays_close': yesterdayclose,
        'day_before_yesterdays_close': daybeforeyesterdayclose,
        'positive difference': Calculate.calculate_difference(yesterdayclose,daybeforeyesterdayclose),
        'news': [
            {'title':'news1'},
            {'title':'news2'},
            {'title':'news3'},
        ]
    }

    return jsonify(stock_data)

# 