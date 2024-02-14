import streamlit as st
import pandas as pd
import seaborn as sns

st.title("_This_ is our first website")

st.write("This site is beautiful")

peng_df = sns.load_dataset('penguins')

with st.expander('Show me the penguins'):

    st.dataframe(peng_df)

option = st.selectbox('Which penguin do you want?', 
                      ('Adelie','Chinstrap','Gentoo'))

col1, col2, col3 = st.columns(3)

if option == 'Adelie':
    with col2:
       st.header("Adelie")
       st.image('Images/Adelie.png')

if option == 'Chinstrap':
    with col2:
       st.header("Chinstrap")
       st.image('Images/Chinstrap.png')

if option == 'Gentoo':
    with col2:
       st.header("Gentoo")
       st.image('Images/Gentoo.png')
