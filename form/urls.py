
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('form/', views.form, name='form'),
    path('table_data/', views.table_data, name='table_data'),
    path('datalist/', views.datalist, name='datalist'),
    path('withajaxdata/', views.withajaxdata, name='withajaxdata'),
]
