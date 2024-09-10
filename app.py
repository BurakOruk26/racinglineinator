from osgeo import gdal

nurburgring_tiff = gdal.Open("./data/nurburgring.tif")

print("We have done it mamma!")