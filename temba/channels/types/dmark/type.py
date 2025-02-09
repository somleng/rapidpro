from django.utils.translation import gettext_lazy as _

from temba.channels.types.dmark.views import ClaimView
from temba.contacts.models import URN

from ...models import ChannelType


class DMarkType(ChannelType):
    """
    A DMark Channel Type http://smsapi1.dmarkmobile.com/
    """

    code = "DK"
    category = ChannelType.Category.PHONE

    name = "DMark"

    courier_url = r"^dk/(?P<uuid>[a-z0-9\-]+)/(?P<action>receive|status)$"

    claim_blurb = _(
        "If you are based in Uganda or DRC you can purchase a short code from %(link)s and connect it in a few simple "
        "steps."
    ) % {"link": '<a target="_blank" href="http://dmarkmobile.com/">DMark Mobile</a>'}
    claim_view = ClaimView

    schemes = [URN.TEL_SCHEME]
    max_length = 459

    configuration_blurb = _(
        "To finish configuring your DMark channel you need to set DMark to send MO messages to the URL below."
    )

    configuration_urls = (
        dict(
            label=_("Receive URL"),
            url="https://{{ channel.callback_domain }}{% url 'courier.dk' channel.uuid 'receive' %}",
        ),
    )

    available_timezones = ["Africa/Kampala", "Africa/Kinshasa"]
