import numpy as np
import tensorflow
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os 


class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename
        self.model = load_model(os.path.join("artifacts", "training", "model.h5"))

    def predict(self):
        imagename = self.filename
        test_image = image.load_img(imagename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = np.argmax(self.model.predict(test_image), axis=1)

        if result[0] == 0:
            prediction = "Cyst"
            condition_info = "Cysts are fluid-filled sacs that can form in the kidneys. They are usually benign and often don't cause any symptoms. In some cases, they may need to be monitored if they grow large or cause discomfort."
            cure_info = "Most kidney cysts don't require treatment. If they cause symptoms or complications, treatment may include: Draining the cyst, Surgery to remove it, Medication to alleviate symptoms"
            return [{"image": prediction, "condition_info": condition_info, "cure_info": cure_info}]

        if result[0] == 1:
            prediction = "Normal"
            condition_info = "Your kidney appears normal according to the analysis."
            cure_info = "Since your kidney is normal, there's no specific treatment needed. Maintaining a healthy lifestyle with proper hydration and diet can help support kidney health."
            return [{"image": prediction, "condition_info": condition_info, "cure_info": cure_info}]

        if result[0] == 2:
            prediction = "Stone"
            condition_info = "Kidney stones are hard deposits made of minerals and salts that form inside the kidneys. They can cause severe pain, blood in urine, and other symptoms."
            cure_info = "Treatment for kidney stones may include: Pain medication, Drinking plenty of water to help pass the stone, Medical procedures like lithotripsy or surgery to remove large stones, Dietary changes to prevent recurrence"
            return [{"image": prediction, "condition_info": condition_info, "cure_info": cure_info}]

        if result[0] == 3:
            prediction = "Tumor"
            condition_info = "A kidney tumor is an abnormal growth of cells in the kidney. It can be benign (non-cancerous) or malignant (cancerous). Early detection and treatment are crucial for better outcomes."
            cure_info = "Treatment for kidney tumors depends on various factors including the type, size, and stage of the tumor. Options may include: Surgery, Radiation therapy, Chemotherapy, Targeted therapy, Immunotherapy"
            return [{"image": prediction, "condition_info": condition_info, "cure_info": cure_info}]
