import streamlit as st
import pandas as pd
from PIL import Image
import plotly.express as px 
from Helper import load_data
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df =load_data("Books_universe.csv")


st.set_page_config(page_title="Unleash your Curiosity", 
                 
                   layout='wide')


#Sidebar - Author selection
#authors = df.groupby(['author'])#['min_max'].mean()

#sorted_authors = sorted(df['author'].unique()) 
#st.markdown("### **Select Author:**")

#select_author= []
#select_author.append(st.selectbox('',sorted_authors))

#Filtering Data
#dft= df[(df.author.isin(select_author))]

def summary_poster(df):
    fig = make_subplots(
        rows=2, cols=2, 
        column_widths=[200,2],
        specs=[[{"type": "bar"}, {"type": "bar"}],
            [ {"type":"scatter", "colspan": 1}, None]],
            subplot_titles=('Most Decorated Authors', )
            #                '#Songs on Billboard Charts across Years', 
            #                'Music Timeline by Billboard Song Rank'),,
            ,vertical_spacing=0.1, horizontal_spacing= 0.09)
    authors = df.groupby(['author'])['award_number'].count()
    authors =pd.DataFrame(authors)
    authors = authors.sort_values(by=['award_number'],ascending=False)[0:50]
    
    fig.add_trace(go.Bar(x = authors.index, y = authors.award_number),marker=dict(color='pink',width=3),row = 1, col = 1)

    fig.update_yaxes(title_text = '#Awards', mirror = True, 
                        title_standoff = 0, gridcolor = 'black', gridwidth = 0.01,
                        zeroline = False,
                        row = 1, col = 1)
    fig.update_xaxes(linecolor = 'black', mirror = True, dtick = 1,
                     row = 1, col = 1)

    author_books = df.groupby('author').count()
    author_books =pd.DataFrame(author_books).sort_values(by=['min_max'],ascending=False)[0:50]
    
    fig.add_trace(go.Scatter(
                x=author_books.index,
                y=author_books.title,
                mode = 'markers',
                            
                showlegend=False
                ),
                row = 2, col = 1
                )
    fig.update_traces(marker = dict(symbol = 'circle',size = 12
                                    ,line = dict(color = 'green', width = 0.5)
                                    ),
                      name = "",
                      row = 2, col =1)
    fig.update_yaxes(title = 'Number of Books',showgrid=False, 
                    
                    row = 2, col = 1)
    fig.update_xaxes(title="",showgrid=False, 
                   
                     row = 2, col =1)

    fig.update_layout( # customize font and margins

                        font_family= 'Nunito',#"Helvetica",
                        width=1200,
                        height=1000,
                        template = 'plotly_dark',
                        legend=dict( orientation = 'v',
                                    font=dict(size = 10),
                                    bordercolor = 'LightGrey',
                                    borderwidth=0.5),
                        )
                    


    return fig



t = summary_poster(df=df)
st.plotly_chart(t)


