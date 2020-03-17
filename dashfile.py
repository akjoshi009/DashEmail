import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Email Classifier',style={"margin-left":"20px","text-allign":"center"}),
    dcc.Input(
    placeholder='Enter a Subject...',
    type='text',
    value='',
    id='subject',
    style={
                "width": "50%",
                "height": "60px",
                "textAlign": "left",
                "margin": "10px"
            }
    ) ,
    
   dcc.Textarea(
    placeholder='Enter a Body...',
    value='',
    id="body",
    style={'width': '50%',
           "margin": "10px"
           }
)
   ,html.Button('Submit', id='button',
                style={"textAlign": "center",
                       "margin": "10px",
                       'width': '50%'
                       }
                ),
    html.H1(children='',id="output",style={"margin-left":"20px","text-allign":"center"})
   
],style={"margin-left":"30%","margin-top":"10%"})
   

@app.callback(
    Output("output", "children"),
    [Input("subject", "value"), Input("body", "value"),Input(component_id='button', component_property='n_clicks')]
)
def loadtomodel(sub,body,n_clicks):
    if n_clicks is None:
        raise PreventUpdate
    else:
        return geteclass(sub+body)



def geteclass(text):
    #load model from here and predict
    return "Not Spam"

      
   

if __name__ == '__main__':
   app.run_server()
