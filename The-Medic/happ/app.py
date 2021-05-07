import streamlit as st
from multiapp import MultiApp
from apps import home, data, model, experiment# import your app modules here

app = MultiApp()

st.markdown("""
# Hippocratia

""")
st.markdown(" ## Inspired by the great Aelius Galen, Hippocratia welcomes you to the future of Medical Science backed by AI")
st.text(' ')
st.markdown('----------------------------------------------- ')
st.text(' ')

st.markdown(' ')
st.markdown('##  With our revolutionary AI technology we will help you save lives!')
st.markdown('----------------------------------------------- ')
st.markdown(' ')


# Add all your application here
app.add_app("HOME", home.app)
app.add_app("Data", data.app)
app.add_app("Model", model.app)
app.add_app("Try it Out", experiment.app)
# The main app
app.run()
