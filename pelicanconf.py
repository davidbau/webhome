#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'David Bau'
SITENAME = u'David Bau'
HIDE_SITENAME = True
SITEURL = 'http://people.csail.mit.edu/davidbau/home'

THEME = '../pelican-bootstrap3'
BOOSTRAP_THEME = 'cosmo'
BOOTSTRAP_NAVBAR_INVERSE = True
SITELOGO = 'img/MIT-logo-grey.png'
SITELOGO_SIZE = 48

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Summaries contain the whole article
SUMMARY_MAX_LENGTH = 600

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

HIDE_SIDEBAR = True
# Blogroll
MENUITEMS = (
  ('Blog', 'http://davidbau.com/'),
  ('Github', 'https://github.com/davidbau'),
#  ('pencilcode.net', 'https://pencilcode.net/'),
)

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['img']
