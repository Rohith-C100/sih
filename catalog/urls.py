from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('signup', views.signup, name='signup'),
    path('filter', views.filter, name='filter'),
    path('lecturer/<int:pk>', views.LecturerDetailView.as_view(), name='lecturer-detail'),
    path('colleges/',views.CollegeListView.as_view(),name='colleges'),
    path('college/<int:pk>',views.CollegeDetailView.as_view(),name='college-detail')

]


urlpatterns += [
    path('lecturer/<int:pk>/feedback/', views.feedback_lecturer, name='feedback-to-lecturer'),
    path('college/<int:pk>/feedback/', views.feedback_college, name='feedback-to-college'),
    path('thankyou',views.Thanku,name='thanku')
]