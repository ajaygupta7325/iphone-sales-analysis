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
                <h3>UK</h3>
                <p>Explore iPhone sales in the UK.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("View UK"):
            st.session_state.page = "uk"

    # Card 4
    with col4:
        st.markdown(
            """
            <div style="background-color:#FF6347; color:white; padding:20px; border-radius:10px; text-align:center;">
                <h3>Canada</h3>
                <p>Explore iPhone sales in Canada.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("View Canada"):
            st.session_state.page = "canada"

       # Add some spacing between the rows
    st.markdown("<br>", unsafe_allow_html=True)

    # Second row of cards
    col5, col6, col7, col8 = st.columns(4)

    # Card 5
    with col5:
        st.markdown(
            """
            <div style="background-color:#FF4500; color:white; padding:20px; border-radius:10px; text-align:center;">
                <h3>Germany</h3>
                <p>Explore iPhone sales in Germany.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("View Germany"):
            st.session_state.page = "germany"

    # Card 6
    with col6:
        st.markdown(
            """
            <div style="background-color:#9400D3; color:white; padding:20px; border-radius:10px; text-align:center;">
                <h3>Japan</h3>
                <p>Explore iPhone sales in Japan.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("View Japan"):
            st.session_state.page = "japan"

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
                <h3>China</h3>
                <p>Explore iPhone sales in China.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("View China"):
            st.session_state.page = "china"
    st.markdown("<br>", unsafe_allow_html=True)

    # Second row of cards
    col9 =st.columns(4)[0]

    # Card 9
    with col9:
        st.markdown(
            """
            <div style="background-color:#4682B4; color:white; padding:20px; border-radius:10px; text-align:center;">
                <h3>Brazil</h3>
                <p>Explore iPhone sales in Brazil.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("View Brazil"):
            st.session_state.page = "brazil"
        
   
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
            st.subheader("Sales Distribution by Country")
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
    st.title("USA Page")
    st.write("Explore iPhone sales in the USA.")
    if st.button("Back to Home"):
        st.session_state.page = "home"

# Function to render the India page
def india_page():
    st.title("India Page")
    st.write("Explore iPhone sales in India.")
    if st.button("Back to Home"):
        st.session_state.page = "home"

# Function to render the UK page
def uk_page():
    st.title("UK Page")
    st.write("Explore iPhone sales in the UK.")
    if st.button("Back to Home"):
        st.session_state.page = "home"

# Function to render the Canada page
def canada_page():
    st.title("Canada Page")
    st.write("Explore iPhone sales in Canada.")
    if st.button("Back to Home"):
        st.session_state.page = "home"

def germany_page():
    st.title("USA Page")
    st.write("Explore iPhone sales in the USA.")
    if st.button("Back to Home"):
        st.session_state.page = "home"

# Function to render the India page
def japan_page():
    st.title("India Page")
    st.write("Explore iPhone sales in India.")
    if st.button("Back to Home"):
        st.session_state.page = "home"

# Function to render the UK page
def australia_page():
    st.title("UK Page")
    st.write("Explore iPhone sales in the UK.")
    if st.button("Back to Home"):
        st.session_state.page = "home"

# Function to render the Canada page
def china_page():
    st.title("Canada Page")
    st.write("Explore iPhone sales in Canada.")
    if st.button("Back to Home"):
        st.session_state.page = "home"

# Function to render the Canada page
def brazil_page():
    st.title("Canada Page")
    st.write("Explore iPhone sales in Canada.")
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
elif st.session_state.page == 'uk':
    uk_page()
elif st.session_state.page == 'canada':
    canada_page()
elif st.session_state.page == 'germany':
    germany_page()
elif st.session_state.page == 'japan':
    japan_page()
elif st.session_state.page == 'australia':
    australia_page()
elif st.session_state.page == 'china':
    china_page()
elif st.session_state.page == 'brazil':
    brazil_page()
