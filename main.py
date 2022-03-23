# This code is kept out of the jupyter notebook for cleanliness
# With this, only 1 line of code shows up in the notebook itself
import parser
import model_generation
import ui
import accuracy_validation
from datetime import datetime
"""
Initializes the Jupyter notebook by loading data, building the model, computing error level, and showing a UI. Also provides
logging and error handling functions.
"""
def init():
    try:
        # load the data
        # the original dataset was taken fron https://www.kaggle.com/harlfoxem/housesalesprediction/data
        training_data, testing_data = parser.parse_csv("seattle_house_data.csv")
        model = model_generation.generate_model(training_data)
        computed_relative_error = accuracy_validation.compute_relative_error(model, testing_data)
        # log the prediction error level
        with open("error_log.txt", "a") as file:
            file.write("Application initialized. Current prediction error: " + str(computed_relative_error) + "\n")
        # show the UI
        ui.initialize(model, computed_relative_error)
    except Exception as e:
        # Log exceptions for later debugging
        # while still keeping the program open for use if possible
        with open("error_log.txt", "a") as file:
            file.write("Exception at " + str(datetime.now()) + ": " + str(e) + "\n")