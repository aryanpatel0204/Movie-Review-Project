from django.urls import path
from movie import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about),
    path('<int:movie_id>',views.detail,name='detail'),
]
#path('',views.about) for exam purpose
