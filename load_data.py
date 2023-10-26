


import os
import netCDF4 as nc4
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import numpy as np



def load_data():
    """
    load_data carga los datos de los archivos netCDF en un GeoDataFrame

    Returns
    -------
    gdfs : dict
    
        Un diccionario que contiene los datos de los archivos netCDF en un GeoDataFrame
    """
    # Ruta al directorio que contiene los archivos netCDF
    directorio_archivos = 'descargas'
    # Lista de archivos netCDF en el directorio
    archivos_netCDF = [os.path.join(directorio_archivos, nombre_archivo) for nombre_archivo in os.listdir(directorio_archivos) if nombre_archivo.endswith('.nc4')]

    # Lista para almacenar los GeoDataFrames de cada archivo
    gdfs = {}

    for archivo_netCDF in archivos_netCDF:
        try:
            # Abre el archivo netCDF
            dataset = nc4.Dataset(archivo_netCDF, 'r')
            fecha = archivo_netCDF[15:25]
            # Extrae las coordenadas latitud y longitud
            latitudes = dataset.variables['Latitude'][:]
            longitudes = dataset.variables['Longitude'][:]

            # Extrae la variable de interés (por ejemplo, 'temperatura')
            co2_free_troposphere = dataset.variables['mole_fraction_of_carbon_dioxide_in_free_troposphere'][:, :]
            co2_free_troposphere_sd = dataset.variables['mole_fraction_of_carbon_dioxide_in_free_troposphere_sdev'][:, :]
            # Crea una malla de coordenadas a partir de latitudes y longitudes
            lon, lat = np.meshgrid(longitudes, latitudes)

            # Aplana las mallas de coordenadas y la matriz de co2_free_troposphere a vectores unidimensionales
            lon_flat = lon #.flatten()
            lat_flat = lat #.flatten()
            co2_free_troposphere_flat = co2_free_troposphere #.flatten()

            # Crea un GeoDataFrame con las variables aplanadas
            geometry = [Point(lon, lat) for lon, lat in zip(lon_flat, lat_flat)]
            gdf = gpd.GeoDataFrame({'Latitude': lat_flat.mean(), 'Longitude': lon_flat.mean(),
                                'CO2_Free_Troposphere': co2_free_troposphere_flat.mean(),
                                "CO2_Free_Troposphere_SD": co2_free_troposphere_sd.mean()}, geometry=geometry, crs="EPSG:4326")

            # Crea un DataFrame de Pandas
        # df = pd.DataFrame({'Latitud': latitudes, 'Longitud': longitudes, 'Temperatura': variable_interes})

            # Crea una columna de geometría utilizando Shapely Point
        # df['geometry'] = [Point(xy) for xy in zip(df['Longitud'], df['Latitud'])]

            # Convierte el DataFrame en un GeoDataFrame
        #   gdf = gpd.GeoDataFrame(df, geometry='geometry')
            ruta_data = archivo_netCDF[0].split('/')
            for i in ruta_data:
                if i[:5] == "AIRS":
                    fecha = i[6:16]
                    break
            # fecha = archivo_netCDF[5:15]
            # Agrega el GeoDataFrame a la lista
            gdfs[fecha] = gdf
            print(f'Se cargó el archivo {archivo_netCDF} correctamente.')
        except Exception as e:
            print(f'Ocurrió un error al abrir el archivo {archivo_netCDF}:{archivo_netCDF[16:26]}: {e}')

    # Combina todos los GeoDataFrames en uno solo
    # geo_dataframe_completo = pd.concat(gdfs, ignore_index=True)

    # Ahora tienes un dict que contiene los datos de todos los archivos netCDF en el directorio.

    # gdfs.keys()
    return gdfs