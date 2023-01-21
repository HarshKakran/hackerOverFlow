from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.db import transaction, connection
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import ValidationError
from rest_framework import generics

from rest_framework.permissions import IsAuthenticated

from .models import Resume
from .serializers import UserSerializer, RegisterSerializer, ResumeSerializer

# Class based view to Get User Details using Token Authentication
class UserDetailAPI(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        # user = User.objects.get(id=request.user.id)
        print(request.user.id)
        serializer = UserSerializer(request.user.id)
        return Response(serializer.data)


# Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class ResumeListCreateView(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )
    lookup_field = 'pk'

    def get(self, request):
        qs = Resume.objects.filter(user=request.user.id)
        return Response(ResumeSerializer(qs, many=True).data)

    def post(self, request):
        data = request.data.copy()
        data['user'] = request.user.id
        print(data, '\n\n')
        s = ResumeSerializer(data=data)
        try:
            if s.is_valid():
                with transaction.atomic():
                    s.save()
                return Response(s.data)
            return Response(s.errors)
        except ValidationError as e:
            return Response({'error': e.detail})
