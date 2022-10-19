from django.urls import path
from .. import views

app_name = 'slamy'

urlpatterns = [
    path('', views.Index, name='index'),
    path('import/', views.CSVImport.as_view(), name='import'),
]
