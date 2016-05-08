#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Bjarni Jens Kristinsson'
SITEURL = ''
SITENAME = u'Bjarni Jens\'s blog'
SITETITLE = 'blog.bjk.is'
SITESUBTITLE = 'servers, networks, infrastructure, programming and mathematics'
SITEDESCRIPTION = 'A personal blog about tech'

TIMEZONE = 'Atlantic/Reykjavik'
DEFAULT_LANG = u'en'

PATH = 'content'
THEME = 'flex-theme'

STATIC_PATHS = ['static']
SITELOGO = SITEURL + '/static/bjk17.jpg '
#FAVICON = SITEURL + '/static/favicon.ico'

SUMMARY_MAX_LENGTH = 100

MAIN_MENU = True
MENUITEMS = (('Archives', '/archives.html'),
            ('Categories', '/categories.html'),
            ('Tags', '/tags.html'))

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('bjk.is', 'https://bjk.is/'),
         ('bio.bjk.is', 'http://bio.bjk.is/'),)

# Social widget
SOCIAL = (('facebook', 'https://facebook.com/bjarni.jens'),
          ('linkedin', 'https://linkedin.com/in/bjk17'),
          ('github', 'https://github.com/bjk17'),
          ('envelope-o', 'mailto:bjarni.jens@gmail.com'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
