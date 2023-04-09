from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from school.models import Student, Course, Enrollment
from school.serializer import SerializerStudent, SerializerCourse, SerializerEnrollment, SerializerStudentEnrollmentList, SerializerStudentsEnrolledList

class StudentsViewSet(viewsets.ModelViewSet):
    """Show all students"""
    queryset = Student.objects.all()
    serializer_class = SerializerStudent
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class CoursesViewSet(viewsets.ModelViewSet):
    """Show all courses"""
    queryset = Course.objects.all()
    serializer_class = SerializerCourse
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class EnrollmentViewSet(viewsets.ModelViewSet):
    """Show all enrollments"""
    queryset = Enrollment.objects.all()
    serializer_class = SerializerEnrollment
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class StudentEnrollmentList(generics.ListAPIView):
    """Show all students enrollments"""
    def get_queryset(self):
        queryset = Enrollment.objects.filter(student_id=self.kwargs['pk'])
        return queryset
    serializer_class = SerializerStudentEnrollmentList
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class StudentEnrolledList(generics.ListAPIView):
    """Show all students enrolleds in courses"""
    def get_queryset(self):
        queryset = Enrollment.objects.filter(course_id=self.kwargs['pk'])
        return queryset
    serializer_class = SerializerStudentsEnrolledList
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]