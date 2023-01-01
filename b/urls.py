from django.urls import path
from . import views



app_name = 'b'


urlpatterns = [
    path('', views.Home, name='home'),
    path('UPLOADS/', views.upload, name='videos'),
    path("contact/", views.contact, name="contact"),

    path('welcome', views.Pastor_desk, name='pastor'),

    path('JOIN-ME-IN-PRAYER/', views.PrayerView, name='pray'),
    path('Biblical-COUNSELling', views.Counselling, name='counsel'),
    path('ABOUT-US/', views.About, name='about'),

    path('BREAKTHROUGH-TIME/', views.Testy, name='testimony'),


    path('PRAYER-MINISTRY/', views.prayerforce, name='prayerforce'),

    path('PROPHETIC-FOCUS/', views.Monthly, name='yt'),


    path('PREACHINGS/', views.service, name='sunday'),
    path('WORD-OF-FAITH/', views.all_message, name='messages'), # messages or sms
    path('MESSAGE<int:id>', views.MDetail, name='detail'),
    path('all-category', views.all_category, name='all-category'),
    path('category<int:id>', views.category, name='category'),

]
