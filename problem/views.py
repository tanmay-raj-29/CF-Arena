from django.test import tag
from rest_framework.response import Response
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import Problem, Tag
from .serializers import ProblemSerializer


# Create your views here.
class ProblemList(generics.GenericAPIView):
    serializer_class = ProblemSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['rating', 'solve_count', 'contest_id']

    def get_queryset(self):
        queryset = Problem.objects.all()
        queryset = self.filter_queryset(queryset)
        query_params = self.request.query_params
        if query_params.get('tag'):
            tags = query_params.getlist('tag')
            queryset = queryset.filter(tags__name__in=tags)
        if query_params.get('min_rating') and query_params.get('max_rating'):
            min_rating = query_params.get('min_rating')
            max_rating = query_params.get('max_rating')
            queryset = queryset.filter(rating__range=[min_rating, max_rating])
        if query_params.get('min_solve_count') and query_params.get('max_solve_count'):
            min_solve_count = query_params.get('min_solve_count')
            max_solve_count = query_params.get('max_solve_count')
            queryset = queryset.filter(solve_count__range=[min_solve_count, max_solve_count])
        if query_params.get('min_contest_id') and query_params.get('max_contest_id'):
            min_contest_id = query_params.get('min_contest_id')
            max_contest_id = query_params.get('max_contest_id')
            queryset = queryset.filter(contest_id__range=[min_contest_id, max_contest_id])
        return queryset

    def get(self, request):
        problems = ProblemSerializer(self.get_queryset(), many=True).data
        return Response(problems)
