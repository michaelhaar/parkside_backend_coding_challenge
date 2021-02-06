from django.test import TestCase, Client
from .models import Robot


class RobotTestCase(TestCase):
    def setUp(self):
        Robot.objects.create(
            id=2,
            name="Jammydevil",
            powermove="Hand Hops",
            experience=7,
            outOfOrder=False,
            avatar="https://robohash.org/jammydevil")
        Robot.objects.create(
            id=5,
            name="Fettboom",
            powermove="Air Flares",
            experience=5,
            outOfOrder=False,
            avatar="https://robohash.org/fettboom")
        self.client = Client()

    def test_receive_individual_robot(self):
        # Issue a GET request.
        response = self.client.get('/api/robots/2')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that content matches the expected data
        expected_data = {
            'id': 2,
            'name': 'Jammydevil',
            'powermove': 'Hand Hops',
            'experience': 7,
            'outOfOrder': False,
            'avatar': 'https://robohash.org/jammydevil'
        }
        self.assertJSONEqual(
            str(response.content, encoding='utf8'), expected_data)

    def test_receive_all_robots(self):
        # Issue a GET request.
        response = self.client.get('/api/robots')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that content matches the expected data
        expected_data = {
            "count": 2,
            "next": None,
            "previous": None,
            "results": [
                {
                    'id': 5,
                    'name': 'Fettboom',
                    'powermove': 'Air Flares',
                    'experience': 5,
                    'outOfOrder': False,
                    'avatar': 'https://robohash.org/fettboom'
                },
                {
                    'id': 2,
                    'name': 'Jammydevil',
                    'powermove': 'Hand Hops',
                    'experience': 7,
                    'outOfOrder': False,
                    'avatar': 'https://robohash.org/jammydevil'
                }
            ]
        }
        self.assertJSONEqual(
            str(response.content, encoding='utf8'), expected_data)
