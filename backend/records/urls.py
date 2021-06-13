from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    # path(r'about/', views.about, name='about'),
    path('', views.main, name='index'),
    path('api/v2/record/', views.RecordList.as_view()),
    path('api/v2/record/<slug:pk>/', views.RecordDetail.as_view()),
]
