import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt

# Define a function to display the home page
def home_page():
    # Page configuration
    st.set_page_config(page_title="iPhone Sales Analysis Dashboard", layout="wide")
    st.markdown(
        """
        <div style='text-align:center;'>
            <h1 style='font-size:10vh; color:orange;'>Welcome to analysis of iPhone sales data</h1>
            <h2 style='font-size:40px; color:#1E90FF;'>We are here providing sales of iPhone in various countries in 2025</h2>
        </div>
        """,
        unsafe_allow_html=True
    )
    # Country selection for detailed analysis
    countries = ["USA", "INDIA", "UK", "Canada", "Germany", "Japan", "Australia", "China", "Brazil"]
    selected_country = st.selectbox("Select a country to explore:", countries)

    if selected_country:
        if st.button("Go to Country Page"):
            st.session_state.page = "country"
            st.session_state.selected_country = selected_country

# Define a function to display the country-specific page
def country_page():
    selected_country = st.session_state.get("selected_country", "Unknown Country")

    # Heading for the country page
    st.markdown(
        f"""
        <div style='text-align:center;'>
            <h1 style='font-size:10vh; color:orange;'>iPhone Sales in {selected_country}</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Load sales data
    try:
        salesdata = pd.read_csv("data.csv")
    except FileNotFoundError:
        st.error("File `data.csv` not found. Please upload the correct file.")
        return

    # Filter data for the selected country
    country_data = salesdata[salesdata["country"] == selected_country]

    if country_data.empty:
        st.warning(f"No sales data available for {selected_country}.")
        return

    # Calculate metrics
    total_sales = (country_data["selled"] * country_data["Sale Price"]).sum()
    total_products_sold = country_data["selled"].sum()
    most_sold_iphone = country_data.loc[country_data["selled"].idxmax()]["Product Name"]

    # Display metrics in cards
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Sales", f"${total_sales:,.2f}")
    col2.metric("Total Products Sold", f"{total_products_sold}")
    col3.metric("Most Sold iPhone", most_sold_iphone)

    # Comparison section
    st.markdown(
        """
        <div style='text-align:center; margin-top: 50px;'>
            <h2 style='font-size:50px; color:#4CAF50;'>Comparison Between Top Two iPhone Models</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Find the top two most sold iPhone models
    top_two = country_data.nlargest(2, "selled")

    if len(top_two) < 2:
        st.warning("Not enough data for comparison.")
        return

    model_1, model_2 = top_two["Product Name"].values
    sales_1, sales_2 = top_two["selled"].values
    price_1, price_2 = top_two["Sale Price"].values

    col4, col5 = st.columns(2)

    with col4:
        st.markdown(
            f"""
            <div style="background-color:#1E90FF; color:white; padding:20px; border-radius:10px; text-align:center;">
                <h3>{model_1}</h3>
                <p>Sales Amount: ${sales_1 * price_1:,.2f}</p>
                <a href="https://www.google.com/search?q={model_1}+review" target="_blank" style="color:yellow;">Read Reviews</a>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col5:
        st.markdown(
            f"""
            <div style="background-color:#32CD32; color:white; padding:20px; border-radius:10px; text-align:center;">
                <h3>{model_2}</h3>
                <p>Sales Amount: ${sales_2 * price_2:,.2f}</p>
                <a href="https://www.google.com/search?q={model_2}+review" target="_blank" style="color:yellow;">Read Reviews</a>
            </div>
            """,
            unsafe_allow_html=True
        )

# Initialize session state for page navigation
if "page" not in st.session_state:
    st.session_state.page = "home"

# Render the appropriate page based on the session state
if st.session_state.page == "home":
    home_page()
elif st.session_state.page == "country":
    country_page()
