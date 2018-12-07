from rest_framework  import routers

from training.views import TrainingViewSet

training_router=routers.DefaultRouter()
training_router.register('',TrainingViewSet)
