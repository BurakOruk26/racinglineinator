from flask import Flask, render_template, send_file, url_for, redirect
from io import BytesIO
from PIL import Image

from process_image import process_image
from rasterlib import Rasterize


app = Flask(__name__)

# open the geospatial data 
nurburgring_tiff = Rasterize("./data/nurburgring.tif")

# Read the raster data as a NumPy array
image_array = nurburgring_tiff.to_image()

@app.route('/')
def home():
    return redirect(url_for('show_image'))

@app.route('/display')
def show_image():
    return render_template('index.html')

@app.route('/getimage')
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
    app.run(debug=True, host='0.0.0.0', port=5000)