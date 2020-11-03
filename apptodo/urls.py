from django.urls import path
from .import views
from .views import Index,update

urlpatterns = [
    path('',Index.as_view(),name="index"),
    path('update/<str:workid>/',views.update,name="update"),

]