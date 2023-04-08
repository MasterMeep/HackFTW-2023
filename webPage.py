import streamlit as st
import numpy as np
import plotly.figure_factory as ff
import pandas as pd
import plotly_express as px
from generateMap import get_graph




def func(arg):
    pass

df = pd.read_csv('graphcsv.csv')

df.columns = ["Years", "Acre", "Amazonas", "Amapá", "Maranhão", "Mato Grosso", "Pará", "Rondônia", "Roraima", "Tocantins", "All"]
x_axis_val = st.selectbox('Select State',  options = list(df.columns)[1:-2])
print("x_axis_val",x_axis_val)
plot = px.line(
    df, x="Years", 
    y=x_axis_val,
    labels={
        x_axis_val:"Deforested Area (km^2)"
    },
    title = f"{x_axis_val}'s Deforested Area through the years"
    )
st.plotly_chart(plot)

st.header("Map of deforestation")

#st.ploty_chart(get_graph(year)) 

# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

# Create distplot with custom bin_size
fig = ff.create_distplot(
        df, x_axis_val, bin_size=[.1, .25, .5])

# Plot!
st.plotly_chart(df, use_container_width=True)








st.markdown(":blue[This graph depicts the loss of density in forests that has occured in the amazon.]")

option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

func(option)

st.subheader("Progression of deforestation over time")
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
fig = ff.create_distplot(
        hist_data, group_labels, bin_size=[.1, .25, .5])

# Plot!
st.plotly_chart(fig, use_container_width=True)

st.markdown(":blue[This graph depicts the loss of density in forests that has occured in the amazon.]")


st.subheader("Forest fire map")

x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
fig = ff.create_distplot(
        hist_data, group_labels, bin_size=[.1, .25, .5])

# Plot!
st.plotly_chart(fig, use_container_width=True)

st.markdown(":blue[This graph depicts the loss of density in forests that has occured in the amazon.]")

with st.expander("See explanation"):
    st.write("""
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    """)
    st.image("https://static.streamlit.io/examples/dice.jpg")
