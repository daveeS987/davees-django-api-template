from django.test import TestCase

# for some reason, we have to use get_user_model and not settings.AUTH_USER_MODEL
from django.contrib.auth import get_user_model
from .models import Example1


class Example1Test(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(email="test@gmail.com", password="pass")
        testuser1.save()
        test_example1 = Example1.objects.create(
            author=testuser1, title="Green Eggs and Ham", body="I do not like green eggs and ham, Sam I  am."
        )
        test_example1.save()

    def test_blog_content(self):
        example1 = Example1.objects.get(id=1)
        self.assertEqual(str(example1.author), "test@gmail.com")
        self.assertEqual(str(example1.title), "Green Eggs and Ham")
        self.assertEqual(str(example1.body), "I do not like green eggs and ham, Sam I  am.")
