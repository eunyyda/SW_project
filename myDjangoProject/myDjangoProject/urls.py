#  myDjangoProject/urls.py

from django.contrib import admin
from django.urls import path, include

from  myDjangoProject.views import main,weathersite 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),  # polls.urls를 포함
    path('', main, name='main'),
    path('weather/', weathersite, name='weathersite'),
]



