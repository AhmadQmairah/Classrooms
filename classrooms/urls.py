
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from classes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('classrooms/', views.classroom_list, name='classroom-list'),
    path('classrooms/<int:classroom_id>/', views.classroom_detail, name='classroom-detail'),
    path('SignUp/', views.SignUp, name='SignUp'),
    path('LogIn/', views.LogIn, name='LogIn'),
    path('LogOut/',views.LogOut	, name='LogOut'),
    path('classrooms/create', views.classroom_create, name='classroom-create'),
    path('classrooms/<int:classroom_id>/update/', views.classroom_update, name='classroom-update'),
    path('classrooms/<int:classroom_id>/delete/', views.classroom_delete, name='classroom-delete'),
    path('classrooms/<int:classroom_id>/student/Add/', views.StudentADD, name='Student-ADD'),
    path('classrooms/<int:student_id>/student/update', views.StudentUpdate, name='student-update'),
    path('classrooms/<int:student_id>/student/delete', views.Studentdelete, name='student-delete'),
]

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
