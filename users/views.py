#Genric
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework import generics, status
import datetime
from .serializers import LoginSerializer
from .models import User


class Login(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        try:
            serializer = self.serializer_class(data = request.data)
            serializer.is_valid(raise_exception = True)
            
            user = User.objects.get(email = request.data['email'])
        
            userData = User.objects.filter(email = serializer.data['email']).values('id', 'email', 'is_active', 'is_staff', 'is_superuser')
            print(userData)
            return Response({'result' : serializer.data, 'userData' : userData, 'code' : status.HTTP_200_OK, 'status' : status.HTTP_200_OK}) 
        
        except Exception:
            raise AuthenticationFailed("Invalid credentials. Try Again...")
