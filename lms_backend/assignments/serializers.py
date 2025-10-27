from rest_framework import serializers
from .models import Assignment, Submission

class AssignmentSerializer(serializers.ModelSerializer):
    course_title = serializers.CharField(source='course.title', read_only=True)
    
    class Meta:
        model = Assignment
        fields = ['id', 'course', 'course_title', 'title', 'description', 
                  'due_date', 'max_marks', 'created_at']
        read_only_fields = ['created_at']

class SubmissionSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student.username', read_only=True)
    assignment_title = serializers.CharField(source='assignment.title', read_only=True)
    
    class Meta:
        model = Submission
        fields = ['id', 'assignment', 'assignment_title', 'student', 'student_name',
                  'submitted_file', 'submitted_at', 'marks_obtained', 'feedback']
        read_only_fields = ['submitted_at']
