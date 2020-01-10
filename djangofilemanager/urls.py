from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<path:name>', views.view, name='view'),
    path('download/<path:name>', views.download, name='download'),
    path('create/<path:name>', views.create, name='create'),
    path('delete/<path:name>', views.delete, name='delete')
]