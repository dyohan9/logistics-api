from django.test import TestCase

from core.authentication.models import User
from core.common.models import Map


class MapCreateTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user("fake@user.com", "123456")
        self.map = Map.objects.create(user=user, map_name="test")

    def test_map_ok(self):
        self.assertEqual(self.map.map_name, "test")
