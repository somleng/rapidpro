from django.utils.translation import gettext_lazy as _

from temba.channels.types.clickatell.views import ClaimView
from temba.contacts.models import URN

from ...models import ChannelType


class ClickatellType(ChannelType):
    """
    A Clickatell channel (https://clickatell.com/)
    """

    code = "CT"
    category = ChannelType.Category.PHONE

    courier_url = r"^ct/(?P<uuid>[a-z0-9\-]+)/(?P<action>status|receive)$"

    name = "Clickatell"

    claim_blurb = _(
        "Connect your %(link)s number, we'll walk you through the steps necessary to get your Clickatell connection "
        "working in a few minutes."
    ) % {"link": '<a target="_blank" href="http://clickatell.com/">Clickatell</a>'}
    claim_view = ClaimView

    schemes = [URN.TEL_SCHEME]
    max_length = 420

    configuration_blurb = _(
        "To finish configuring your Clickatell connection you'll need to set the following callback URLs on the "
        "Clickatell website for your integration."
    )

    configuration_urls = (
        dict(
            label=_("Reply Callback"),
            url="https://{{ channel.callback_domain }}{% url 'courier.ct' channel.uuid 'receive' %}",
            description=_(
                "You can set the callback URL on your Clickatell account by managing your integration, "
                """then setting your reply callback under "Two Way Settings" to HTTP POST and your target address """
                "to the URL below. (leave username and password blank)"
            ),
        ),
        dict(
            label=_("Delivery Notifications"),
            url="https://{{ channel.callback_domain }}{% url 'courier.ct' channel.uuid 'status' %}",
            description=_(
                "You can set the delivery notification URL on your Clickatell account by managing your "
                """integration, then setting your delivery notification URL under "Settings" to HTTP POST and your """
                "target address to the URL below. (leave username and password blank)"
            ),
        ),
    )
