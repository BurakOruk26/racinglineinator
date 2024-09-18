from osgeo import gdal
import numpy as np

class Rasterize:
    def __init__( self, raster_path : str ) -> None:   
        self.gdal_dataset : gdal.Dataset = gdal.Open(raster_path)
        
    
    def to_image( self ) -> np.ndarray:
        # Read the raster data as a NumPy array
        image_array = self.gdal_dataset.ReadAsArray()
        
        band_count = self.gdal_dataset.RasterCount

        if band_count == 3:
            # If the image has three bands, this indicates a processed raster.
            # Stack those channels along the third axis to create an RGB image.
            red =   0
            green = 1
            blue =  2
        elif band_count == 1:
            # If the image has only one band, you might want to replicate it across three channels
            red =   0
            green = 0
            blue =  0
        else:
            # If the image has more than 3 channels, this indicates a direct satellite image.
            # First identify the satellite and then chose the rgb channels accordingly.
            satellite_source = self._identify_raster_source()
            if satellite_source == 1:
                red =   3   -1
                green = 2   -1
                blue =  1   -1
            elif satellite_source == -1:
                red =   4   -1
                green = 3   -1
                blue =  2   -1
            else:
                raise Exception( "Satellite source of the raster can not be identified!" )

        return np.dstack( [ image_array[red, :, :], image_array[green, :, :], image_array[blue, :, :] ])

    def _identify_raster_source( self ):
        dataset = self.gdal_dataset

        metadata = dataset.GetMetadata()
        driver = dataset.GetDriver().ShortName
        sensor_data = metadata.get('SENSOR', '')

        if 'SENTINEL2' in driver or 'SENTINEL' in sensor_data:
            return -1
        elif 'LANDSAT' in sensor_data :
            return 1
        else:
            return 0
        

"""
The OG Code copied from app.py:

# open the geospatial data 
nurburgring_tiff : gdal.Dataset = gdal.Open("./data/nurburgring.tif")

# Read the raster data as a NumPy array
image_array = nurburgring_tiff.ReadAsArray()

# If the image has multiple bands, stack them along the third axis to create an RGB image
if len(image_array.shape) == 3:
    image_array = np.dstack([image_array[i, :, :] for i in range(image_array.shape[0])])
else:
    # If the image has only one band, you might want to replicate it across three channels
    image_array = np.stack((image_array,) * 3, axis=-1)

"""