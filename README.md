## AI허브 오픈 데이터를 원하는 포맷으로 학습 DB 구축하기
- 한국인 대화 음성 샘플 데이터 다운로드
- 데이터 확인 후 훈련DB 포맷으로 구축

### 📁Dataset
원천 데이터셋은 AI-Hub의 한국인 대화음성 샘플 데이터를 활용하였습니다.

https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=&topMenu=&aihubDataSe=data&dataSetSn=130

### 📌Results Description
화자(34, 35)별로 폴더를 나누어 정리
각 폴더 구성
- wav : 음성 파일
- etc : 텍스트 파일
  - DURINFO : 각 파일 정보 + 음성 파일 길이
  - LANG : 각 파일 정보 + 옳은 스크립트 (원천 데이터의 괄호 중 첫 번째)
  - PROMPT : 각 파일 정보 + 틀린 스크립트 (원천 데이터의 괄호 중 두 번째)
