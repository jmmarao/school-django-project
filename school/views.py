from rest_framework import viewsets
from school.models import Student, Course, Enrollment
from school.serializer import SerializerStudent, SerializerCourse, SerializerEnrollment

class StudentsViewSet(viewsets.ModelViewSet):
    """Show all students"""
    queryset = Student.objects.all()
    serializer_class = SerializerStudent

class CoursesViewSet(viewsets.ModelViewSet):
    """Show all courses"""
    queryset = Course.objects.all()
    serializer_class = SerializerCourse

class EnrollmentViewSet(viewsets.ModelViewSet):
    """Show all enrollments"""
    queryset = Enrollment.objects.all()
    serializer_class = SerializerEnrollment