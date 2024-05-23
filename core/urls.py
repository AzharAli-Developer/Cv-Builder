from django.urls import path
from .import views
urlpatterns = [
    path('home/',views.main,name='home'),
    path('candidate/<int:candidate_id>/', views.candidate_detail,name='candidate')
]