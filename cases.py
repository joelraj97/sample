import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output
app=dash.Dash(__name__)
df=pd.read_csv('covidd.csv')

#app layout

app.layout=html.Div([
    html.H1("The Covid case in Each country"),
    dcc.Dropdown(id='my_option',
                 options=[{'label':i,'value':i}
                          for i in df['Combined_Key'].unique()],
                 value='Afghanistan',

                 ),
    html.H6("Confirmed"),
    html.Div(id='confirmedid'),

    html.Br(),
    html.H6("Recovered"),
    html.Div(id='recoveredid'),
    html.Br(),
    html.H6("Deaths"),
    html.Div(id='deathid'),
    html.Br(),
    dcc.Graph(id='incidentrate',figure={})
])

#app callback

@app.callback(
    [Output(component_id='confirmedid',component_property='children'),
     Output(component_id='recoveredid',component_property='children'),
     Output(component_id='deathid',component_property='children'),
     Output(component_id='incidentrate',component_property='figure')],
    [Input(component_id='my_option',component_property='value')]
)
def update_graph(option_slctd):
    filtered_data=df[df['Combined_Key']==option_slctd]
    print(filtered_data)

    confirmation= filtered_data['Confirmed']

    recovery=filtered_data['Recovered']
    death=filtered_data['Deaths']
    named=['Confirmed','Recovered','Deaths']
    valued=[confirmation,recovery,death]

    fig=px.pie(data_frame=filtered_data,names=named,values=['Confirmed','Recovered','Deaths'],hole=0.3,title="Covid Data associated with it")

    return confirmation,recovery,death,fig

if __name__ == '__main__':
    app.run_server(debug=True)