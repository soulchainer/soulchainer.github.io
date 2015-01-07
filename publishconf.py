#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

# import os
# import sys
# sys.path.append(os.curdir)
# from pelicanconf import *

# DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
AUTHOR = 'Soulchainer'
SITENAME = 'Soulbits'
SITESUBTITLE = 'archlinux, software libre y apuntes varios'
SITEURL = '//soulchainer.github.io'
PATH = 'content/'
PAGE_PATHS = ['pages',]
ARTICLE_PATHS = ['posts',]
OUTPUT_PATH = 'publish/'
PLUGIN_PATHS = ['plugins/',]
PLUGINS = ['better_figures_and_images', 'multi_part',
           'pelican_youtube', 'sitemap', 'pelican_vimeo', 'summary']
SUMMARY_MAX_LENGTH = 70
SUMMARY_BEGIN_MARKER = "{BEGIN_SUMMARY}"
SUMMARY_END_MARKER = "{END_SUMMARY}"

TIMEZONE = 'Europe/Madrid'

TYPOGRIFY = True

DEFAULT_LANG = 'es'

FEED_ALL_ATOM = 'feeds/all.xml'
CATEGORY_FEED_ATOM = None

DEFAULT_PAGINATION = 6
DEFAULT_ORPHANS = 4

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
# URL settings
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
TAG_URL = 'tags/{slug}/'
TAG_SAVE_AS = 'tags/{slug}/index.html'
TAGS_URL = 'tags/'
TAGS_SAVE_AS = 'tags/index.html'
AUTHOR_URL = 'author/{slug}.html'
AUTHOR_SAVE_AS = False
AUTHORS_URL = 'authors.html'
AUTHORS_SAVE_AS = False
ARCHIVES_URL = 'archives/'
ARCHIVES_SAVE_AS = 'archives/index.html'
# YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
# MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

# Custom pages
TEMPLATE_PAGES = {'themes/simplesoul/templates/404.html': '404.html'
                  }

STATIC_PATHS = [
    'images',
    'extra/robots.txt',
    'extra/humans.txt',
    'extra/favicon.ico',
    'extra/README.rst',
    'extra/.nojekyll',
    ]
EXTRA_PATH_METADATA = {
    'images': {'path': 'images'},
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/humans.txt': {'path': 'humans.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/README.rst': {'path': 'README.rst'},
    'extra/.nojekyll': {'path': '.nojekyll'},
    }
# Tag Cloud
TAG_CLOUD_STEPS = 4     # Count of different font sizes in the tag cloud.
TAG_CLOUD_MAX_ITEMS = 300   # Maximum number of tags in the cloud.

# Themes
# Specify name of a built-in theme
#THEME = "notmyidea"
# Specify name of a theme installed via the pelican-themes tool
# THEME = "pelican-cait"
# Specify a customized theme, via path relative to the settings file
# THEME = "themes/mycustomtheme"
# Specify a customized theme, via absolute path
THEME = 'content/themes/simplesoul'
# Añadidos del tema simplesoul, basado en crowsfoot
GITHUB = 'https://github.com/soulchainer'
TWITTER = 'https://twitter.com/soulchainer'
GOOGLEPLUS = 'https://www.google.com/+JuanRiquelmeSoul'
TUMBLR = 'http://soulchainer.tumblr.com'
LASTFM = 'http://www.lastfm.es/user/Soulchainer'
FLICKR = 'http://flickr.com/photos/soulchainer'
DISQUS_SITENAME = 'soulbits'
MENUITEMS = [
    ['tags', '/tags/'],
    ['archivo', '/archives/'],
    ['rss', '/feeds/all.xml']
]

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}
# Añadidos para plugin Better Figures & Images
RESPONSIVE_IMAGES = True
# Extension for more easy archive generation
# JINJA_EXTENSIONS = ['jinja2.ext.loopcontrols']
# Jinja custom filters available to all templates:
# import re
# from jinja2 import Undefined


# # Custom filter method
# def regex_replace(s, find, replace):
#     """A implementation of a regex filter"""
#     if s is None or isinstance(s, Undefined):
#         # if s is Undefined, return s
#         return s
#         # else, do the regex replace
#     return re.sub(find, replace, s)

# JINJA_FILTERS = {
#     'regex_replace': regex_replace,
# }
