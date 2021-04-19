import streamlit as st 
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

def app():
    header = st.beta_container()
    image = st.beta_container()

    with header:
        st.title('Books That Everyone Should Read At Least Once\n')     
        st.text('')
        st.text('')
        st.text('')
        st.text('')
        st.title('⚜️ About ⚜️:')
        st.markdown('''
    
    Books are disponible for everyone, rich and poor, young and old. 
    From love stroies to Sci Fi, it's gonna change the world for 
    everyone. How will your life be affected ?📖
    
   ⬇️⬇️ This Project was created by 4 ***[Strive School](https://strive.school/)*** Students.⬇️⬇️
    ''')
    
        st.markdown('## Get to know us 👋🏻:')

    
        if st.button('Click here'):
            st.markdown("![Hello There](https://media2.giphy.com/media/3ornk57KwDXf81rjWM/200w.webp?cid=ecf05e47chobelyn3nvbi5od5v1l7ahhd8t9uy1irct4rqiq&rid=200w.webp&ct=g)")
            st.write('***The Developer Team***:')
            st.write('• Sven Skyth Henriksen: [GitHub ](https://github.com/Sven-Skyth-Henriksen)&[ LinkedIn](https://www.linkedin.com/in/sven-skyth-henriksen-4857bb1a2/)')
            st.write('• Madina Zhenisbek: [GitHub ](https://github.com/madinach)&[ LinkedIn](https://www.linkedin.com/in/madina-zhenisbek/)')
            st.write('• Olatunde Salami: [GitHub ](https://github.com/salamituns)&[ LinkedIn](https://www.linkedin.com/in/olatunde-salami/)')
            st.write('• Paramveer Singh: [GitHub ](https://github.com/paramveer)&[ LinkedIn](https://www.linkedin.com/in/paramveer-singh07/)')

        
    with image:
        image = Image.open('book.jpeg')
        st.image(image, caption='Quote by ERNEST HEMINGWAY')

app()



st.subheader('Number of Ratings by users vs Average Ratings')
fig = px.scatter(df, x=df["min_max"].values, y=df["num_ratings"], hover_name=df["title"],size=df['num_pages']*10000, 
hover_data=['num_pages','author'],labels={
                    "x":"Average Ratings",
                    "num_ratings":"Number of Ratings",
                    
                },color=df["author"])

#fig.update_traces(marker=dict(size=df['num_pages']/15))
fig.update_xaxes(showgrid=False)
fig.update_yaxes(showgrid=False )
fig.update(layout_showlegend=False)
fig.update_layout(plot_bgcolor="black", height= 600,width=1000,title_text='Number of Ratings in comparison to the Number of Ratings')

st.plotly_chart(fig)
