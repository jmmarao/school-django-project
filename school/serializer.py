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