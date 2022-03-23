from datetime import date
from distutils.log import error
import numpy as np
import statsmodels.api as statmodel

"""
Computes the relative error of predictions by taking a set of testing data not used in training
and comparing predictions to actual sales price.
"""
def compute_relative_error(model, testing_data):
    # Use the model to generate predictions for each house in the testing dataset
    testing_sales_prices = list(testing_data.pop("price"))
    testing_independent = statmodel.add_constant(testing_data)
    testing_results = list(model.predict(testing_independent))
    error_percentage = []
    # Then, loop through the arrays to compute error percentages
    for i in range(0,len(testing_results)):
        actual_price = testing_sales_prices[i]
        estimated_price = testing_results[i]
        difference_percent = abs((estimated_price - actual_price) / actual_price)
        error_percentage.append(difference_percent)
    
    return np.average(error_percentage)