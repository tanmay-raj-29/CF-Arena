from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Problem
from .serializers import ProblemSerializer

# Create your views here.
@api_view(['GET'])
def problemList(request):
    problems = Problem.objects.all()
    print(problems)
    serializer = ProblemSerializer(problems, many=True)
    print(serializer)
    return Response(serializer.data)