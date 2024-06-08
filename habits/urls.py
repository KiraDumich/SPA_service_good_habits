from habits.apps import HabitsConfig
from django.urls import path
from habits.views import HabitsDestroyAPIView, HabitsUpdateAPIView, HabitsListAPIView, HabitsCreateAPIView, HabitsRetrieveAPIView

app_name = HabitsConfig.name

urlpatterns = [
    path('create', HabitsCreateAPIView.as_view(), name='habit_create'),
    path('', HabitsListAPIView.as_view(), name='habits_list'),
    path('view/<int:pk>', HabitsRetrieveAPIView.as_view(), name='habit_view'),
    path('edit/<int:pk>', HabitsUpdateAPIView.as_view(), name='habit_edit'),
    path('delete/<int:pk>',HabitsDestroyAPIView.as_view(), name='habit_delete'),
]