from django.urls import path
from hr import views

urlpatterns = [
    path('hrdash/',views.hrHome,name='hrdash'),
    path('postjob/',views.postJobs,name='postjob'),
    path('candidate-detail/<int:pk>/', views.candidate_view, name='candidate_details'),
    path('select-candidate/', views.selectCandidate, name='selectcandidate'),
    path('delete-candidate/', views.deleteCandidate, name='deletecand'),
]