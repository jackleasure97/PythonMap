
import pandas as pd
import folium
from folium.plugins import Search

from folium.plugins import MarkerCluster
from pandas.io.formats.format import return_docstring

df_zips = pd.read_csv('combinedzipandlat.csv')
columns=pd.Index(['Zip','Potomac', 'Arlington','Hunt', 'Glen' 'Lat', 'Long','ID'], name='dmv')

df_zips


avg_location = df_zips[['Lat', 'Long']].mean()
map_dmv = folium.Map(location=avg_location, zoom_start=10)




PotomacOffice = (folium.Marker([39.061078, -77.157952],
                        radius=50,
                        popup='Potomac',
                        icon = folium.Icon(icon = 'home', color='blue'))

              .add_to(map_dmv))

ArlingtonOffice = (folium.Marker([38.880294,	-77.114794],
                        radius=100,
                        popup='Arlington',
                        color='red',
                        icon=folium.Icon(icon='home', color='red'))

.add_to(map_dmv))

HuntOffice = (folium.Marker([39.490480,	-76.664136],
                        radius=100,
                        popup='Hunt Valley',
                        color='green',
                        icon=folium.Icon(icon='home', color='green'))



          .add_to(map_dmv))




GlenOffice = (folium.Marker([37.671436, -77.573225],
                        radius=100,
                        popup='Glen Allen',
                        color='gray',
                        icon=folium.Icon(icon='home', color='gray'))



          .add_to(map_dmv))

marker_cluster = MarkerCluster().add_to(map_dmv)


for i in range(len(df_zips)):
    html = df_zips.loc[i,['Zip','Potomac','Arlington','Hunt','Glen']].to_frame().T.to_html(
        classes="table table-striped table-hover table-condensed table-responsive"
    )
    popup = folium.Popup(html, max_width=500)

    folium.Marker([df_zips.iloc[i]['Lat'], df_zips.iloc[i]['Long']], popup=popup, name=df_zips.iloc[i]["Zip"]).add_to(marker_cluster)


servicesearch = Search(
    layer=marker_cluster,
    search_label="name",
    placeholder='Search for Zip Code',
    collapsed=False,
).add_to(map_dmv)

map_dmv.save('map_dmv.html')

