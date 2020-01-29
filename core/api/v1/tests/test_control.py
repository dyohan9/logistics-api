from django.test import RequestFactory
from django.test import TestCase

from core.api.v1.control.tasks import map_create
from core.authentication.models import User
from core.common.models import Map, Router


class AddMapTaskTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

        self.password = "abcgq!!123"
        self.email = "user@user.com"

        user = User.objects.create(email=self.email, name="User")
        user.set_password(self.password)
        user.save(update_fields=["password"])

        self.map = Map.objects.create(map_name="test", user=user)
        self.mapcreate = map_create(
            self.map.pk, ["A B 10", "B D 15", "A C 20", "C D 30", "B E 50", "D E 30"]
        )

    def test_ok(self):
        routers = Router.objects.filter(map=self.map)

        self.assertEqual(routers.first().source, "A")
        self.assertEqual(routers.first().destiny, "B")
        self.assertEqual(routers.first().distance, 10)
