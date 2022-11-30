import os.path

from qrcodegenerator import create_qr_code_image
from config import Config

from flask import Flask, send_file, request  # , render_template

app = Flask(__name__)  # Create a Flask instance


@app.route("/", methods=['GET'])  # Create a route for the default URL, which is '/'
def index_get():  # Create a function which is called when the default URL is requested using GET
    # qr_code_url = url_for('static', filename=Config.QR_CODE_DEFAULT_FILE_NAME)
    form = '<h1>Make a QR Code</h1><form method="POST" action="/"> \
                <label for="qrurl">QR URL:</label><br> \
                <input type="text" id="qrurl" name="qrurl" value="http://www.njit.edu"><br> \
                 <input type="submit" value="Submit"> \
            </form>'

    return form  # Return a simple HTML form


@app.route("/", methods=['POST'])  # Create a route for the default URL, which is '/', but use POST
def index_post():  # Create a function which is called when the default URL is requested using POST
    full_path = os.getcwd()  # Get the current working directory
    qr_url = request.form.get("qrurl")  # Get the value of the form field named 'qrurl'
    qr_file_name = request.form.get("qr_file_name")  # Get the value of the form field named 'qr_file_name'

    directory_path_and_file_name = os.path.join(full_path, Config.QR_CODE_IMAGE_DIRECTORY,
                                                Config.QR_CODE_DEFAULT_FILE_NAME)  # Create a path to the QR code image

    qr_image = create_qr_code_image(qr_url)  # Create a QR code image
    for i in range(0, 1):  # Loop through the image
        while True:  # Loop forever
            try:  # Try to
                qr_image.save(directory_path_and_file_name)  # Save the QR code image
            except FileNotFoundError:  # If the file is not found
                qr_image_directory = Config.QR_CODE_IMAGE_DIRECTORY  # Get the QR code image directory
                new_directory_path = \
                    os.path.join(full_path, qr_image_directory)  # Create a path to the QR code image directory
                os.mkdir(new_directory_path)  # Create the QR code image directory
                continue  # Continue the loop
            break  # Break the loop
    return send_file(directory_path_and_file_name, mimetype='image/png')  # Return the QR code image
