from django.urls import path

from . import views


urlpatterns = [
    # path("", views.index, name="index"),
    # path("<str:room_name>/", views.room, name="room"),
    path('login/', views.MyLoginView.as_view(), name='login'),
    path("chat/", views.index, name="index"),
    path("chat/<str:room_name>/", views.room, name="room"),
    path('/', views.MyLogoutView.as_view(), name='logout'),

]
