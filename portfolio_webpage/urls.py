from django.urls import path, include
from portfolio_webpage import views

urlpatterns = [
    path('', views.index, name='index'),
    path('send', views.send, name="send"),
    path('succeed', views.succeed, name="succeed"),
    path('oops', views.oops, name='oops')
]