import streamlit as st
import numpy as np
import plotly.figure_factory as ff
import pandas as pd
import plotly_express as px
from generateMap import get_graph

st.markdown("<h1 style='text-align: center; color: black;'>Our Dying Rainforest</h1>", unsafe_allow_html=True)

df = pd.read_csv('PredictFutureRainforest.csv')


st.subheader("An Alarming Future")
df.columns = ["Years", "Acre", "Amazonas", "Amapá", "Maranhão", "Mato Grosso", "Pará", "Rondônia", "Roraima", "Tocantins", "All", "Past/Future"]
x_axis_val = st.selectbox('Select State',  options = list(df.columns)[1:-2])
print("x_axis_val",x_axis_val)
plot = px.line(
    df, x="Years", 
    y=x_axis_val,
    labels={
        x_axis_val:"Deforested Area (km^2)"
    },
    title = f"{x_axis_val}'s Deforested Area through the years",
    color = "Past/Future"
    )
st.plotly_chart(plot)

st.write("""The Amazon Rainforest, one of the world's most important ecosystems, has been losing trees at an alarming rate over the past few years.  Deforestation in the Amazon is a major concern as it not only destroys the habitat of countless species, but it also contributes to climate change. In fact, it has been estimated that in the next 10 years, a quarter of
the Amazon will be destroyed if we do not take immediate action. This data is alarming and shows that the forest will only keep dying if we do not act now. It is crucial that we take urgent steps to stop
deforestation and promote reforestation in the region. The Amazon Rainforest is an irreplaceable natural treasure that needs to be protected for the sake of our planet's future.""")

st.subheader("Deforestation in the Past")

year = st.slider("Years",2004, 2019)

st.plotly_chart(get_graph(year)) 


st.write("""The Amazon Rainforest has been dying at an alarming rate over the last 15 years. What started as a loss of only a few thousand square kilometers per year has now skyrocketed to the loss of hundreds of thousands of trees each year. 
The data shows a horrifying increase in trees lost in this critical ecosystem, which not only supports numerous species but also plays a vital role in regulating the planet's climate. 
The loss of the Amazon Rainforest is having severe consequences for the entire planet, from the destruction of critical habitats to the exacerbation of climate change. 
We must take action to address this crisis and work to stop deforestation, restore damaged areas, and promote sustainable land use practices in the region. 
The continued loss of the Amazon Rainforest is not only devastating for the region but for the entire planet.""")
st.subheader("How you can help")
with st.expander("Amazon Watch"):
    st.write("""
        Amazon Watch is a nonprofit organization that works to protect the Amazon rainforest, 
        defend the rights of indigenous people who call it their home, and address the root causes of climate change. 
        They partner with indigenous communities and grassroots organizations to protect the rainforest and promote sustainable development. 
        You can donate to Amazon Watch or learn more about their work on their website: https://amazonwatch.org/

    """)
with st.expander("Rainforest Foundation US"):
    st.write("""
        The Rainforest Foundation US is a nonprofit organization that works to protect the rainforest and its indigenous people. 
        They support grassroots organizations in Brazil, Peru, and other countries in the Amazon basin by providing funding, training, 
        and advocacy support. Their work includes protecting indigenous land rights, promoting sustainable land use practices, 
        and supporting indigenous-led conservation efforts. You can donate to the Rainforest Foundation US or learn more about their work on their website:
          https://rainforestfoundation.org/
    """)
with st.expander("Rainforest Trust"):
    st.write("""
       Rainforest Trust is a nonprofit organization that works to protect threatened tropical forests and endangered wildlife. 
       They partner with local conservation organizations and communities to purchase and protect land in the Amazon and other regions.
        Their work includes protecting biodiversity, supporting sustainable development, and mitigating climate change. 
        You can donate to Rainforest Trust or learn more about their work on their website: 
       https://www.rainforesttrust.org/
    """)
with st.expander("World Wildlife Fund (WWF)"):
    st.write("""
       The WWF is a global conservation organization that works to protect the environment and wildlife around the world. 
       They have a specific program focused on the Amazon rainforest, where they work with local communities and partner organizations 
       to protect biodiversity, promote sustainable land use practices, and address the impacts of climate change.
        You can donate to WWF or learn more about their work on their website: 
       https://www.worldwildlife.org/places/amazon
    """)
