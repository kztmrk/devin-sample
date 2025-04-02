import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from streamlit_app.utils.data_utils import load_sample_data

st.set_page_config(
    page_title="Streamlit Python Application",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Streamlit Python Application")
st.markdown("""
This is a sample Streamlit application demonstrating various features and capabilities.
Use the sidebar to navigate between different sections of the application.
""")

st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Select a page:",
    ["Home", "Data Visualization", "Interactive Analysis", "About"]
)

if page == "Home":
    st.header("Welcome to the Streamlit Python Application")
    
    st.subheader("Features")
    st.markdown("""
    - Data visualization with Matplotlib and Plotly
    - Interactive data analysis
    - Sample data exploration
    - Customizable parameters
    """)
    
    if st.button("Generate Random Data"):
        data = np.random.randn(100, 2)
        df = pd.DataFrame(data, columns=["x", "y"])
        st.dataframe(df)
        
        fig, ax = plt.subplots()
        ax.scatter(df["x"], df["y"])
        ax.set_title("Random Data Scatter Plot")
        st.pyplot(fig)

elif page == "Data Visualization":
    st.header("Data Visualization")
    
    st.subheader("Sample Chart")
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=["A", "B", "C"]
    )
    
    chart_type = st.selectbox(
        "Select chart type:",
        ["Line Chart", "Bar Chart", "Area Chart"]
    )
    
    if chart_type == "Line Chart":
        st.line_chart(chart_data)
    elif chart_type == "Bar Chart":
        st.bar_chart(chart_data)
    else:
        st.area_chart(chart_data)
    
    st.subheader("Interactive Plotly Chart")
    df = pd.DataFrame({
        "Category": ["A", "B", "C", "D", "E"] * 4,
        "Group": ["Group 1"] * 5 + ["Group 2"] * 5 + ["Group 3"] * 5 + ["Group 4"] * 5,
        "Value": np.random.randn(20) * 10 + 50
    })
    
    fig = px.bar(
        df, 
        x="Category", 
        y="Value", 
        color="Group",
        barmode="group",
        title="Sample Grouped Bar Chart"
    )
    st.plotly_chart(fig, use_container_width=True)

elif page == "Interactive Analysis":
    st.header("Interactive Analysis")
    
    st.subheader("Parameter Selection")
    
    col1, col2 = st.columns(2)
    
    with col1:
        param1 = st.slider("Parameter 1", 0, 100, 50)
        param2 = st.slider("Parameter 2", 0.0, 1.0, 0.5)
    
    with col2:
        option = st.selectbox(
            "Choose an option",
            ["Option A", "Option B", "Option C"]
        )
        
        color = st.color_picker("Pick a color", "#00f900")
    
    st.subheader("Results")
    st.write(f"Parameter 1: {param1}")
    st.write(f"Parameter 2: {param2}")
    st.write(f"Selected option: {option}")
    st.write(f"Selected color: {color}")
    
    result = param1 * param2
    st.metric(label="Calculated Result", value=f"{result:.2f}")
    
    st.subheader("Processing")
    progress_bar = st.progress(0)
    for i in range(100):
        progress_bar.progress(i + 1)
    
    st.success("Processing complete!")

elif page == "About":
    st.header("About This Application")
    
    st.markdown("""
    This is a sample Streamlit application created as a template for Python projects.
    
    - Streamlit
    - Pandas
    - NumPy
    - Matplotlib
    - Plotly
    
    The application follows a modular structure with separate components for different functionalities.
    
    For more information, please contact the project maintainer.
    """)

st.sidebar.markdown("---")
st.sidebar.info(
    "This is a sample Streamlit application. "
    "Customize it according to your project requirements."
)
