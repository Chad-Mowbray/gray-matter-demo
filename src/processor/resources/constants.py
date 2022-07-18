ALL_COST_COLS = [
    "fare_amount",
    "extra",
    "mta_tax",
    "tip_amount",
    "tolls_amount",
    "improvement_surcharge",
    "congestion_surcharge",
    "airport_fee",
    "total_amount",
]

PICKUP_TS = "tpep_pickup_datetime"
DROPOFF_TS = "tpep_dropoff_datetime"
TIME_COLS = [PICKUP_TS, DROPOFF_TS]

PASSENGER_COUNT = ["passenger_count"]

PAYMENT_TYPE = ["payment_type"]

REQUIRED_COLS = ALL_COST_COLS + TIME_COLS + PASSENGER_COUNT + PAYMENT_TYPE
