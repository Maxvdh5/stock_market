"""This page is for searching and viewing the list of awesome resources"""
import datetime
import streamlit as st
from src.utils import cache
import holidays
import yfinance as yf


def write():
    # make a title for your webapp
    session_state = cache()
    st.title("settings")
    st.write(
        """
        choose a stock to predict\n
        """
    )
    set_stock = True
    if "mrkt" in session_state:
        stock = st.text_input("", value=session_state["mrkt_val"])
    else:
        stock = st.text_input("", value="ASML")
    try:
        mrkt = yf.Ticker(stock)
        _ = mrkt.get_splits()
        session_state["mrkt"] = mrkt
        session_state["mrkt_val"] = stock
    except:
        set_stock = False
        st.warning(
            "stock cannot be found"
        )

    st.write(
        """
        choose a country where us want to use the holidays from\n
        """
    )
    set_holiday = True

    if "hol" in session_state:
        hd = st.text_input("", value=session_state['hol_val'])
    else:
        hd = st.text_input("", value='Netherlands')

    try:
        session_state["hol_val"] = hd
    except:
        set_holiday = False
        st.warning(
            "country cannot be found"
        )

    st.write(
        """
        Choosing the right start and end date is very important. For predictions over longer periods of time it is
        preferable to use longer time ranges. This way the predictions are more generalized. When predicting for shorter
        periods shorter time ranges should be chosen in order to fit the current climate more precise.
        """
    )
    if "begin" in session_state:
        begin = st.date_input('start date', value=session_state["begin"])
    else:
        begin = st.date_input('start date', value=datetime.date(2010,1 , 1))
    session_state["begin"] = begin

    if "end" in session_state:
        end = st.date_input('end date', value=session_state['end'])
    else:
        end = st.date_input('end date')
    session_state["end"] = end

    if "days" in session_state:
        days = st.number_input("days to predict", value=session_state["days"], step=1)
    else:
        days = st.number_input("days to predict", value=150, step=1)
    session_state["days"] = days

    if st.button("save"):
        if set_holiday and set_stock:
            session_state['is_done'].add('Settings')


if __name__ == "__main__":
    write()