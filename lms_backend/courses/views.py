from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Course, Enrollment
from .serializers import CourseSerializer, EnrollmentSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [AllowAny]

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [AllowAny]

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def enroll_course(request, course_id):
    try:
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        return Response({"error": "Course not found."}, status=404)
    enrollment_exists = Enrollment.objects.filter(user=request.user, course=course).exists()
    if enrollment_exists:
        return Response({"message": "Already enrolled in this course."})
    Enrollment.objects.create(user=request.user, course=course)
    return Response({"message": "Enrollment successful!"})
