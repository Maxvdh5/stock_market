import streamlit as st
import awesome_streamlit as ast
import datetime
from src.utils import cache
from copy import deepcopy

import src.pages.home
import src.pages.settings
import src.pages.result

PAGES = {
    "Home": src.pages.home,
    "Settings": src.pages.settings,
    "Result": src.pages.result
}

def is_done(page):
    if page in cache()['is_done']:
        page = page + ' ✓'
    return page

def check_done(pages):
    if 'Result' in pages:
        pages.remove('Result')

    for page in pages:
        if page not in cache()['is_done']:
            return pages
    pages = deepcopy(cache()['is_done'])
    pages.add('Result')
    return pages

def main():
    """Main function of the App"""
    st.sidebar.title("Navigation")
    pgs = list(PAGES.keys())
    pgs = check_done(pgs)
    selection = st.sidebar.radio("Go to", [is_done(p) for p in pgs])

    page = PAGES[selection.strip(' ✓')]

    with st.spinner(f"Loading {selection} ..."):
        ast.shared.components.write_page(page)

    st.sidebar.warning(
        """
        if after saving the settings results does not show up please click on "home" the Results page should pop up!
        """
    )
    st.sidebar.title("Warning")
    st.sidebar.info(
        "This project has been made by a student for training purposes "
    )
    st.sidebar.title("About")
    st.sidebar.info(
        """
       This app is made by Max van den Heijkant
"""
    )


if __name__ == "__main__":
    main()