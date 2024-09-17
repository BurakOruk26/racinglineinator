from osgeo import gdal

from flask import Flask, render_template, send_file
from io import BytesIO
from PIL import Image
import numpy as np

from process_image import process_image

app = Flask(__name__)

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

@app.route('/')
def show_image():
    return render_template('index.html')

@app.route('/image')
def get_image():
    # process the image
    process_image(image_array)

    # Convert the NumPy array to a PIL Image
    img = Image.fromarray(image_array.astype('uint8'))

    # Resize the image
    new_size = (700, 700)  # width, height
    img.thumbnail(new_size)
    
    # Save the image to a BytesIO object (as an in-memory file)
    img_io = BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)  # Seek to the start so it can be read

    return send_file(img_io, mimetype='image/png')

if __name__ == '__main__':
    print("We have done it mamma!")
    app.run(host='0.0.0.0', port=5000)