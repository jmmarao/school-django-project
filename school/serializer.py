from rest_framework import serializers
from school.models import Student, Course

class SerializerStudent(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'rg', 'cpf', 'birth_date']

class SerializerCourse(serializers.ModelSerializer):
    class Meta:
        model = Coursefields = '__all__'