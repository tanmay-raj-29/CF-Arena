from rest_framework.response import Response
from rest_framework import generics, status
from .serializers import MatchSerializer
from .models import Match
from team.models import Team


# Create your views here.
class MatchCreate(generics.GenericAPIView):
    serializer_class = MatchSerializer

    def post(self, request):
        match_name = request.data.get('match_name')
        team1 = Team.objects.get(id=request.data.get('first_team_id'))
        team2 = Team.objects.get(id=request.data.get('second_team_id'))
        problems = request.data.get('problem_ids')
        match = Match.objects.create(
            match_name=match_name,
            team1=team1,
            team2=team2,
            duration=request.data.get(
                'duration', Match._meta.get_field('duration').get_default())
        )
        match.problems.add(*problems)
        serializer = MatchSerializer(match)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
