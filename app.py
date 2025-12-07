from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
import numpy as np

# Try to import TensorFlow - it may not be available on Python 3.14+
TENSORFLOW_AVAILABLE = False
try:
    import tensorflow as tf
    from tensorflow.keras.models import load_model
    from tensorflow.keras.preprocessing import image
    TENSORFLOW_AVAILABLE = True
except ImportError:
    print("Warning: TensorFlow not available. ML models will not work.")
    print("Note: TensorFlow requires Python 3.11 or 3.12. You are using a different version.")

# model1 = load_model("./Selfmodel.keras")
# model2 = load_model("./ResNetmodel.keras")
# model3 = load_model("./MobileNetmodel.keras")
# model4 = load_model("./VGG16.keras")


UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__, template_folder='templates')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



##################################################
##################################################
##################################################

#TensorFlow Model Prediction
# def model1_prediction(test_image):
#     model = load_model("./Selfmodel.keras")
#     img = image.load_img(test_image, target_size = (224, 224))
#     i = image.img_to_array(img)/255
#     input_arr = np.array([i])
#     predictions = model.predict(input_arr)
#     predictions = "Healthy" if predictions >0.45492  else "Cardiovascular Disease"
#     return predictions

########################################################################
########################################################################
#########################################################################

def model2_prediction(test_image):
    if not TENSORFLOW_AVAILABLE:
        return "TensorFlow not available. Please install Python 3.11 or 3.12 with TensorFlow."
    try:
        model = load_model("./ResNetmodel.keras")
        img = image.load_img(test_image, target_size = (224, 224))
        i = image.img_to_array(img)/255
        input_arr = np.array([i])
        predictions = model.predict(input_arr)
        result = "Healthy" if predictions > 0.8473 else "Prone to/Suffering from Cardiovascular Disease."
        return result
    except Exception as e:
        return f"Error in ResNet prediction: {str(e)}"

    ########################################################################
    ########################################################################

def model3_prediction(test_image):
    if not TENSORFLOW_AVAILABLE:
        return "TensorFlow not available. Please install Python 3.11 or 3.12 with TensorFlow."
    try:
        model = load_model("./MobileNetmodel.keras")
        img = image.load_img(test_image, target_size = (224, 224))
        i = image.img_to_array(img)/255
        input_arr = np.array([i])
        predictions = model.predict(input_arr)
        result = "Healthy" if predictions < 0.5886 else "Prone to/Suffering from Cardiovascular Disease"
        return result
    except Exception as e:
        return f"Error in MobileNet prediction: {str(e)}"

    ########################################################################
    ########################################################################

def model4_prediction(test_image):
    if not TENSORFLOW_AVAILABLE:
        return "TensorFlow not available. Please install Python 3.11 or 3.12 with TensorFlow."
    try:
        model = load_model("./VGG16.keras")
        img = image.load_img(test_image, target_size = (224, 224))
        i = image.img_to_array(img)/255
        input_arr = np.array([i])
        predictions = model.predict(input_arr)
        result = "Healthy" if predictions < 0.4498 else "Prone to/Suffering from Cardiovascular Disease"
        return result
    except Exception as e:
        return f"Error in VGG16 prediction: {str(e)}"

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

# Login credentials
        if username == 'admin' and password == 'admin':
            return redirect('home')
        elif username == 'abhishek' and password == 'abhishek':
            return redirect('home')
        else:
           
            return render_template('/login.html')
    return render_template('/login.html')

@app.route('/home')
def home():
    return render_template('/home.html')

@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            if not os.path.exists(image_path):
                return "Image not found", 404

            # image checking
            # model1_result = model1_prediction(image_path) if request.form.get('model1') else None
            model2_result = model2_prediction(image_path) if request.form.get('model2') else None
            model3_result = model3_prediction(image_path) if request.form.get('model3') else None
            model4_result = model4_prediction(image_path) if request.form.get('model4') else None


            # # image checking ye remove ho jayega  upr wala ajayega
            # model1_result =  "Model not used"
            # model2_result =  "Model not used"
            # model3_result =  "Model not used"
            # model4_result =  "Model not used"

            return render_template('index.html',filename=filename,
                                #    model1_result=model1_result,
                                   model2_result=model2_result,
                                   model3_result=model3_result,
                                   model4_result=model4_result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)



   
