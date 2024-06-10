from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from users.models import User
from habits.models import Habit


class HabitsTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            email='test@mail.com',
            password='123456',
        )
        self.client.force_authenticate(user=self.user)

        self.habit = Habit.objects.create(
            owner=self.user,
            place='дома',
            time="19:00:00",
            action='Прочитать книгу',
            is_pleasant=False,
            related_habit=None,
            period=3,
            reward='Приготовить десерт',
            duration=60,
            is_public=True
        )

    def test_create_habit(self):
        """ Тестирование на создание полезной привычки"""

        data = {
            "owner": self.user.id,
            "place": 'дома',
            "time": "19:00:00",
            "action": 'Прочитать книгу',
            "is_pleasant": False,
            "related_habit": "",
            "period": 3,
            "reward": "Приготовить десерт",
            "duration": 60,
            "is_public": True
        }
        response = self.client.post(
            '/habits/create/', data=data
        )
        print('RESPONSE', response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Habit.objects.all().exists())

    def test_list_habit(self):
        """Тестирование на вывод списка полезных привычек"""
        response = self.client.get(
            '/habits/'
        )
        print('RESPONSE', response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"count": 1, "next": None, "previous": None, "results": [
            {'id': self.habit.id, 'place': 'дома', 'time': '19:00:00', 'action': 'Прочитать книгу',
             'is_pleasant': False, 'period': 3, 'reward': 'Приготовить десерт',
             'duration': 60, 'is_public': True, 'owner': self.user.pk, 'related_habit': None}
        ]}
                         )

    def test_detail_habit(self):
        """Тестирование на вывод одной привычки"""
        data = {
            "owner": self.user.id,
            "place": 'дома',
            "time": "19:00:00",
            "action": 'Прочитать книгу',
            "is_pleasant": False,
            "related_habit": "",
            "period": 3,
            "reward": "Приготовить десерт",
            "duration": 60,
            "is_public": True
        }
        response = self.client.get(
            f'/habits/view/{self.habit.id}',
            data=data
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_habit(self):
        """Тестирование на обновление или изменения привычки"""
        data = {
            "owner": self.user.id,
            "place": 'Улица',
            "time": "20:00:00",
            "action": 'Пройти пешком 2 км',
            "is_pleasant": True,
            "related_habit": "",
            "period": 3,
            "reward": "",
            "duration": 90,
            "is_public": False
        }
        response = self.client.patch(
            f'/habits/edit/{self.habit.id}',
            data=data
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.habit.refresh_from_db()
        self.assertEqual(self.habit.place, data["place"])
        self.assertEqual(self.habit.action, data["action"])

    def test_delete_habit(self):
        """Тестирование на удаление привычки"""
        data = {
            "owner": self.user.id,
            "place": 'Улица',
            "time": "20:00:00",
            "action": 'Пройти пешком 2 км',
            "is_pleasant": True,
            "related_habit": "",
            "period": 3,
            "reward": "",
            "duration": 90,
            "is_public": False
        }
        response = self.client.delete(
            f'/habits/delete/{self.habit.id}',
            data=data
        )
        print('RESPONSE', response.content)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
