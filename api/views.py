from django.contrib.auth.models import User

from .models import Column, Card
from .serializers import UserSerializer, ColumnSerializer, CardSerializer
from .permissions import IsAuthorOrReadOnly

from rest_framework import viewsets, permissions




# Users
class UsersList(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]






# Cards
class CardsList(viewsets.ModelViewSet):
    queryset = Card.objects.all().order_by('modified_at')
    serializer_class = CardSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]





# Columns
class ColumnsList(viewsets.ModelViewSet):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]