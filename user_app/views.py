from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from user_app import signals
# from user_app import models
from rest_framework.authtoken.models import Token
from user_app.serializers import RegistrationSerializer


# Create your views here.

@api_view(['POST'])
def registration(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'registration successfully completed'
            data['username'] = account.username
            data['email'] = account.email

            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)



@api_view(['POST'])
def logout_view(request):
    if request.method == 'POST':
        if request.user.is_authenticated:  # Check if the user is authenticated
            # Delete the user's auth token if it exists
            try:
                request.user.auth_token.delete()
            except AttributeError:
                pass  # If the user doesn't have an auth token, do nothing
            return Response({'message': 'Successfully logged out'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'You are not logged in'}, status=status.HTTP_401_UNAUTHORIZED)
