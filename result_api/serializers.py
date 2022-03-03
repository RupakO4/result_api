from rest_framework.serializers import ModelSerializer
from .models import Exam , Result

class ExamSerializer(ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'

class ResultSerializer(ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'
