#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import configparser
import random
import re
import requests
import sys
import unshortenit
import feedparser


BOT_CONFIG_FILE = '/usr/local/bin/RssToFile/bot.conf'
SRC_RE = re.compile(r'src="([^"]*)"')
RE_HTML_TAGS = re.compile(r'<.+?>')

def clean_url(url):
    unshortened_uri,status = unshortenit.unshorten(url)
    return unshortened_uri


def create_file(file):
    open(file, 'w', encoding='utf-8')


def update_log(link):
    with open(last_updates, 'r') as file:
        lines = file.readlines()
    if lines.__len__() >= 200:
        lines.pop(0)
    lines.append(''.join(link) + '\n')
    with open(last_updates, 'w') as file:
        for l in lines:
            file.write(l)

def has_updates(item_datetime):
    try:
        updates = open(last_updates, 'r')
    except:
        create_file(last_updates)
        updates = open(last_updates, 'r')
    for update in updates:
        if item_datetime in update.split('\n'):
            return False

    update_log(item_datetime)
    return True

def to_line(text):
    with open(line_file, 'a', encoding="utf-8") as file:
        file.write(text + '\n')
        file.close()

if __name__ == '__main__':
    rss = sys.argv[1]
    config = configparser.ConfigParser()
    config.sections()
    config.read(BOT_CONFIG_FILE)
    last_updates = config[rss]['LOG_FILE']
    feed_url = config[rss]['FEED_URL']
    line_file = config[rss]['LINE_FILE']
    blacklist = ('/usr/local/bin/RssToFile/lists/' + rss + '_blacklist.txt')
    feed = feedparser.parse(feed_url)
    for item in reversed(feed['items'][:100]):
        published_parsed = item['published_parsed']
        publicado = '{}{:02d}{:02d}{:02d}{:02d}{:02d}'.format(
            published_parsed.tm_year,
            published_parsed.tm_mon,
            published_parsed.tm_mday,
            published_parsed.tm_hour,
            published_parsed.tm_min,
            published_parsed.tm_sec)

        if not has_updates(publicado):
            continue

        link = clean_url(item['link'])
        to_line(link)
        print(link)
