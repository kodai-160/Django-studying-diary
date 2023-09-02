from django.http import HttpRequest
from django.test import TestCase
from snippets.views import top  # これから実装するビュー (このコードを書き始めた時点ではまだ存在しない)


# Create your tests here.

class TopPageViewTest(TestCase):

    def test_top_returns_200(self):
        request = HttpRequest()
        response = top(request)
        self.assertEqual(response.status_code, 200)

    def test_top_returns_expected_content(self):
        pass
        request = HttpRequest()
        response = top(request)
        self.assertEqual(response.content, b"Hello World")
