from django.utils.translation import gettext_lazy as _

from temba.channels.views import AuthenticatedExternalClaimView
from temba.contacts.models import URN

from ...models import ChannelType


class MbloxType(ChannelType):
    """
    A Mblox channel (https://www.mblox.com/)
    """

    code = "MB"
    category = ChannelType.Category.PHONE

    courier_url = r"^mb/(?P<uuid>[a-z0-9\-]+)/(?P<action>receive)$"

    name = "Mblox"

    claim_blurb = _("Easily add a two way number you have configured with %(link)s using their APIs.") % {
        "link": '<a target="_blank" href="https://www.mblox.com/">Mblox</a>'
    }

    claim_view = AuthenticatedExternalClaimView

    schemes = [URN.TEL_SCHEME]
    max_length = 459

    configuration_blurb = _("As a last step you'll need to set the following callback URL on your Mblox account.")

    configuration_urls = (
        dict(
            label=_("Callback URL"),
            url="https://{{ channel.callback_domain }}{% url 'courier.mb' channel.uuid 'receive' %}",
            description=_(
                "This endpoint will be called by Mblox when new messages are received to your number and for delivery "
                "reports."
            ),
        ),
    )
