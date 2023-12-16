import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_prime_video_url(value):
    regex = re.compile(r'https:\/\/www.amazon.co.jp\/gp\/video\/detail\/.+')
    if regex.match(value) is None:
        raise ValidationError(
            _("%(value)s は AmazonPrimeVideo の URL ではありません。"),
            params={"value": value},
        )
