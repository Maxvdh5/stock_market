"""Home page shown when the user enters the application"""
import streamlit as st

import awesome_streamlit as ast


# pylint: disable=line-too-long
def write():
    """Used to write the page in the app.py file"""
    with st.spinner("Loading Home ..."):
        st.write(
            f"# The stock market predictor"
        )
        st.write(
            """
        Welcome to the stock market predictor. This predictor uses a new state-of-the-art model developed by Facebook.
        This application is designed to help users to get a better understanding in how the price of a stock will change
        over time. 
        
        The model trains on history data of the chosen stock market. Each day the market opens on a certain starting 
        price. The difference between these prices will be used to predict the future prices of the stock.
        
        These techniques are not new. However, the special thing about this model is that you can specify the holidays 
        of a country as a parameter as well. The model can use this information to recalibrate it's calculations so it 
        can give a even more detailed prediction. 
        
        Why does this work? The change in price of a stock can have a lot of different reasons. Some of these reasons
        can introduce a bias in the predictions. Holidays are one of the biggest biases in predicting new stock market 
        prices. They cause peaks in sentiment that are not proportional to the actual sentiment. By filtering out these
        biases the predictions will be much more precise. 
    """)