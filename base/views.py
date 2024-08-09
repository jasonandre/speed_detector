from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import default_storage
import tensorflow as tf
from keras.preprocessing import image
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model
import os
import numpy as np
from PIL import Image


def speed_detector(request):
    file = request.FILES.get("file")
    if not file:
        return render(request, "index.html")

    else:
        file_name = file.name
        file_path = os.path.join(settings.MEDIA_ROOT, "images", file_name)

        # Save the uploaded file
        with default_storage.open(file_path, "wb+") as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        
        # 테스트 데이터 준비
        # test_image = Image.open(file_path)
        # test_image = test_image.resize((32, 32))
        # test_image = np.asarray(test_image) / 255.0
        # test_image = test_image.reshape(1, 32, 32, 3)
        test_image = image.load_img(file_path, target_size=(32, 32))
        test_image = img_to_array(test_image) / 255.0
        test_image = np.expand_dims(test_image, axis=0)

        # 사전학습 모델 가져오기
        model = load_model("base/models/traffic_sign_classfication_cnn.keras")

        
        # 라벨이름 저장
        label_names = [
            'Speed limit (20km/h)',
            'Speed limit (30km/h)', 
            'Speed limit (50km/h)', 
            'Speed limit (60km/h)', 
            'Speed limit (70km/h)', 
            'Speed limit (80km/h)', 
            'End of speed limit (80km/h)', 
            'Speed limit (100km/h)', 
            'Speed limit (120km/h)', 
            'No passing', 
            'No passing veh over 3.5 tons', 
            'Right-of-way at intersection', 
            'Priority road', 
            'Yield', 
            'Stop', 
            'No vehicles', 
            'Veh > 3.5 tons prohibited', 
            'No entry', 
            'General caution', 
            'Dangerous curve left', 
            'Dangerous curve right', 
            'Double curve', 
            'Bumpy road', 
            'Slippery road', 
            'Road narrows on the right', 
            'Road work', 
            'Traffic signals', 
            'Pedestrians', 
            'Children crossing', 
            'Bicycles crossing', 
            'Beware of ice/snow',
            'Wild animals crossing', 
            'End speed + passing limits', 
            'Turn right ahead', 
            'Turn left ahead', 
            'Ahead only', 
            'Go straight or right', 
            'Go straight or left', 
            'Keep right', 
            'Keep left', 
            'Roundabout mandatory', 
            'End of no passing', 
            'End no passing veh > 3.5 tons'
        ]

        pred = model.predict(test_image)
        objs_num = np.argmax(pred, axis=1)[0]
        objs = label_names[objs_num]
        probs = pred[0][int(objs_num)]

        img_url = f"{settings.MEDIA_URL}images/{file_name}"

        return render(request, "index.html", {"objs": objs, "probs": probs,"img_url": img_url})