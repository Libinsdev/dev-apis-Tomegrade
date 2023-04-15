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
    path('api/addtocart/',views.addtocart,name='addtocart'),
    path('api/getcartitems/',views.getcartitems,name='getcartitems'),
    path('api/inccartcount/<str:pk>/',views.incitem,name='inccartitem'),
    path('api/deccount/<str:pk>/',views.deccount,name='deccount'),
    path('api/removeitem/<str:pk>/',views.removeitem,name='removeitem'),
    path('api/cart_subtotal/',views.subtotal,name='cart_subtotal'),
    path('api/bundleadded/',views.addbundlecart,name='addbundlecart'),
    path('api/bundleremove/<int:pk>/',views.bundlebookremove,name='bundleremove'),
    path('api/checkoutdetails/',views.checkoutdetails,name='checkoutdetails'),
    
]
