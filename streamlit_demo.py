import streamlit as st
import datetime
import SessionState
from cache import cached_dict






def main():
    # make a title for your webapp
    st.title("An Input Form")
    session_state = cached_dict()

    loc = ""
    if "location" in session_state:
        loc = session_state["location"]

    # lets try a both a text input and area as well as a date
    field_1 = st.text_input('Your Name')
    field_2 = st.text_area("Your address", loc)

    start_date = datetime.date(1990, 7, 6)
    date = st.date_input('Your birthday', start_date)

    if date != start_date:
        print(field_1)
        print(field_2)
        print(date)
        session_state["location"] = field_2


if __name__ == "__main__":
    main()

