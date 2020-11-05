from django.urls import path
from .import views
from .views import Index,update,delete_task

urlpatterns = [
    path('',Index.as_view(),name="index"),
    path('update/<str:workid>/',views.update,name="update"),
    path('delete_task/<str:workid>/',views.delete_task,name="delete_task"),

]