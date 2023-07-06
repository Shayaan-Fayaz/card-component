import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sosc_card.settings")
django.setup()

from card.models import Member


import requests
from bs4 import BeautifulSoup

URL="https://www.sosc.org.in/team/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find_all("div", class_="team-section")
required_result = results[1]
team_members = required_result.find_all("a", class_="card-link")

for member in team_members:
    member_github = member.get("href")
    memeber_photo_link = member.find("img", class_="profile-pic")["src"]
    member_name = member.find("h3").text
    member_designation = member.find("p").text
    memebers_data = Member(name=member_name, roles=member_designation, img=memeber_photo_link, github_link=member_github)
    memebers_data.save()