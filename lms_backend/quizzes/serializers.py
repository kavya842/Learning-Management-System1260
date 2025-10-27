from rest_framework import serializers
from .models import Quiz, Question, QuizAttempt

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'quiz', 'question_text', 'marks']

class QuizSerializer(serializers.ModelSerializer):
    course_title = serializers.CharField(source='course.title', read_only=True)
    questions = QuestionSerializer(many=True, read_only=True)
    
    class Meta:
        model = Quiz
        fields = ['id', 'course', 'course_title', 'title', 'description', 
                  'duration_minutes', 'total_marks', 'created_at', 'questions']
        read_only_fields = ['created_at']

class QuizAttemptSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student.username', read_only=True)
    quiz_title = serializers.CharField(source='quiz.title', read_only=True)
    
    class Meta:
        model = QuizAttempt
        fields = ['id', 'quiz', 'quiz_title', 'student', 'student_name', 
                  'score', 'attempted_at']
        read_only_fields = ['attempted_at']
