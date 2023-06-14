
from django.contrib import admin
from django.urls import include, path
from chat import views


urlpatterns = [
    # path('login/', views.MyLoginView.as_view(), name='login'),
    # path("chat/", include("chat.urls")),
    # path("admin/", admin.site.urls),
    # path('', views.MyLogoutView.as_view(), name='logout'),
    path("admin/", admin.site.urls),
    path("", include("chat.urls")),




]