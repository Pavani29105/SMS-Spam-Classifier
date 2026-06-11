import streamlit as st
import pickle

st.set_page_config(page_title="SMS Spam Classifier")
st.title("📩 SMS Spam Classifier")
st.write("Enter an SMS message to check whether it is Spam or Ham.")

tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

input_sms = st.text_area("Enter SMS Message")

if st.button("Predict"):
    vector = tfidf.transform([input_sms])
    result = model.predict(vector)

    if result[0] == 1:
        st.error("Spam")
    else:
        st.success("Ham")