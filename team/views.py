from rest_framework.response import Response
from rest_framework import generics, status
from .serializers import TeamSerializer
from team.models import Team


# Create your views here.
class TeamCreate(generics.GenericAPIView):
    serializer_class = TeamSerializer

    def post(self, request):
        team_name = request.data.get(
            'team_name', Team._meta.get_field('team_name').get_default())
        score = request.data.get(
            'score', Team._meta.get_field('score').get_default())
        users = request.data.get('users')
        team = Team.objects.create(
            team_name=team_name,
            score=score
        )
        team.users.add(*users)
        serializer = TeamSerializer(team)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
