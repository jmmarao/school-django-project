from rest_framework import serializers
from school.models import Student, Course, Enrollment

class SerializerStudent(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'rg', 'cpf', 'birth_date']

class SerializerCourse(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class SerializerEnrollment(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        exclude = []

class SerializerStudentEnrollmentList(serializers.ModelSerializer):
    course = serializers.ReadOnlyField(source='course.description')
    period = serializers.SerializerMethodField()
    class Meta:
        model = Enrollment
        fields = ['course', 'period']
    def get_period(self, obj):
        return obj.get_period_display()
    
class SerializerStudentsEnrolledList(serializers.ModelSerializer):
    student_name = serializers.ReadOnlyField(source='student.name')
    class Meta:
        model = Enrollment
        fields = ['student_name']