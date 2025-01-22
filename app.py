import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt

# Set page configuration for wide layout
st.set_page_config(page_title="Iphone Sales Analysis", layout="wide")

st.markdown("""
<style>
button:hover {
    background-color:rgb(49, 99, 149); /* Darker green on hover */
    
}
</style>
""", unsafe_allow_html=True)


def home_page():
   
    # Add a centered heading and description
    st.markdown(
        """
        <div style='text-align:center;'>
            <h1 style='font-size:10vh; color:orange;'>Welcome to analysis of iPhone sales data</h1>
            <h2 style='font-size:40px; color:#1E90FF;'>We are here providing sales of iPhone in various countries in 2025</h2>
            <p style='font-size:30px; color:gray;'>Here are the countries you can explore:</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Create four columns for the cards
    col1, col2, col3, col4 = st.columns(4)

    # Card 1
    with col1:
        st.markdown(
            """
            <div style="background-color:#1E90FF; color:white; padding:20px; border-radius:10px; text-align:center;">
                <h3>USA</h3>
                <p>Explore iPhone sales in the USA.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("View USA"):
            st.session_state.page = "usa"

    # Card 2
    with col2:
        st.markdown(
            """
            <div style="background-color:#32CD32; color:white; padding:20px; border-radius:10px; text-align:center;">
                <h3>India</h3>
                <p>Explore iPhone sales in India.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("View India"):
            st.session_state.page = "india"

    # Card 3
    with col3:
        st.markdown(
            """
            <div style="background-color:#FFD700; color:black; padding:20px; border-radius:10px; text-align:center;">
                <h3>Africa</h3>
                <p>Explore iPhone sales in the Africa.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("View Africa"):
            st.session_state.page = "africa"

    # Card 4
    with col4:
        st.markdown(
            """
            <div style="background-color:#FF6347; color:white; padding:20px; border-radius:10px; text-align:center;">
                <h3>China</h3>
                <p>Explore iPhone sales in China.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("View China"):
            st.session_state.page = "china"

       # Add some spacing between the rows
    st.markdown("<br>", unsafe_allow_html=True)

    # Second row of cards
    col5, col6, col7, col8 = st.columns(4)

    # Card 5
    with col5:
        st.markdown(
            """
            <div style="background-color:#FF4500; color:white; padding:20px; border-radius:10px; text-align:center;">
                <h3>Japan</h3>
                <p>Explore iPhone sales in Japan.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("View Japan"):
            st.session_state.page = "japan"

    # Card 6
    with col6:
        st.markdown(
            """
            <div style="background-color:#9400D3; color:white; padding:20px; border-radius:10px; text-align:center;">
                <h3>U.A.E</h3>
                <p>Explore iPhone sales in U.A.E.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("View U.A.E"):
            st.session_state.page = "dubai"

    # Card 7
    with col7:
        st.markdown(
            """
            <div style="background-color:#00CED1; color:white; padding:20px; border-radius:10px; text-align:center;">
                <h3>Australia</h3>
                <p>Explore iPhone sales in Australia.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("View Australia"):
            st.session_state.page = "australia"

    # Card 8
    with col8:
        st.markdown(
            """
            <div style="background-color:#8B0000; color:white; padding:20px; border-radius:10px; text-align:center;">
                <h3>France</h3>
                <p>Explore iPhone sales in France.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("View France"):
            st.session_state.page = "france"
    st.markdown("<br>", unsafe_allow_html=True)

    # Second row of cards
    col9 =st.columns(4)[0]

    # Card 9
    with col9:
        st.markdown(
            """
            <div style="background-color:#4682B4; color:white; padding:20px; border-radius:10px; text-align:center;">
                <h3>NewZealand</h3>
                <p>Explore iPhone sales in NewZealand.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("View NewZealand"):
            st.session_state.page = "newZealand"
        
   
   # Add more spacing
    st.markdown("<br><br>", unsafe_allow_html=True)

    # Comparison Section
    st.markdown(
        """
        <div style='text-align:center;'>
            <h2 style='font-size:50px; color:#4CAF50;'>Compare Sales Between Two Countries</h2>
            <p style='font-size:20px; color:gray;'>Select two countries below to compare their iPhone sales data.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Country selection for comparison
    countries = ["INDIA", "America", "Africa", "China", "Japan", "U.A.E", "France", "Australia", "NewZealand"]
    country_1=""
    country_2=""
    top_10_data1=""
    top_10_data2=""
    col10, col11 = st.columns(2)
    with col10:
        country_1 = st.selectbox("Select First Country:", countries)
    with col11:
        country_2 = st.selectbox("Select Second Country:", countries)


    # Display comparison
    if country_1 and country_2:
        try:
            salesdata = pd.read_csv("data.csv")
        except FileNotFoundError:
            st.error("File `data.csv` not found. Please upload the correct file.")
            return

        # Filter data for selected countries
        filtereddata_1 = salesdata[salesdata["country"] == country_1]
        filtereddata_2 = salesdata[salesdata["country"] == country_2]

        if filtereddata_1.empty or filtereddata_2.empty:
            st.warning("Sales data for one or both countries is not available.")
        else:
            top_10_data1 = filtereddata_1.nlargest(10, "selled")
            top_10_data2 = filtereddata_2.nlargest(10, "selled")

        col12, col13 = st.columns(2)

        with col12:
            st.markdown(f"## Top 10 Most Selled Iphones in {country_1}")

            product_c1 = top_10_data1["Product Name"].values
            sales_c1 = top_10_data1["selled"].values
            explode = [0.1] * len(sales_c1)
            colors = plt.cm.tab10.colors

            # Create pie chart for the first country
            fig, ax = plt.subplots(figsize=(6, 6))  # Ensure consistent size
            fig.patch.set_facecolor("black")  # Set background to black
            ax.set_facecolor("black")  # Ensure inner axes also have a black background
            ax.pie(
                sales_c1,
                explode=explode,
                labels=product_c1,
                autopct="%1.1f%%",
                startangle=140,
                colors=colors,
                wedgeprops={"edgecolor": "white", "linewidth": 1},  # Adjusted for black background
                textprops={"color": "white"}, # Set text color to white
                radius=1.0,  # Fix the radius for consistent size
            )
            ax.axis("equal")
            ax.set_title(f"Sales Distribution in {country_1}", color="white")  # White text for contrast
            st.pyplot(fig)

        with col13:
            st.markdown(f"## Top 10 Most Selled Iphones in {country_2}")

            product_c2 = top_10_data2["Product Name"].values
            sales_c2 = top_10_data2["selled"].values
            explode = [0.1] * len(sales_c2)
            colors = plt.cm.tab20.colors

            # Create pie chart for the second country
            fig, ax = plt.subplots(figsize=(6, 6))  # Ensure consistent size
            fig.patch.set_facecolor("black")  # Set background to black
            ax.set_facecolor("black")  # Ensure inner axes also have a black background
            ax.pie(
                sales_c2,
                explode=explode,
                labels=product_c2,
                autopct="%1.1f%%",
                startangle=140,
                colors=colors,
                wedgeprops={"edgecolor": "white", "linewidth": 1},  # Adjusted for black background
                textprops={"color": "white"},  # Set text color to white
                radius=1.0,  # Fix the radius for consistent size
            )
            ax.axis("equal")
            ax.set_title(f"Sales Distribution in {country_2}", color="white")  # White text for contrast
            st.pyplot(fig)
            
        st.markdown("<br><br>", unsafe_allow_html=True)
        
        # Comparison of All Countries Section
        st.markdown(
            """
            <div style='text-align:center;'>
                <h2 style='font-size:50px; color:#FF6347;'>All Countries total sales</h2>
            </div>
            """,
            unsafe_allow_html=True
        )
        # Ensure the necessary columns are present
        if not {"country", "selled", "Sale Price"}.issubset(salesdata.columns):
            st.error("The file must contain 'country', 'selled', and 'Sale Price' columns.")
        else:
            # Add a new column for total sales per product
            salesdata["total_sales"] = salesdata["selled"] * salesdata["Sale Price"]

            # Group by country and calculate total sales
            country_sales = salesdata.groupby("country")["total_sales"].sum().reset_index()

            # Convert to arrays
            countries = country_sales["country"].values  # Array of country names
            sales_amount = country_sales["total_sales"].values  # Array of total sales amounts

            # Optional: Display a bar chart for visualization
            st.subheader("Sales Distribution by Country in Indian Currency")
            chart = alt.Chart(country_sales).mark_bar(color="orange").encode(
                x="country:O",
                y="total_sales:Q",
                tooltip=["country", "total_sales"]
            ).properties(
                width=600,
                height=400
            )

            # Render the chart in Streamlit
            st.altair_chart(chart, use_container_width=True)
        

# Function to render the USA page
def usa_page():
    country="America"
    country_page(country)

# Function to render the India page
def india_page():
    country="INDIA"
    country_page(country)

# Function to render the UK page
def africa_page():
    country="Africa"
    country_page(country)
    

# Function to render the Canada page
def china_page():
    country="China"
    country_page(country)
    

def dubai_page():
    country="U.A.E"
    country_page(country)
    
    

# Function to render the India page
def japan_page():
    country="Japan"
    country_page(country)
  
    

# Function to render the UK page
def australia_page():
    country="Australia"
    country_page(country)
    
    

# Function to render the Canada page
def france_page():
    country="France"
    country_page(country)
    
    

# Function to render the Canada page
def newZealand_page():
    country="NewZealand"
    country_page(country)
   
   
# Define a function to display the country-specific page
def country_page(country):
    selected_country = country

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
                <a href="https://www.google.com/search?q={model_1}+review" target="_blank" style="color:yellow;">Product Url</a>
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
                <a href="https://www.google.com/search?q={model_2}+review" target="_blank" style="color:yellow;">Product Url</a>
            </div>
            """,
            unsafe_allow_html=True
        )
        
    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("Back to Home"):
        st.session_state.page = "home"

# Initialize session state for page tracking
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Render the appropriate page based on session state
if st.session_state.page == 'home':
    home_page()
elif st.session_state.page == 'usa':
    usa_page()
elif st.session_state.page == 'india':
    india_page()
elif st.session_state.page == 'africa':
    africa_page()
elif st.session_state.page == 'china':
    china_page()
elif st.session_state.page == 'japan':
    japan_page()
elif st.session_state.page == 'dubai':
    dubai_page()
elif st.session_state.page == 'france':
    france_page()
elif st.session_state.page == 'australia':
    australia_page()
elif st.session_state.page == 'newZealand':
    newZealand_page()