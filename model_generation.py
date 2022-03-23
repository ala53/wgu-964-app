from datetime import date
import numpy as np
import statsmodels.api as statmodel

"""
Generates a linear regression model from the specified data
"""
def generate_model(training_data):
    # pop the price into a dependent data structure
    training_dependent_price = training_data.pop("price")
    # create the regression model
    training_independent = statmodel.add_constant(training_data)
    linear_model = statmodel.OLS(training_dependent_price, training_independent).fit()

    return linear_model

"""
Generates a predicted value for the model from an array of parameters. In order, the array must specify
- Date
- Bedroom count
- Bathroom count
- House size sqft
- Lot size sqft
- Floors 
- Waterfront property (boolean)
- Property has notable view (boolean)
- Condition of property on 1-5 scale

"""
def generate_prediction(model, parameters):
    prediction_array = [1] # constant factor
    prediction_array.append((parameters[0] - date(2014,5,1)).days) # days since 5/1/14
    prediction_array.append(parameters[1]) # bedrooms
    prediction_array.append(parameters[2]) # bathrooms
    prediction_array.append(parameters[3]) # house size
    prediction_array.append(parameters[4]) # lot size
    prediction_array.append(parameters[5]) # floors
    if parameters[6]:                      # waterfront
        prediction_array.append(1)
    else: 
        prediction_array.append(0)
    if parameters[7]:                      # view
        prediction_array.append(1)
    else: 
        prediction_array.append(0)
    prediction_array.append(parameters[8]) # condition

    cols = np.column_stack(prediction_array)
    cols = statmodel.add_constant(cols)
    return model.predict(cols)[0] # return predicted value