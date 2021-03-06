from django.contrib import admin
from django.urls import path
import crudApp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', crudApp.views.main, name='main'),
    path('detail/<str:id>/', crudApp.views.detail, name='detail'),
    path('read/', crudApp.views.read, name = 'read'),
    path('new/create/', crudApp.views.create, name='create'),
    path('edit/<str:id>/', crudApp.views.edit, name='edit'),
    path('delete/<str:id>/', crudApp.views.delete, name='delete'),
]