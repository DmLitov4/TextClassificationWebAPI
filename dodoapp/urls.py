from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api/predictions/$', views.PredictionAPIView.as_view()),
]
