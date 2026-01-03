from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model, authenticate
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer

class IsUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj == request.user

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

from drf_yasg.utils import swagger_auto_schema

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, IsUserOrReadOnly]

    @swagger_auto_schema(operation_description="Delete a user account")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()

    def post(self, request, pk):
        user_to_follow = get_object_or_404(User, pk=pk)
        if request.user == user_to_follow:
            return Response({"error": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        
        if request.user.following.filter(pk=user_to_follow.pk).exists():
             return Response({"message": "You are already following this user."}, status=status.HTTP_400_BAD_REQUEST)

        request.user.following.add(user_to_follow)
        return Response({"message": f"You are now following {user_to_follow.username}"}, status=status.HTTP_200_OK)

class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()

    def post(self, request, pk):
        user_to_unfollow = get_object_or_404(User, pk=pk)
        if not request.user.following.filter(pk=user_to_unfollow.pk).exists():
            return Response({"message": "You are not following this user."}, status=status.HTTP_400_BAD_REQUEST)

        request.user.following.remove(user_to_unfollow)
        return Response({"message": f"You have unfollowed {user_to_unfollow.username}"}, status=status.HTTP_200_OK)

from rest_framework.authtoken.views import ObtainAuthToken

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data,
                                               context={'request': request})
            if not serializer.is_valid():
                return Response({
                    'message': 'Wrong credentials.',
                    'success': False,
                    'errors': serializer.errors,
                    'errorcode': status.HTTP_400_BAD_REQUEST
                }, status=status.HTTP_400_BAD_REQUEST)
            
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user_id': user.pk,
                'message': 'Login successful',
                'success': True,
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            error_code = getattr(e, 'status_code', status.HTTP_500_INTERNAL_SERVER_ERROR)
            return Response({
                'message': 'An unexpected error occurred.',
                'success': False,
                'details': str(e),
                'errorcode': error_code
            }, status=error_code)
