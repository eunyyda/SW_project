# polls/urls.py

from django.urls import path
from . import views  # 현재 디렉터리의 views.py 파일에서 views를 가져옵니다

urlpatterns = [
    path('', views.index, name='index'),  # 기본 경로에 대한 URL을 정의합니다.
]
