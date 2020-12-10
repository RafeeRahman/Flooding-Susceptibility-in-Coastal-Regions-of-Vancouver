"""
Display the map which shows the susceptible flooding regions - includes interactive features
Here we will interpret the data with our own logic/calculations
MAP DATA FROM
https://simplemaps.com/data/canada-cities
"""
import python_ta
from python_ta import contracts
import plotly.express as px
import plotly.graph_objects as go  # or plotly.express as px

import pandas as pd
from typing import Any
from canada_dsm import *

map = pd.read_csv('vancouver.csv')


def display_map(data: Any) -> go.Figure():
    """Displays the map of the given data
    """
    # Main point
    fig = px.scatter_mapbox(data, lat="lat", lon="lng",
                            color_discrete_sequence=["fuchsia"], zoom=3)
    # Flood risk points DUMMY VALUES CURRENTLY
    fig.add_trace(
        go.Scattermapbox(
            lat=['49.4', '49.5', '49.6'],
            lon=['-122.5', '-122.6', '-122.8'],
            mode='markers',
            marker=go.scattermapbox.Marker(
                color='rgb(0, 0, 255)',
                size=12,
                colorscale='teal',
                showscale=True,
                cmax=200,
                cmin=0
            ),
            text=['Flood Risk'],
        )
    )
    fig.update_layout(mapbox_style="open-street-map",
                      mapbox={'center': go.layout.mapbox.Center(lat=data['lat'][0], lon=data['lng'][0]), 'zoom': 10})
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

    return fig


if __name__ == '__main__':
    python_ta.check_all(config={
        'extra-imports': [],  # the names (strs) of imported modules
        'allowed-io': [],  # the names (strs) of functions that call print/open/input
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']

    })
    python_ta.contracts.check_all_contracts()
