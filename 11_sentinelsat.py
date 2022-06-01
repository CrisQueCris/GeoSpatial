from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt
from datetime import date
from copernicus_config import copernicus_user, copernicus_password 

api = SentinelAPI(user= copernicus_user, password = copernicus_password, api_url='https://scihub.copernicus.eu/dhus')

product_id_example = 'S2A_MSIL2A_20220518T100601_N0400_R022_T33UUV_20220518T162816'

api.download(id= product_id_example, directory_path='Data/Copernicus/')





api = SentinelAPI('user', 'password', 'https://scihub.copernicus.eu/dhus')

# download single scene by known product id
api.download(<product_id>)

# search by polygon, time, and SciHub query keywords
footprint = geojson_to_wkt(read_geojson('/path/to/map.geojson'))
products = api.query(footprint,
                     date=('20151219', date(2015, 12, 29)),
                     platformname='Sentinel-2',
                     cloudcoverpercentage=(0, 30))

# download all results from the search
api.download_all(products)

# convert to Pandas DataFrame
products_df = api.to_dataframe(products)

# GeoJSON FeatureCollection containing footprints and metadata of the scenes
api.to_geojson(products)

# GeoPandas GeoDataFrame with the metadata of the scenes and the footprints as geometries
api.to_geodataframe(products)

# Get basic information about the product: its title, file size, MD5 sum, date, footprint and
# its download url
api.get_product_odata(<product_id>)

# Get the product's full metadata available on the server
api.get_product_odata(<product_id>, full=True)
