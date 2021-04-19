import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st
import plotly.express as px 

def load_data(filename):
    df = pd.read_csv(filename, index_col=0)
    return df

def summary_poster(df):
    #MAKE SUBPLOTS
    #fig = make_subplots(
    #    rows=2, cols=2, 
    #    column_widths=[0.4, 0.6],
     #   specs=[[{"type": "bar"}, {"type": "scatter"}],
     #       [ {"type":"scatter", "colspan": 2}, None]],
    #        subplot_titles=('#Awards for Author', 
     #                       'Overall Average Ratings for the Author', 
     #                       '#Books Featured by an Author'),
     #       vertical_spacing=0.1, horizontal_spacing= 0.09)

 #STACKED BAR
    authors_df= pd.DataFrame(df.groupby(['author'])['award_number'].count())
    fig= go.Bar(x = authors_df.index, 
                                y = authors_df.award_number,
                                #name = label_name,
                                #hovertemplate='<b>Year: %{x}</b><br>#Songs: %{y}',
                                #marker_color = pd.Series([label_name]*len(x)).map(color_dict),
                                legendgroup = 'grp2',
                                #showlegend=True),
                                )
                                




    return fig 