from app.models import StockModel

class StockController:
    @staticmethod
    def fetch_stock():
        return StockModel.get_stock()