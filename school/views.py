from rest_framework import viewsets, generics
from school.models import Student, Course, Enrollment
from school.serializer import SerializerStudent, SerializerCourse, SerializerEnrollment, SerializerStudentEnrollmentList, SerializerStudentsEnrolledList

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

class StudentEnrollmentList(generics.ListAPIView):
    """Show all students enrollments"""
    def get_queryset(self):
        queryset = Enrollment.objects.filter(student_id=self.kwargs['pk'])
        return queryset
    serializer_class = SerializerStudentEnrollmentList

class StudentEnrolledList(generics.ListAPIView):
    """Show all students enrolleds in courses"""
    def get_queryset(self):
        queryset = Enrollment.objects.filter(course_id=self.kwargs['pk'])
        return queryset
    serializer_class = SerializerStudentsEnrolledList