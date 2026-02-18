import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from tensorflow.keras.models import model_from_json
import numpy as np
from tensorflow.keras.preprocessing import image
import cv2

json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)
model.load_weights("model.weights.h5")
print("Loaded model from disk")

def classify(img_file):
    img_name = img_file
    test_image = image.load_img(img_name, target_size = (64, 64))

    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    result = model.predict(test_image)

    if result[0][0] == 1:
        prediction = 'Sachin'

    else:
        prediction = 'Dhoni'
    print(prediction,img_name)
    
    # Read the image using cv2 for visualization
    img_cv = cv2.imread(img_name)
    if img_cv is not None:
        # Resize for better visibility if needed, or keep original
        # img_cv = cv2.resize(img_cv, (600, 400)) 
        
        # Put text on image
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img_cv, prediction, (10, 50), font, 1.0, (255, 0, 0), 2, cv2.LINE_AA)
        
        # Show image
        cv2.imshow('Prediction', img_cv)
        print("Press any key to continue...")
        cv2.waitKey(0) # Wait for any key press to move to next image


import os
path = 'Dataset/test'
files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
   for file in f:
     if file.lower().endswith(('.jpg', '.jpeg', '.png')):
       files.append(os.path.join(r, file))

for f in files:
   classify(f)
   print('\n')

cv2.destroyAllWindows()
