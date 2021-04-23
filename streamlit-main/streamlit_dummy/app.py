
import streamlit as st
from multiapp import MultiApp
from apps import about, data, models, home # import your app modules here

app = MultiApp()

st.title(' Dooku Welcomes you to the DARK SIDE')
st.text('')
st.text('')
st.text('')
st.markdown("![Alt Text](https://media4.giphy.com/media/lKYMj63WqlBcc/giphy.gif?cid=ecf05e470d15qsjwvus5fhfgb3l2hpf5js7gqr26lshesrpe&rid=giphy.gif&ct=g)")



st.markdown('''
# Project Baby Yoda

Please select a page:

''')

# Add all your application here
app.add_app('Home',info.app)
app.add_app("About", intro.app)
#app.add_app("Data", data.app)
#app.add_app('Models', models.app)



# The main app
app.run()

