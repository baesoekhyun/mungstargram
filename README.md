현재 사진 +글 업로드 까지 마친상태
+ 오른쪽 하이퍼링크 까지.
+ 회원가입 + 로그인 까지 .
+ 로그 아웃 까지.
+ 프로필 페이지 만들기 + 프로필 변경하기
+ 좋아요, 댓글, 북마크 기능까지 완료
+ 프로필 들어가면 내 게시물,좋아요,북마크 기능 보이게 하기
가상환경 생성
python -m venv venv
가상환경 실행
/venv/Scripts/acrivate
필요 package 설치
pip install -r requrments.txt
DB생성
python manage.py makemigrations
python manage.py migrate
서버 실행
python manage.py runserver
