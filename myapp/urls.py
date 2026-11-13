from django.urls import path
from myapp import views
from .views import contact_ajax_view, privacy_view, MainPage, AllArtworks


app_name = 'myapp'
urlpatterns =[
    path('', views.MainPage.as_view(), name='main_page'),
    path('api/contact/', views.contact_ajax_view, name='contact_ajax'),
    path('privacy/', views.privacy_view, name='privacy_policy'),
    path('artworks/', views.AllArtworks.as_view(), name='all_artworks'),
]
    
    