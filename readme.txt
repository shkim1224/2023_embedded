본 github 사용방법
1) ubuntu의 chrome에서 https://github.com/shkim1224/2023_embedded 에 접속함
2) code 메뉴에서 "download zip"을 클릭하고 ubuntu의 작업 공간에 zip 파일을 다운 받고 압축해제
  => 압축해제된 폴더(작업 스페이스)에는 readme.txt와 requirements.tx 및 여러개의 파이선 코드가 들어 있음
3) ubuntu 22.04에 설치된 아나콘다를 이용하여 opencv_media (이름 달라도 됨) 가상환경을 생성
   $ conda create -n opencv_media python=3.8
   $ conda activate opencv_media
4) 디렉토리에 있는 requirements.txt 파일을 사용하여 작업관련 패키지를 한번에 설치함
   (opencv_media) $ pip install -r requirements.txt // 이 명령 수행은 requirements.txt 가 있는 위치에서 실행

5) 압축해제된 폴더에 들어가 vsc 를 실행시킴

