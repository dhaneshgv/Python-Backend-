# from . import views 
# from django.contrib import admin
# from django.urls import path



# urlpatterns = [
    
#     path('admin/', admin.site.urls),
#     #path('', views.index),  # Add a path for the root URL
#     path('student/', views.studentApi),
#     path('student/<int:pk>/', views.studentApi),
#     #path('content/',views.content)
# ]



# from django.contrib import admin
# from django.urls import path
# from django.conf.urls import url
# from student import views

# urlpatterns = [
#     url(r'^student$',views.studentApi),
#     url(r'^student$',views.studentApi),
#     url(r'^student/([0-9]+)$',views.studentApi),
#     path('admin/', admin.site.urls),
# ]

from django.contrib import admin
from django.urls import path
from student import views

urlpatterns = [
    path('student/', views.studentApi, name='student-list-create'),
    path('student/<int:pk>/', views.studentApi, name='student-detail'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
]
