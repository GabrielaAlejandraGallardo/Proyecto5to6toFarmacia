from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static 

urlpatterns = [
 
    path('', views.inicio, name='inicio'),
    path('index', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('add/addrecord/', views.addrecord, name='addrecord'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
  
    ]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 









