import streamlit as st
import pandas as pd
import seaborn as sns
import pickle
import sklearn

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

my_scaler = pickle.load(open('my_scaler.sav', 'rb'))



bill_length = st.slider('What is the bill lenght?',30,65,40)
bill_depth = st.slider('What is the bill depth?',10,25,15)
flipper_length = st.slider('What is the flipper length?',150,250,200)
body_mass = st.slider('What is the body_mass?',2500,6500,4000)

if st.button("Create a new penguin and scale it"):
    new_peng = pd.DataFrame({'bill_length_mm':[bill_length],'bill_depth_mm':[bill_depth],'flipper_length_mm':[flipper_length],'body_mass_g':[body_mass]})
    st.dataframe(new_peng)
    scaled_peng = my_scaler.transform(new_peng)

    st.dataframe(scaled_peng)