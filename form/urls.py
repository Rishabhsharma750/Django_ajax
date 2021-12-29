
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('form/', views.form, name='form'),
    path('table_data/', views.table_data, name='table_data'),
    path('edit/', views.edit, name='edit_data'),
    path('delete/<user_id>/', views.delete, name='delete_data'),
    path('datalist/', views.datalist, name='datalist'),
    path('withajaxdata/', views.withajaxdata, name='withajaxdata'),
]
