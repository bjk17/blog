#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Bjarni Jens Kristinsson'
SITENAME = u'Bjarni Jens\'s blog'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Atlantic/Reykjavik'

DEFAULT_LANG = u'en'

THEME = 'flex-theme'
SITETITLE = 'blog.bjk.is'
SITESUBTITLE = 'Bjarni Jens Kristinsson blogging about tech'
SITEDESCRIPTION = 'A tech blog'

STATIC_PATHS = ['static']
SITELOGO = SITEURL + '/static/bjk17.jpg '
#FAVICON = SITEURL + '/static/favicon.ico'
DISQUS_SITENAME = 'bjk17'

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
LINKS = (('my website', 'https://bjk.is/'),
         ('bio.bjk.is', 'http://bio.bjk.is/'),)

# Social widget
SOCIAL = (('facebook', 'https://facebook.com/bjarni.jens'),
          ('linkedin', 'https://linkedin.com/in/bjk17'),
          ('envelope-o', 'mailto:bjarni.jens@gmail.com'),
          ('github', 'https://github.com/bjk17'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
