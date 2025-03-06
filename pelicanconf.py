AUTHOR = 'Davud'
SITENAME = 'Pelican Resume'
SITEURL = ""

PATH = "content"

TIMEZONE = 'America/Winnipeg'

DEFAULT_LANG = 'EN'


THEME = "themes/Flex"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

SITETITLE = "Welcome to my website"

MAIN_MENU = True

MENUITEMS = [
    ("About", "/Assignment2/about.html"),
    ("Resume", "/Assignment2/resume.html"),
]

# Social widget
SOCIAL = (
    ("github", "https://github.com/davkasnaixl"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
