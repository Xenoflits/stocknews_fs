from datetime import datetime, timedelta

class Dates():
    @staticmethod
    def yesterday():
        today = datetime.now().date()
        yesterday = today - timedelta(days=1)
        return str(yesterday)
    def day_before_yesterday():
        today = datetime.now().date()
        daybeforeyesterday = today - timedelta(days=2)
        return str(daybeforeyesterday)

class Calculate():
    @staticmethod
    def calculate_difference(first, second):
        difference = second - first
        return str(difference)

print(Dates.yesterday())
print(type(str(Dates.yesterday())))