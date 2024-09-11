#speed_detector

#프로젝트는 크게 모델 생성과 웹 어플리케이션 제작 단계로 나누어 진행했습니다.

#20, 30, 50, 80, stop 등 도로에서 관찰가능한 표지판 이미지를 분류하는 모델을 CNN 기반으로 만들었습니다. 

#4인 1조로 프로젝트를 진행했습니다. 각자 모델을 만들고 가장 좋은 것을 선택하는 방식으로 진행한 결과, 모델은 제가 직접 제작한 것이 아닌 다른 분이 제작한 것을 채택했습니다. 

#모델 구성 코드 입니다.

cnn_model = Sequential()

cnn_model.add(Conv2D(32, kernel_size = 3, activation='relu', input_shape = (32, 32, 3)))
cnn_model.add(BatchNormalization())
cnn_model.add(Conv2D(32, kernel_size = 3, activation='relu'))
cnn_model.add(BatchNormalization())
cnn_model.add(Conv2D(32, kernel_size = 5, strides=2, padding='same', activation='relu'))
cnn_model.add(BatchNormalization())
cnn_model.add(Dropout(0.4))

cnn_model.add(Conv2D(64, kernel_size = 3, activation='relu'))
cnn_model.add(BatchNormalization())
cnn_model.add(Conv2D(64, kernel_size = 3, activation='relu'))
cnn_model.add(BatchNormalization())
cnn_model.add(Conv2D(64, kernel_size = 5, strides=2, padding='same', activation='relu'))
cnn_model.add(BatchNormalization())
cnn_model.add(Dropout(0.4))

cnn_model.add(Conv2D(128, kernel_size = 4, activation='relu'))
cnn_model.add(BatchNormalization())
cnn_model.add(Flatten())
cnn_model.add(Dropout(0.4))
cnn_model.add(Dense(43, activation='softmax'))

cnn_model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])



#안내사항
1. 모델 위치는 base\models\traffic_sign_classfication_cnn.keras 입니다.
2. 웹의 프론트엔드 부분은 base\templates\index.html 에서 확인하실 수 있습니다.
3. README.md 파일을 제외한 나머지 파일을 하나의 폴더에 다운받으신 후 명령 프롬프트에서 python manage.py runserver 명령어로 실행해 보실 수 있습니다.
4. 서버 유지비 문제로, 모델 실행가능한 사이트주소는 별도로 제공하지 않습니다. 




