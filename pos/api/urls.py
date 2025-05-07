from django.urls import path, include
from api import views
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    TableRestoListApiView, TableRestoDetailApiView,RegisterUserApiView,
)

app_name = 'api'

urlpatterns = [
    #path('api/v1/login', LoginView.as_view()),
    #path('api/v1/logout', LogoutView.as_view()),
    #path('api/v1/register', RegisterWaitressAPI.as_view()),
    path('api/table_resto/', views.TableRestoListApiView.as_view()),
    path('api/table_resto/<int:id>/', views.TableRestoDetailApiView.as_view()),
    path('api/register', RegisterUserApiView.as_view()),
]
