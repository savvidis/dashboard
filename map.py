import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import ipdb

app = dash.Dash()

df = pd.read_csv('poi_map_sample.csv')

df = df[:200]
app.layout = html.Div([
    html.Div(id='text-content'),
    dcc.Graph(id='map',
              figure={
                  'data': [
                      go.Scattermapbox(
                          lat=df[df['Category_Minor'] == i]['lt'],
                          lon=df[df['Category_Minor'] == i]['ln'],
                          # text=df[df['Category_Minor'] == i]['Category_Minor'],
                          marker={
                              'size': 8,
                              'opacity': 0.6,
                          },
                          name=i

                      ) for i in df.Category_Minor.unique()
                  ],
                  'layout': {
                      'autosize': True,
                      'hovermode': 'closest',
                      'mapbox': {
                          'accesstoken': 'pk.eyJ1IjoiY2hyaWRkeXAiLCJhIjoiY2ozcGI1MTZ3MDBpcTJ3cXR4b3owdDQwaCJ9.8jpMunbKjdq1anXwU5gxIw',
                          'bearing': 0,
                          'style': 'dark',
                          'center': {
                              'lat': 37.98,
                              'lon': 23.75
                          },
                          'zoom': 14,
                          'pitch': 0
                      },
                      'legend': {'x': 0, 'y': 1},
                      'showlegend': False,
                      'margin': {'l': 0, 'r': 0, 'b': 0, 't': 0}
                  }
              })
])

# ipdb.set_trace()


# @app.callback(
#     dash.dependencies.Output('text-content', 'children'),
#     [dash.dependencies.Input('map', 'hoverData')])
# def update_text(hoverData):
#     s = df[df['storenum'] == hoverData['points'][0]['customdata']]
#     return html.H3(
#         'The {}, {} {} opened in {}'.format(
#             s.iloc[0]['STRCITY'],
#             s.iloc[0]['STRSTATE'],
#             s.iloc[0]['type_store'],
#             s.iloc[0]['YEAR']
#         )
#     )

app.css.append_css({
    'external_url': 'bWLwgP.css'
})

if __name__ == '__main__':
    app.run_server(debug=True)
