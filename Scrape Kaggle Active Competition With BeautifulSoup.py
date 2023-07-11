# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 22:59:11 2023

@author: NDU-PC
"""

import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import re


def get_remaining_time(time_str):
    if "month" in time_str:
        months = int(re.findall(r"\d+", time_str)[0])
        return datetime.now() + timedelta(days=months * 30)
    elif "day" in time_str:
        days = int(re.findall(r"\d+", time_str)[0])
        return datetime.now() + timedelta(days=days)
    elif "hour" in time_str:
        hours = int(re.findall(r"\d+", time_str)[0])
        return datetime.now() + timedelta(hours=hours)
    elif "minute" in time_str:
        minutes = int(re.findall(r"\d+", time_str)[0])
        return datetime.now() + timedelta(minutes=minutes)
    else:
        return None


url = "https://www.kaggle.com/competitions"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

active_competitions = soup.find_all(
    "div", {"class": "competition-item__spacer"}
)

active_competitions_list = []
for competition in active_competitions:
    competition_name = competition.find(
        "a", {"class": "competition-item__title"}
    ).text.strip()
    prize_money = competition.find("div", {"class": "prize"}).text.strip()
    time_left = competition.find(
        "div", {"class": "competition-item__end-time"}
    ).text.strip()
    remaining_time = get_remaining_time(time_left)
    if remaining_time:
        active_competitions_list.append(
            {
                "Name": competition_name,
                "Prize Money": prize_money,
                "Time Left": remaining_time,
            }
        )

if len(active_competitions_list) > 0:
    print("Active Competitions:")
    for i, competition in enumerate(active_competitions_list, 1):
        print(f"Number {i}")
        print("Competition Name:", competition["Name"])
        print("Prize Money:", competition["Prize Money"])
        print("Time Left:", competition["Time Left"])
        print()
else:
    print("No active competitions found.")
