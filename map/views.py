
import os

import folium
import pandas as pd

from django.shortcuts import render
from folium import plugins, raster_layers
import folium
import json

import requests
import pandas as pd
from django.shortcuts import render
import matplotlib.pyplot as plt
import io
import urllib, base64
from .models import AllData
from django_pandas.io import read_frame
# Create your views here.



def index(request):


    url = (
        "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data"
    )
    luna = json.loads(requests.get(f"{url}/vis1.json").text)

    m = folium.Map(location=[33.886917, 9.537499], zoom_start=2, control_scale=True,min_zoom=2, min_lot=-179,max_lot=179, min_lat=-65,max_lat=179, max_bounds=True)
    state_geo = f"geoFiles/Tunisiesecteurs.geojson"
    data=f"geoFiles/ndvidata.csv"
    df = pd.read_csv(data)
    d = df.iloc[578:972]
    print(d.head(5))
    k = d['Data'].plot()


    plugins.Fullscreen().add_to(m)

    m.choropleth(
        geo_data=state_geo,
        data=df,
        columns=['Province','Data_long_term_Average'],
        key_on='feature.properties.gov_name_f',
        fill_color='BuPu',#OrRd#BuPu#YlOrRd
        fill_opacity=1,#0.5
        line_opacity=1,#0.2
        legend_name='NDVI per gov',
        highlight=True,
        line_color='black',
        line_weight=2,
        smooth_factor=0)
    g = folium.GeoJson(state_geo, name="geojson").add_to(m)
    folium.GeoJsonTooltip(fields=["gov_name_f"],labels=True).add_to(g)
    # Add marker for Boulder, CO

    marker = folium.Marker(
        location=[33.886917, 9.537499],
        popup=folium.Popup(max_width=450).add_child(
            folium.Vega(luna, width=450, height=250)#df.to_json()
        ),
    )

    marker.add_to(m)

    m = m._repr_html_()

    plt.plot(range(10))
    fig = plt.gcf()
    # convert graph into dtring buffer and then we convert 64 bit code into image
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    return render(request, 'home.html', {'data': uri})
    context = {
        'm': m,
        'data': uri
    }

    return render(request, 'index.html', context)
