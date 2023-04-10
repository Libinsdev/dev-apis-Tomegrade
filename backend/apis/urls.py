from knox import views as knox_views
from .views import RegisterAPI,LoginAPI
from django.urls import path
from . import views



urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/userinfo/', views.userinfo, name="userinfo"),
    path('api/courses/offered/<str:pk>/',views.university_course,name="university_course"),
    path('api/course_books/<str:pk>/',views.course_books,name='course-books'),
    path('api/upload',views.upload_data,name='upload'),
]