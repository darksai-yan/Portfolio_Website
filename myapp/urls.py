from django.urls import path
from myapp import views

app_name = 'myapp'
urlpatterns =[
    path('', views.MainPage.as_view(), name='main_page'),
]
    
    