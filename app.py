from osgeo import gdal

from flask import Flask, render_template, send_file
from io import BytesIO
from PIL import Image

app = Flask(__name__)

# open the geospatial data 
nurburgring_tiff = gdal.Open("./data/nurburgring.tif")

# Mock-up of your image array (example)
image_array =  nurburgring_tiff #np.random.rand(200, 300, 3) * 255  # Random RGB image

@app.route('/')
def show_image():
    return render_template('index.html')

@app.route('/image')
def get_image():
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
    app.run(debug=True, host='0.0.0.0', port=5000)