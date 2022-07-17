class Analyzer:
    def __init__(self, df):
        self.df = df

    # avg price and passenger count per payment type
    # avg price and passenger count per year
    # avg price and passenger count per month

    def price_passenger_per_payment_type(self):
        df = self.df.groupby("payment_type")["fare_amount", "passenger_count"].mean()
        return df

    def price_passenger_per_year(self):
        df = self.df.groupby("year")["fare_amount", "passenger_count"].mean()
        return df

    def price_passenger_per_month(self):
        df = self.df.groupby("month")["fare_amount", "passenger_count"].mean()
        return df
