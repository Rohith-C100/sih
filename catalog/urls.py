from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('jobs/', views.JobListView.as_view(), name='jobs'),
    path('job/<int:pk>', views.JobDetailView.as_view(), name='job-detail'),
    path('companies/',views.CompanyListView.as_view(),name='companies'),
    path('company/<int:pk>',views.CompanyDetailView.as_view(),name='company-detail')
]

