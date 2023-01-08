from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/msg-chatbot', views.handle_post_request, name='msg'),
]
