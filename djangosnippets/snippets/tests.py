from django.test import TestCase


# Create your tests here.

# トップページがb"Hello Wrold"というプレーンテキストではなくhtmlファイルを返すように変更するため、
# TopPageViewTestクラスは削除して、TopPageTestクラスを次んように書き換え

class TopPageTest(TestCase):
    def test_top_page_returns_200_and_expected_title(self):
        response = self.client.get("/")
        self.assertContains(response, "Djangoスニペット", status_code=200)

    def test_top_page_uses_expected_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "snippets/top.html")
