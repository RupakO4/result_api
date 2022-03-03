from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ExamSerializer, ResultSerializer
from .models import Exam , Result


# Create your views here.
@api_view(['GET'])
def getRoutes(request):

    routes = [
        {
            'Endpoint': '/exams/',
            'Method': 'GET',
            'Description': 'Get all exams'
        },
        {
            'Endpoint': '/exam_id/student_id',
            'Method': 'GET',
            'Description': 'Get all results of specific year'
        }
    ]
    return Response(routes)

@api_view(['GET'])
def getExam(request):
    results = Exam.objects.all()
    serializer = ExamSerializer(results, many=True)
    return Response(serializer.data)

# @api_view(['GET'])
# def getYearResults(request,pk):
#     yearResults = Results.pk.all()
#     serializer = ResultsSerializer(yearResults, many=True)
#     return Response(serializer.data)

@api_view(['GET'])
def getResult(request,pk1 ,pk2):
    exam = Result.objects.filter(exam_id__exam_id=pk1)
    results = exam.get(student_id=pk2)
    #query = self.request.GET.get('search')
    #if query is not None:
        #results = results.filter(result_id__results_id=pk, passed_id__icontains=query)
    serializer = ResultSerializer(results)
    return Response(serializer.data)
