import streamlit as st
import altair as alt
import pandas as pd
import numpy as np

# def visualize_data(df, x_axis, y_axis):
#     pass
def visualize_data(df, x_axis, y_axis):
    chart = alt.Chart(df).mark_circle().encode(
        x=x_axis,
        y=y_axis,
        tooltip=[x_axis, y_axis]
    ).interactive()

    st.altair_chart(chart, use_container_width=True)

def load_data():
    file_path = "metrics.csv"
    df = pd.read_csv(file_path)
    return df

def main():
    df = load_data()
    # df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))
    page = st.sidebar.selectbox("Choose a page", ["Homepage", "Exploration"])
    
    if page == "Homepage":
        st.header("This is your data explorer.")
        st.write("Please select a page on the left.")
        st.write(df)
    elif page == "Exploration":
        st.title("Data Exploration")
        x_axis = st.selectbox("Choose a variable for the x-axis", df.columns, index=3)
        y_axis = st.selectbox("Choose a variable for the y-axis", df.columns, index=4)
        visualize_data(df, x_axis, y_axis)

main()