# Traffic Signs 인식 및 분류 프로젝트

A. 프로젝트 개요
  - 20, 30, 50, 80, stop 등 도로에서 관찰가능한 표지판 이미지를 분류하는 CNN 모델
  - 참여 인원 4인
  - 프로젝트기간 : 2024.07.15 ~ 2024.08.09

B. 활용한 스킬
  - 웹 : Django, html, css, javascript , AI : Conv2D 
  - 프로젝트는 CNN모델 개발과 웹 어플리케이션 제작 단계로 나누어 진행

C. 담당 역할
 - django 프레임워크를 활용한 웹 제작
 - 웹에서 모델 활성화 
 - 머신러닝 모델개발

D. 프로젝트 진행단계
  1. kaggle, hugging face 에서 교통이미지 관련 데이터 수집
  2. IDE(google colab, VScode)에서  머신러닝 모델생성
     
     #데이터 수
     - train 34799 개
     - valid  4410 개
     - test  12630 개

     #데이터 전처리
     - 셔플
     - 정수형 클래스 레이블 원핫인코딩 : to_categorical

     #모델
     - input 데이터 : 32 * 32 RGB 이미지
     - kernel_size : 3
     - 총 레이어 수 7개 (input, output 제외)  
     - layer 3개, 필터수 32, 배치정규화 3회, 드랍아웃 1회
     - layer 3개, 필터수 64, 배치정규화 3회, 드랍아웃 1회
     - layer 1개, 필터수 128, 배치정규화 1회, 드랍아웃 1회
     - 라벨 수 43
     - 활성화 함수 :relu , 출력 레이어 활성화 함수 : softmax
     - optimizer="adam", loss="categorical_crossentropy", metrics="accuracy"

     #모델 학습
     - epoch 10회
     - batch size = 500
     - validation_split = 0.2

     #결과
     - accuracy : 0.9928
     - loss : 0.0279
     - val_accuracy : 0.9895
     - val_loss 0.0365
     
     
  3. Django 프레임워크 기반으로 웹 구성
   - base 폴더
      - models 에 생성한 모델첨부
      - templates 폴더의 index.html 문서에 웹 프론트엔드 작업(이미지 입력, 문구, 폰트 등)
      - views, urls, static 설정
      - media 폴더에 입력받은 이미지 저장 설정
   - speed_detector 폴더
      - settings, urls 설정 
      
  4. 모델 실행결과 확인 및 오류수정



#예측정확도를 점검한 이미지입니다.
![image](https://github.com/user-attachments/assets/47df0296-f534-4827-a4b5-56c34399c515)




#특이사항
 1. 모델 위치 : base\models\traffic_sign_classfication_cnn.keras 
 2. 웹html 위치 : base\templates\index.html 
 3. 서버 유지비 문제로, 모델 실행가능한 사이트주소 없음 





#이미지는 웹에서 표지판 이미지를 넣었을 때 실행 결과 입니다.
![image](https://github.com/user-attachments/assets/1c090b12-14e8-4212-b371-9806c2364fa5)





E. 프로젝트 회고 
- 만족했던 부분: 
   - 웹에서 실행할 때 버전호환이나 모델손상 등 문제없이 정상작동 
   - 이미지종류만 변경해서 다른 도메인의 이미지분류에도 적용가능
   - 43개 라벨을 정확히 분류 가능하고, 웹에서 확률을 표시해주는 기능 존재

- 아쉬웠던부분: 
   - 웹 사이트 주소 배포의 경우, 무료 배포는 기간제한이 있어 어려움 
   - 표지판 이미지가 회전하거나 다른 사물과 같이 있을 때, 인식 정확도가 떨어지는 문제 존재, 데이터 추가 수집 및 증강 기법 적용 필요. 
