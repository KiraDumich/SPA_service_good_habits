from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from habits.serializer import HabitsSerializer
from habits.models import Habit
from habits.permissions import Owner, IsAdminUser
from habits.pagination import HabitsPaginator


class HabitsCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitsSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsAuthenticated, Owner, IsAdminUser,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class HabitsListAPIView(generics.ListAPIView):
    serializer_class = HabitsSerializer
    permission_classes = [IsAdminUser]
    pagination_class = HabitsPaginator

    def get_queryset(self):
        user = self.request.user
        if not user.is_superuser:
            queryset = Habit.objects.filter(owner=user)
        else:
            queryset = Habit.objects.all()
        return queryset


class HabitsRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = HabitsSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsAuthenticated, Owner, IsAdminUser, )


class HabitsUpdateAPIView(generics.UpdateAPIView):
    serializer_class = HabitsSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsAuthenticated, Owner, IsAdminUser, )


class HabitsDestroyAPIView(generics.DestroyAPIView):
    queryset = Habit.objects.all()
    permission_classes = (IsAuthenticated, Owner, IsAdminUser, )



