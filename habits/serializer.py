from rest_framework import serializers
from habits.models import Habit
from habits.validators import TimeCompleteValidator, BothValidator, RelatedPleasantValidator, PleasantValidator, \
    PeriodicityValidator


class HabitsSerializer(serializers.ModelSerializer):
    validators = [
        TimeCompleteValidator(field='time_to_complete'),
        BothValidator(field1='related_habit', field2='reward'),
        RelatedPleasantValidator(field1='related_habit', field2='is_pleasant_habit'),
        PleasantValidator(field1='is_pleasant_habit', field2='reward', field3='related_habit'),
        PeriodicityValidator(field='periodicity')
    ]

    class Meta:
        model = Habit
        fields = '__all__'
