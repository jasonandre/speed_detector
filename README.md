#speed_detector

A.프로젝트 개요

-20, 30, 50, 80, stop 등 도로에서 관찰가능한 표지판 이미지를 분류하는 모델을 CNN 기반으로 만들었습니다. 

-4인 1조로 프로젝트를 진행했습니다.

-프로젝트기간 : 2024.08.06 ~ 2024.08.09  총4일

B.활용한 스킬

Django 프레임워크, python, html, css, javascript

-프로젝트는 크게 모델 생성과 웹 어플리케이션 제작 단계로 나누어 진행했습니다.

C. 담당 역할

1)django 프레임워크를 활용한 웹 제작

2)웹에서 모델 활성화 

3)머신러닝 모델개발

D. 프로젝트 진행단계

1)kaggle, hugging face 등에서 교통이미지 관련 데이터 수집

2)teachable machine, google colab 등을 활용하여 머신러닝 모델생성

3)Django 프레임워크 기반으로 웹 구성

4)모델 배포

#전처리, 평가부분을 제외한 모델 코드 입니다.


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

#예측정확도를 점검한 이미지입니다.
![image](https://github.com/user-attachments/assets/47df0296-f534-4827-a4b5-56c34399c515)


#안내사항
1. 모델 위치는 base\models\traffic_sign_classfication_cnn.keras 입니다.
2. 웹의 프론트엔드 부분은 base\templates\index.html 에서 확인하실 수 있습니다.
3. README.md 파일을 제외한 나머지 파일을 하나의 폴더에 다운받으신 후, 명령 프롬프트 혹은 anaconda 프롬프트에서 'cd 폴더이름' 명령어를 이용해 해당 폴더로 이동하신 다음 python manage.py runserver 명령어로 실행해 보실 수 있습니다.
4. 서버 유지비 문제로, 모델 실행가능한 사이트주소는 별도로 제공하지 않습니다. 

#이미지는 웹에서 표지판 이미지를 넣었을 때 실행 결과 입니다.
![image](https://github.com/user-attachments/assets/1c090b12-14e8-4212-b371-9806c2364fa5)

E.프로젝트 회고 

1)만족했던 부분: 
웹에서 실행할 때 버전호환이나 모델손상 등 문제없이 정상작동합니다. 이미지종류만 다르게 하면 다른 도메인의 이미지분류에도 적용가능할 것으로 보입니다.

2)아쉬웠던부분: 
웹 사이트 주소 배포의 경우, 무료 배포는 기간제한이 있어서 어려웠습니다. 
표지판 이미지가 회전하거나 다른 사물과 같이 있을 때, 인식 정확도가 떨어집니다. 더 많은 데이터와 라벨링, 성능개선이 필요합니다.
