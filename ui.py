import ipywidgets as widgets
from IPython.display import display
from datetime import date
import model_generation

"""
Initializes all of the UI widgets and links them to a button that lets a user get a prediction from the input parameters
"""
def initialize(model, regression_err_percent):
    
    header_widget = widgets.Label("Proof of Concept Property Valuation Program / Valuation Data is from 5-2014 through 5-2015 / By Alastair Bennett, WGU Student")
    regression_error_widget = widgets.Label("Average Prediction Deviation from Testing Data: {:.2f}%".format(regression_err_percent * 100))

    date_widget = widgets.DatePicker(value = date(2014, 7, 21), description = "Date of Estimated Value")

    bedroom_widget = widgets.IntSlider(
    value=1,
    min=1,
    max=10,
    step=1,
    description='Bedrooms:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='d'
    )

    bathroom_widget = widgets.IntSlider(
    value=1,
    min=1,
    max=10,
    step=1,
    description='Bathrooms:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='d'
    )

    floors_widget = widgets.IntSlider(
    value=1,
    min=1,
    max=3,
    step=1,
    description='Floors:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='d'
    )

    sqft_widget = widgets.IntSlider(
    value=1250,
    min=300,
    max=10000,
    step=50,
    description='Home Size (sqft):',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='d'
    )

    lot_size_widget = widgets.IntSlider(
    value=7500,
    min=5000,
    max=200000,
    step=500,
    description='Lot Size (sqft):',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='d'
    )

    condition_widget = widgets.IntSlider(
    value=3,
    min=1,
    max=5,
    step=1,
    description='Home Condition:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='d'
    )

    view_widget = widgets.Checkbox(False, description = "View Property")
    waterfront_widget = widgets.Checkbox(False, description = "Waterfront Property")

    estimate_label_widget = widgets.Label(value = "")

    estimate_button = widgets.Button(description="Estimate Value")

    def compute_prediction(event):
        predicted_value = model_generation.generate_prediction(model, 
        [
        date_widget.value,
        bedroom_widget.value, 
        bathroom_widget.value, 
        sqft_widget.value, 
        lot_size_widget.value, 
        floors_widget.value, 
        view_widget.value, 
        waterfront_widget.value, 
        condition_widget.value])
        estimate_label_widget.value = 'Estimated Value: ${:,.2f}'.format(predicted_value)

    estimate_button.on_click(compute_prediction)
    display(header_widget)
    display(regression_error_widget)
    display(date_widget)
    display(bedroom_widget)
    display(bathroom_widget)
    display(floors_widget)
    display(sqft_widget)
    display(lot_size_widget)
    display(condition_widget)
    display(view_widget)
    display(waterfront_widget)
    display(estimate_button)
    display(estimate_label_widget)