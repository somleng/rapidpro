from unittest.mock import patch

from django.urls import reverse

from temba.tests import TembaTest

from ...models import Channel


class JunebugTypeTest(TembaTest):
    @patch("socket.gethostbyname", return_value="123.123.123.123")
    def test_claim(self, mock_socket_hostname):
        Channel.objects.all().delete()
        self.login(self.admin)

        url = reverse("channels.types.junebug.claim")

        # check that claim page URL appears on claim list page
        response = self.client.get(reverse("channels.channel_claim"))
        self.assertContains(response, url)

        response = self.client.get(url)
        self.assertEqual(200, response.status_code)

        post_data = {
            "country": "ZA",
            "number": "+273454325324",
            "url": "http://nyaruka.com/messages.json",
            "username": "foo",
            "password": "bar",
        }

        response = self.client.post(url, post_data)

        channel = Channel.objects.get()

        self.assertEqual(channel.country, post_data["country"])
        self.assertEqual(channel.address, post_data["number"])
        self.assertEqual(channel.config["send_url"], post_data["url"])
        self.assertEqual(channel.config["username"], post_data["username"])
        self.assertEqual(channel.config["password"], post_data["password"])
        self.assertEqual(channel.channel_type, "JN")
        self.assertEqual(channel.role, Channel.DEFAULT_ROLE)

        config_url = reverse("channels.channel_configuration", args=[channel.uuid])
        self.assertRedirect(response, config_url)

        response = self.client.get(config_url)
        self.assertEqual(200, response.status_code)

        self.assertContains(response, reverse("courier.jn", args=[channel.uuid, "inbound"]))

        Channel.objects.all().delete()
        self.login(self.admin)

        response = self.client.get(url)
        self.assertEqual(200, response.status_code)

        post_data = {
            "country": "ZA",
            "number": "+273454325324",
            "url": "http://nyaruka.com/messages.json",
            "username": "foo",
            "password": "bar",
            "secret": "UjOq8ATo2PDS6L08t6vlqSoK",
        }

        response = self.client.post(url, post_data)

        channel = Channel.objects.get()

        self.assertEqual(channel.country, post_data["country"])
        self.assertEqual(channel.address, post_data["number"])
        self.assertEqual(channel.config["secret"], post_data["secret"])
        self.assertEqual(channel.config["send_url"], post_data["url"])
        self.assertEqual(channel.config["username"], post_data["username"])
        self.assertEqual(channel.config["password"], post_data["password"])
        self.assertEqual(channel.channel_type, "JN")
        self.assertEqual(channel.role, Channel.DEFAULT_ROLE)

        config_url = reverse("channels.channel_configuration", args=[channel.uuid])
        self.assertRedirect(response, config_url)

        response = self.client.get(config_url)
        self.assertEqual(200, response.status_code)

        self.assertContains(response, reverse("courier.jn", args=[channel.uuid, "inbound"]))
