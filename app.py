from flask import Flask, render_template, redirect, url_for, flash, request, send_from_directory
import subprocess
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flashing messages
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

RESULTS_DIR = os.path.join('runs', 'detect')

@app.route('/')
def index():
    result_img = request.args.get('result_img')
    return render_template('index.html', result_img=result_img)

def get_latest_result_image():
    # Find the latest prediction folder
    folders = [f for f in os.listdir(RESULTS_DIR) if f.startswith('predict')]
    if not folders:
        return None
    latest_folder = max(folders, key=lambda x: os.path.getmtime(os.path.join(RESULTS_DIR, x)))
    folder_path = os.path.join(RESULTS_DIR, latest_folder)
    # Find the first .jpg file in the folder
    for file in os.listdir(folder_path):
        if file.lower().endswith('.jpg'):
            return os.path.join(folder_path, file)
    return None

@app.route('/predict', methods=['POST'])
def predict():
    source = request.form.get('source')
    image_path = None
    if source == 'image' and 'image' in request.files:
        file = request.files['image']
        if file.filename != '':
            filename = secure_filename(file.filename)
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(image_path)
            source_arg = image_path
        else:
            flash('No image selected.', 'danger')
            return redirect(url_for('index'))
    else:
        # Default to webcam
        source_arg = '0'

    try:
        subprocess.run(['python', 'predict.py', source_arg], check=True)
        result_img = get_latest_result_image()
        if result_img:
            # Serve the image via a static route
            return redirect(url_for('index', result_img=result_img.replace('\\', '/')))
        else:
            flash('Prediction completed, but no result image found.', 'warning')
    except subprocess.CalledProcessError:
        flash('Prediction failed. Please check the server logs.', 'danger')
    return redirect(url_for('index'))

@app.route('/result_img/<path:filename>')
def result_img(filename):
    # Serve result images from the runs/detect folders
    return send_from_directory('.', filename)

if __name__ == '__main__':
    app.run(debug=True) 