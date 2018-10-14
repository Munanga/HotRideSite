from core.views import Home,Upload,search_ride,Update,Delete
from django.urls import path

app_name = 'app'

urlpatterns = [
    path('', Home.as_view(),name='home'),
    path('upload/', Upload.as_view(),name='upload'),
    path('find/', search_ride,name='find'),
    path('<int:id>/update/', Update.as_view(),name='update'),
    path('delete/', Delete.as_view(),name='delete'),
]


