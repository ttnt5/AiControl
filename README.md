<h1 align= "center" > 김한별
<p align = "center">
<img src="https://img.shields.io/badge/Python-3766AB?style=flat-square&logo=Python&logoColor=white"/></a>

## 취미

- 게임
- 책읽기

## 나의 장점
- 자기가 맡은일을 끈기있게 함
- 뭐든지 열심히 하려고 함

## 나의 단점 

- 집중력이 약함
- 내성적임

## 다짐

- 자격증 공부 열심히 하기
- 수업 열심히 참여하기

## 목표

- [ ] 기계정비 산업기사 따기
- [ ] 생산자동화 산업기사 따기
- [ ] 파이썬 능숙하게 하기

## 배운내용

|번호|기능
|:------:|:---:|
|1.|int(x [,base] </br> 정수변환
|2.|float(x) </br> 소수로 변환
|3.|complex(real [,imag]) </br> 복소수로 변환
|4.|str(x) </br> 문자열로 변환 </br> (사람이 알아보기 쉬운형태)
|5.|repr(x) </br> 문자열로 변환</br> (기계가 알아보기 쉬운형태)
|6.|eval(str) </br> 문자열을 입력하면 결과값으로 변환 </br> 해킹에 취약함
|7.|tuple(s) </br> 객체의 집합이고 값이 변하지 않음
|8.|list(s) 객체의 집합이고 값이 변함
|9.|set(s) </br> 집합 자료형 </br> 중복 허용x </br> 순서가 없음
|10.|dict(d) </br>사전
|11.|frozenset(s) </br> set과 다르게 집합 객체를 만들면 수정 불가
|12.|chr(x) 정수를 받고 정수에 해당하는 문자로 변환
|13.|unichr(x) </br> 정수를 받고 정수에 해당하는 유니코드 문자로 변환
|14.|ord(x) </br> 문자를 받고 문자에 해당하는 유니코드 정수를 변환
|15.|hex(x) </br>  정수를 16진수로 변환
|16.|oct(x) </br> 정수를 8진수로 변환

# 프로젝트
손의 좌표를 [mediapipe](https://google.github.io/mediapipe/) 모듈로 손의 마디를 좌표로 인식한후  
인공지능(AI)으로 학습시켜서 램프를 키는 프로젝트를 만들었습니다

아래 유사 프로젝트들의 소스코드를 적극 활용하였습니다.

* [gesture-recognition by kairess](https://github.com/kairess/gesture-recognition)

# 프로젝트 실행 과정

학습
1. 데이터셋.py 를 실행시킨후 웹캠으로 0도 90도 180도에 대한 데이터셋을 만듭니다.
2. 머신러닝.ipynb를 순서대로 실행시켜 ai를 학습합니다.

실행
1. 웹캠과 아두이노를 연결한후 손가락 방향을 바꾸면서 각도가 바뀌면 램프가 바뀌는지 확인한다.
<img src="https://github.com/LETAUK/AIControlE/blob/main/img/0s.JPG" width="300" height="200">
<img src="https://github.com/LETAUK/AIControlE/blob/main/img/90s.JPG" width="300" height="200">
<img src="https://github.com/LETAUK/AIControlE/blob/main/img/180s.JPG" width="300" height="200">

# 각 구성파일의 역할

|파일명|설명|
|------|---|
|dataset폴더|데이터셋을 저장하는 폴더입니다|
|models.h5|학습시킨 AI 모델입니다|
|sketch_nov15a폴더|아두이노 파일입니다|
|데이터셋.py|데이터셋을 만드는 실행파일입니다|
|머신러닝.ipynb|AI학습을 시키는파일입니다|
|실행.py|AI를 실행시키는 파일입니다|

# 한계

* 손의 여러가지 각도는 인식이 되지 않는다  
* 검지손가락 이외의 손가락으로 가리킬시 손가락인식이 불가능하다
