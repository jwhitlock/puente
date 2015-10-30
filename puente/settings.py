from puente.utils import generate_keywords


# Name for .pot file--should be 'django'
TEXT_DOMAIN = 'django'

# Keywords indicating gettext calls
KEYWORDS = generate_keywords()

# By default, all the domains you speficy will be merged into one big django.po
# file. If you want to separate a domain from the main .po file, specify it in
# this list. Make sure to include TEXT_DOMAIN in this list, even if you have
# other .po files you're generating
STANDALONE_DOMAINS = [TEXT_DOMAIN]

# Prefixes that indicate a comment tag intended for localizers
COMMENT_TAGS = ['L10n:', 'L10N:', 'l10n:', 'l10N:']

# Tells the extract script what files to look for L10n in and what
# function handles the extraction.
# Map of domain to list of (match, extractor)
DOMAIN_METHODS = None

# The basedir of this project to extract strings from
BASE_DIR = None

# If you set this, we'll use it. Otherwise we assume you're using django-jinja
# and we'll pick up the settings from the first template handler specified.
JINJA2_CONFIG = None

# The name of the project.
PROJECT = 'PROJECT'

# The version of the project.
VERSION = '1.0'

# Email address or url for reporting msgid-related bugs to.
MSGID_BUGS_ADDRESS = ''


def get_setting(key):
    from django.conf import settings
    return settings.PUENTE.get(key, globals()[key])
