#!/usr/bin/env python
# coding: utf-8

# A csv file containing the ship movement data is given. The data contains unique ship id (mmid), timestamp, latitude and longitude.
# 
# The task given is to find probable collision events
# 
# Exploratory data analysis and plotting the data onto world map.

# In[140]:


#importing the libraries  and defining the haversine distance function
import numpy as np
import geopandas as gd
import pandas as pd
from geodatasets import get_path
import matplotlib.pyplot as plt
from sklearn.neighbors import BallTree
from sklearn.cluster import DBSCAN
from shapely.geometry import LineString, Point
from math import radians, cos, sin, asin, sqrt


# Haversine distance is the distance between two points on a sphere.
# 
# $d=2R\sin^{-1}\left(\sqrt{(\sin^2\left(\frac{\phi_2-\phi_1}{2}\right)\cos\phi_1\cos\phi_2\sin^2\left(\frac{\lambda_2-\lambda_1}{2}\right)}\right)$
# 
# where $R$ is the radius of the sphere, $\phi_{1,2}$ are latitudes and $\lambda_{1,2}$ are the longitudes

# In[141]:


def haversine_np(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1[:,None] 
    dlat = lat2 - lat1[:,None] 
    a = np.sin(dlat/2)**2 + np.cos(lat1[:,None]) * np.cos(lat2) * np.sin(dlon/2)**2
    #print("a=",a)
    c = 2 * np.arcsin(np.sqrt(a)) 
    r = 6371 # Radius of earth: 6371 kilometers
    return c * r


# Reading the data into pandas dataframe for exploratory analysis

# In[142]:


df = pd.read_csv("d:\sample_data.csv")
print(df.info())
print(df.head())
#converting go geodataframe
gdf = gd.GeoDataFrame(df, geometry=gd.points_from_xy(df.lon, df.lat), crs="EPSG:4326")
#getting the world map
world = gd.read_file(get_path("naturalearth.land"))


# In[143]:


#plotting the world map as background
ax = world.plot(color="white", edgecolor="black")
# plotting the geodatframe.
gdf.plot(ax=ax, color="red")


# Each point in the plot above is the location of ship covering all times. There are multiple points overlapping. 

# In[144]:


#convert timestamp into datetime format and get time difference.

df['timestamp']=pd.to_datetime(df['timestamp'])
start_time=df['timestamp'].min()

df['timediff']=(df['timestamp']-start_time).astype("timedelta64[s]")/60   #in minutes


# In[145]:


df['geometry']=df.apply(lambda x: Point(x['lon'],x['lat']),axis=1)


# In[146]:


s_df = df.sort_values(by=["mmsi","timestamp"],ascending=[True,False])


# In[147]:


linedf = s_df.groupby("mmsi", as_index=False).agg({"geometry": lambda x: LineString(x)})


# In[148]:


#plotting the movement of each ship as line
linedf = gd.GeoDataFrame(data=linedf, geometry=linedf.geometry, crs=4326)
ax = world.plot(color="white", edgecolor="black")

linedf.plot(ax=ax, column="mmsi", cmap="jet")
plt.show()


# The plot above is a line representation of ship-data. each color represent one line, resulting in a timeseries of different ships.
# 
# Potential collision is when two different ships come in close proximity within a small time window. To analyze this, first we will separate each ship's own timeline. Then, within a small window around each timestamp, we will analyze whether there is any other ship within a cutoff distance. 
# 
# We have taken time window of $\pm 1$ minute, and window of $\pm 0.01^{\circ}$ around latitude and longitude. We further refined it with a distance of $\pm 1$ kilometer.

# In[149]:


#get number of ships
mmsi_a=df['mmsi'].unique()


# In[150]:


print(mmsi_a)


# In[173]:


df_final=pd.DataFrame()   #This is the dataframe to collate all the possible collision events
for i in mmsi_a:
    #Getting the timeseries for ship i
    timeseries_df=df[df['mmsi']==i]
    
    timeseries=timeseries_df['timediff'].unique()
    
    #Getting data for all ships excluding ship i
    df_new=df[df['mmsi']!=i]
    
    for j in timeseries:

        #Recording the lat lon for ship i at time instance j. This will be useful for distance calculation
        orig_lat=pd.to_numeric(timeseries_df[timeseries_df['timediff']==j]['lat'].unique())
        orig_lon=pd.to_numeric(timeseries_df[timeseries_df['timediff']==j]['lon'].unique())
        
        #Filtering the data frame based on time window
        df_new4=df_new[abs(df_new['timediff']-j)<1]
        #Further filtering based on lat-lon
        df_new3=df_new4[abs(df_new4['lat']-orig_lat)<0.01]
        df_new2=df_new3[abs(df_new3['lon']-orig_lon)<0.01]
        
        if df_new2.empty:
            continue
        
        d=haversine_np(orig_lon,orig_lat, pd.to_numeric(df_new2['lon']).values,pd.to_numeric(df_new2['lat']).values).ravel()
        
        #Adding distance column, and final filter based on distance window
        
        df_new2.insert(6,'dist',d)
        df_new5=df_new2[df_new2['dist']<1]
        #df_new5['mmsi_1']=i   #The collision event is between ship i and ship mmid in df_new5
        df_new5.insert(7,'mmsi_1',i)
        #Appending the entry to the df_final dataframe
        if not(df_new5.empty):
            df_final=pd.concat([df_final,df_new5],ignore_index=True)
 
        else:
           continue

        
    
    


# In[174]:


print(df_final.head())


# In[175]:


df_final.info()


# The number of potential collision events can be obtained from the info of the dataframe. For the conditions set-up here, there are 1276 collision events. The plot below overlays the events as points on the lines of each ships.

# In[164]:


gdf = gd.GeoDataFrame(df_final, geometry=gd.points_from_xy(df_final.lon, df_final.lat), crs="EPSG:4326")
ax = world.plot(color="white", edgecolor="black")
linedf.plot(ax=ax, column="mmsi", cmap="hsv")
gdf.plot(ax=ax, color="red")


# In[ ]:




