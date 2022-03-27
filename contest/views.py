from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Contest
from .serializers import ContestSerializer

# Create your views here.
@api_view(['GET'])
def contestList(request):
    contests = Contest.objects.all()
    serializer = ContestSerializer(contests, many=True)
    return Response(serializer.data)