from rest_framework import status
from rest_framework.test import APITestCase
from .models import Robot, DanceOff


def create_robots():
    Robot.objects.create(
        id=1,
        name='Jammydevil',
        powermove='Hand Hops',
        experience=7,
        outOfOrder=False,
        avatar='https://robohash.org/jammydevil')
    Robot.objects.create(
        id=2,
        name='Fettboom',
        powermove='Air Flares',
        experience=5,
        outOfOrder=False,
        avatar='https://robohash.org/fettboom')
    Robot.objects.create(
        id=3,
        name='FreakyFriday',
        powermove='Jackhammers',
        experience=3,
        outOfOrder=False,
        avatar='https://robohash.org/freakyfriday')


def create_danceoffs():
    DanceOff.objects.create(
        id=1,
        winner=Robot.objects.get(pk=1),
        loser=Robot.objects.get(pk=2),
    )
    DanceOff.objects.create(
        id=2,
        winner=Robot.objects.get(pk=3),
        loser=Robot.objects.get(pk=2),
    )


class GetRobotTestCase(APITestCase):
    def setUp(self):
        create_robots()

    def test_receive_robot(self):
        # Issue a GET request.
        response = self.client.get('/api/robots/1')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check that content matches the expected data
        expected_data = {
            'id': 1,
            'name': 'Jammydevil',
            'powermove': 'Hand Hops',
            'experience': 7,
            'outOfOrder': False,
            'avatar': 'https://robohash.org/jammydevil'
        }
        self.assertJSONEqual(
            str(response.content, encoding='utf8'), expected_data)

    def test_list_robots(self):
        # Issue a GET request.
        response = self.client.get('/api/robots')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check that content matches the expected data
        expected_data = {
            'count': 3,
            'next': None,
            'previous': None,
            'results': [
                {
                    'id': 3,
                    'name': 'FreakyFriday',
                    'powermove': 'Jackhammers',
                    'experience': 3,
                    'outOfOrder': False,
                    'avatar': 'https://robohash.org/freakyfriday'
                },
                {
                    'id': 2,
                    'name': 'Fettboom',
                    'powermove': 'Air Flares',
                    'experience': 5,
                    'outOfOrder': False,
                    'avatar': 'https://robohash.org/fettboom'
                },
                {
                    'id': 1,
                    'name': 'Jammydevil',
                    'powermove': 'Hand Hops',
                    'experience': 7,
                    'outOfOrder': False,
                    'avatar': 'https://robohash.org/jammydevil'
                },
            ]
        }
        self.assertEqual(response.data, expected_data)


class GetDanceOffTestCase(APITestCase):
    def setUp(self):
        create_robots()
        create_danceoffs()

    def test_list_danceoffs(self):
        # Issue a GET request.
        response = self.client.get('/api/danceoffs')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check that content matches the expected data
        expected_data = {
            'count': 2,
            'next': None,
            'previous': None,
            'results': [
                {
                    'id': 2,
                    'winner': 3,
                    'loser': 2,
                    'dancedAt': DanceOff.objects.get(pk=2).dancedAt.isoformat()
                },
                {
                    'id': 1,
                    'winner': 1,
                    'loser': 2,
                    'dancedAt': DanceOff.objects.get(pk=1).dancedAt.isoformat()
                }
            ]
        }
        self.assertEqual(response.data, expected_data)


class PostDanceOffTestCase(APITestCase):
    def setUp(self):
        create_robots()

    def assert_bad_danceoff_create_request(self, url, post_data):
        response = self.client.post(url, post_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_danceoff(self):
        url = '/api/danceoffs'
        post_data = {
            'winner': 1,
            'opponents': [1, 2]
        }
        response = self.client.post(url, post_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(DanceOff.objects.count(), 1)
        latest = DanceOff.objects.latest('id')
        self.assertEqual(latest.winner.id, 1)
        self.assertEqual(latest.loser.id, 2)

        post_data = {
            'winner': 3,    # winner is not in opponentens
            'opponents': [1, 2]
        }
        self.assert_bad_danceoff_create_request(url, post_data)

        post_data = {
            'winner': 1,
            'opponents': [1, 1]  # same opponentens
        }
        self.assert_bad_danceoff_create_request(url, post_data)

        post_data = {
            'winner': 1,
            'opponents': [1, 5]  # robot doesn't exist
        }
        self.assert_bad_danceoff_create_request(url, post_data)

        post_data = {
            'winner': 10,  # robot doesn't exist
            'opponents': [1, 2]
        }
        self.assert_bad_danceoff_create_request(url, post_data)

        post_data = {
            # winner missing
            'opponents': [1, 2]
        }
        self.assert_bad_danceoff_create_request(url, post_data)

        post_data = {
            'winner': 1,
            # opponents missing
        }
        self.assert_bad_danceoff_create_request(url, post_data)

        post_data = {
            'winner': "a",  # invalid data type
            'opponents': [1, 2]
        }
        self.assert_bad_danceoff_create_request(url, post_data)

        post_data = {
            'winner': 1,
            'opponents': ""  # invalid data type
        }
        self.assert_bad_danceoff_create_request(url, post_data)

        post_data = {
            'winner': 1,
            'opponents': [1]  # missing opponent
        }
        self.assert_bad_danceoff_create_request(url, post_data)

        post_data = {
            'winner': 1,
            'opponents': [1, 2, 3]  # too many opponents
        }
        self.assert_bad_danceoff_create_request(url, post_data)

    def test_bulkcreate_danceoff(self):
        url = '/api/danceoffs'
        post_data = [
            {  # gets inserted first
                'winner': 3,
                'opponents': [2, 3]
            },
            {
                'winner': 3,
                'opponents': [1, 3]
            },
            {
                'winner': 2,
                'opponents': [1, 2]
            },
        ]
        response = self.client.post(url, post_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(DanceOff.objects.count(), 3)
        last_two = DanceOff.objects.order_by('-id')[:3]
        self.assertEqual(last_two[0].winner.id, 2)
        self.assertEqual(last_two[0].loser.id, 1)
        self.assertEqual(last_two[1].winner.id, 3)
        self.assertEqual(last_two[1].loser.id, 1)
        self.assertEqual(last_two[2].winner.id, 3)
        self.assertEqual(last_two[2].loser.id, 2)

        post_data = [
            {
                'winner': 3,
                'opponents': [5, 3]  # robot doesn't exist
            },
            {
                'winner': 3,
                'opponents': [1, 3]
            },
        ]
        self.assert_bad_danceoff_create_request(url, post_data)
        self.assert_bad_danceoff_create_request(url, {"abc"})
        self.assert_bad_danceoff_create_request(url, ["a", "b", "c"])
