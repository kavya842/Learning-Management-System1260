from rest_framework import serializers
from .models import Course, Enrollment
from django.contrib.auth.models import User

class CourseSerializer(serializers.ModelSerializer):
    teacher_name = serializers.CharField(source='teacher.username', read_only=True)
    
    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'teacher', 'teacher_name', 
                  'students', 'created_at', 'updated_at', 'is_active']
        read_only_fields = ['created_at', 'updated_at']

class EnrollmentSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student.username', read_only=True)
    course_title = serializers.CharField(source='course.title', read_only=True)
    
    class Meta:
        model = Enrollment
        fields = ['id', 'student', 'student_name', 'course', 'course_title', 
                  'enrolled_date', 'progress']
        read_only_fields = ['enrolled_date']
