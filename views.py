from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from .models import Post, Account, Analytics
from .serializers import PostSerializer, AccountSerializer, AnalyticsSerializer

User = get_user_model()


class PostViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing social media posts
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user)

    @action(detail=True, methods=['post'])
    def schedule(self, request, pk=None):
        """Schedule a post for later publishing"""
        post = self.get_object()
        scheduled_time = request.data.get('scheduled_time')
        # Scheduling logic here
        return Response({'message': 'Post scheduled successfully'})


class AccountViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing social media accounts
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Account.objects.filter(user=self.request.user)

    @action(detail=True, methods=['post'])
    def connect(self, request, pk=None):
        """Connect a social media account"""
        account = self.get_object()
        # OAuth connection logic here
        return Response({'message': 'Account connected successfully'})


class AnalyticsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for viewing analytics data
    """
    queryset = Analytics.objects.all()
    serializer_class = AnalyticsSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'])
    def overview(self, request):
        """Get analytics overview"""
        # Analytics calculation logic
        data = {
            'total_posts': 0,
            'total_engagement': 0,
            'follower_growth': 0,
            'best_posting_times': []
        }
        return Response(data)

