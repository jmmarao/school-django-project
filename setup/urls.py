from django.contrib import admin
from django.urls import path, include
from school.views import StudentsViewSet, CoursesViewSet, EnrollmentViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('students', StudentsViewSet, basename='Students')
router.register('courses', CoursesViewSet, basename='Courses')
router.register('enrollments', EnrollmentViewSet, basename='Enrollments')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
