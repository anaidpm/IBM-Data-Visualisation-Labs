
# coding: utf-8

# In[3]:


import numpy as np  # useful for many scientific computing in Python
import pandas as pd # primary data structure library

df = pd.read_csv('https://cocl.us/sanfran_crime_dataset')
df.rename(columns={'PdDistrict':'Neighbourhood'}, inplace=True)

print ('Data read into a pandas dataframe!')

df.head()


# In[14]:


df_areas=df.groupby('Neighbourhood',axis=0).count()
df_areas=df_areas[['IncidntNum']]
df_areas.rename(columns={'IncidntNum':'Count'}, inplace=True)

df_areas


# In[17]:


get_ipython().system('conda install -c conda-forge folium=0.5.0 --yes')
import folium
# San Francisco latitude and longitude values
latitude = 37.77
longitude = -122.42
# create map and display it
sanfran_map = folium.Map(location=[latitude, longitude], zoom_start=12)

# display the map of San Francisco
sanfran_map


# In[26]:


# download countries geojson file
get_ipython().system('wget --quiet https://cocl.us/sanfran_geojson -O sanfran.json')
    
print('GeoJSON file downloaded!')

df_areas=df_areas.reset_index()
df_areas


# In[32]:



san_geo = r'sanfran.json'

# create a numpy array of length 6 and has linear spacing from the minium total immigration to the maximum total immigration
threshold_scale = np.linspace(df_areas['Count'].min(),
                              df_areas['Count'].max(),
                              6, dtype=int)
threshold_scale = threshold_scale.tolist() # change the numpy array to a list
threshold_scale[-1] = threshold_scale[-1] + 1 # make sure that the last value of the list is greater than the maximum immigration

# let Folium determine the scale.
sanfran_map = folium.Map(location=[latitude, longitude], zoom_start=12)
sanfran_map.choropleth(
    geo_data=san_geo,
    data=df_areas,
    columns=['Neighbourhood', 'Count'],
    key_on='feature.properties.DISTRICT',
    threshold_scale=threshold_scale,
    fill_color='YlOrRd', 
    fill_opacity=0.7, 
    line_opacity=0.2,
    legend_name='Crime in San Francisco',
    reset=True
)
sanfran_map

