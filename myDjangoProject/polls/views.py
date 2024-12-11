# polls/views.py

from django.http import HttpResponse

def index(request):
    return HttpResponse("sw project")  # 간단한 응답을 반환합니다.
