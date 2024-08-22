#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7415405703:AAGGGCgvldr3KIf6Agj9vituKJAz4gWM0H8")
    API_ID = int(os.environ.get("API_ID", "29640188"))
    API_HASH = os.environ.get("API_HASH", "e470abc84a3bc445997ee4ea5be87deb")
    AUTH_USERS = os.environ.get("AUTH_USERS", "7504263874")
