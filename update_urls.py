import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sosc_card.settings")
django.setup()


from urllib.parse import urlparse, urlunparse, parse_qs, urlencode
from django.core.management.base import BaseCommand
from card.models import Member


members = Member.objects.all()

for member in members:
    url_parts = list(urlparse(member.img))
    query_params = parse_qs(url_parts[4])

    query_params['size'] = ['500']

    url_parts[4] = urlencode(query_params, doseq=True)

    modified_url = urlunparse(url_parts)

    member.img = modified_url
    member.save()