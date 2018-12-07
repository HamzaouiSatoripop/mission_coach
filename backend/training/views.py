from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import TrainingSerializer
from .models import Training

# Create your views here.
class TrainingViewSet(viewsets.ModelViewSet):
    serializer_class = TrainingSerializer
    def get_queryset(self):
        return Training.objects.filter(trainee=self.request.user)
    queryset = Training.objects.all()
    permission_classes = [IsAuthenticated]

