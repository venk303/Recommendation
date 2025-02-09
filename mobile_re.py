import streamlit as st
import pandas as pd
import numpy as np
import pickle

data = pd.read_csv('C:\\venkat\\genai\\GENAI_JAN\\GenAI1\\mlprojects\\offers\\mobile_recommendation_system_dataset.csv')

similarity = pickle.load(open("similarity.pkl", "rb"))

def recommend(mobile):
    try:
        mobile_index = data[data['name']==mobile].index[0]
        similarity_array = similarity[mobile_index]
        similar_10_mobiles = sorted(list(enumerate(similarity_array)),reverse=True,key=lambda x:x[1])[1:11]
        recommendations =  [data['name'].iloc[i[0]] for i in similar_10_mobiles]
        return recommendations
    except IndexError:
        return ["No recommendations found!"]

st.title("Mobile Recommendation System")
st.write("-----------------------------")

select_mobile = st.selectbox("select mobile type", data['name'].values)

if st.button("recommend"):
    recommendations = recommend(select_mobile)
    st.subheader("* recommended mobiles *")
    #print(*** recommendations ***)
    for mobile in recommendations:
        st.write(f"✅ {mobile}")
        