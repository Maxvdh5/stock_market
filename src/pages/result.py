"""Home page shown when the user enters the application"""
import streamlit as st
from src.utils import cache
from streamlit import caching
from fbprophet import Prophet
import pandas as pd


@st.cache
def get_model(data):
    m = Prophet()
    m.fit(data)
    return m


def write():
    session_state = cache()
    hist = session_state["mrkt"].history(start=session_state["begin"], end=session_state["end"],)
    hist = hist.reset_index()

    data = pd.DataFrame(data={'ds': hist['Date'], 'y': hist['Open']})

    m = get_model(data)

    future = m.make_future_dataframe(periods=session_state["days"])

    forecast = m.predict(future)

    st.title("Results")
    st.write(
        """
        Welcome to the results! you can click the graphs to expand them.
        """
    )

    st.pyplot(m.plot(forecast))
    st.write(
        """
        In the graph above you can find the expected forecast. All the black dots are data points that have been used to
        calculate the prediction. The darker blue line is the models prediction. This is also calculated for previous 
        days to show the accuracy of the model. The lighter blue "bands" around the prediction line is the expected 
        upper and lower bound.
        """
    )


    st.pyplot(m.plot_components(forecast))
    st.write(
        """
        This model can also give you some intuition on how the stock fluctuates within a year (fig 2.3) or even within a 
        week (fig 2.2). The first graph shows the trend line. This is the same as the in the first graph.
        """
    )

    # st.write(
    #     """
    #     want to know what the model predicts on a specific date? Select the date below and find out!
    #     """
    # )
    # date = st.date_input("select date")
    # forecast = m.predict(future)
    # st.write(f"The predicted value of stock {session_state['mrkt_val']} on {date} is: {forecast}")




    st.write(
        """
        Are you satisfied with the results? \n
        If you want to change some answers on a specific topic you can just go to the topic, hit save and return to the Results page to see the new results. \n
        Or if you want to retry from the start, hit the \"Try again\" button below!
        """
    )
    if st.button("Try again"):
        caching.clear_cache()