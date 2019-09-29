from django.urls import path

from . import views

app_name= 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/detail/', views.detail, name='detail'),
    path('<int:question_id>/result/', views.result, name='result'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
# the blank ('' ..) in path means the urls.py in pollster will be directed to path in urls.py in polls
#question_id path is accessed by views