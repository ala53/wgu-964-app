import numpy as np
import pandas as pd
from datetime import datetime,date
from sklearn.model_selection import train_test_split

"""
Parses a housing data CSV file, drops unnecessary columns, and divides it into 2 sets
Returns a tuple of the training and testing datasets
"""
def parse_csv(file):
    def process_date_field(text: str):
        text = text.split("T")[0] # remove the timefield
        parsedDate = datetime.strptime(text, "%Y%m%d")
        days = (parsedDate.date() - date(2014, 5, 1)).days #count number of days since 1/1/2014
        return days
    

    # first, load the housing price data
    housing_data = pd.read_csv(file)
    # then, convert dates into a usable format(number of days since 5/1/2014, as all dates are after that point)
    housing_data["date"] = housing_data["date"].apply(process_date_field)
    # then, drop unnecessary columns
    housing_data.pop("id")
    housing_data.pop("zipcode")
    housing_data.pop("grade")
    housing_data.pop("sqft_above")
    housing_data.pop("sqft_basement")
    housing_data.pop("yr_built")
    housing_data.pop("yr_renovated")
    housing_data.pop("lat")
    housing_data.pop("long")
    housing_data.pop("sqft_living15")
    housing_data.pop("sqft_lot15")

    # then, split the rows into a training and testing set, with a static selection seed so the same rows
    # are chosen each run
    np.random.seed(0)
    housing_data_training, housing_data_testing = train_test_split(housing_data, train_size = 0.9, test_size = 0.1, random_state = 0)
    return housing_data_training, housing_data_testing