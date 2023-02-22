from os import environ


SESSION_CONFIGS = [
    dict(
        name='public_goods',
        display_name="Public Goods",
        num_demo_participants=3,
        app_sequence=['public_goods', 'payment_info'],
    ),
    dict(
        name='guess_two_thirds',
        display_name="Guess 2/3 of the Average",
        num_demo_participants=3,
        app_sequence=['guess_two_thirds', 'payment_info'],
        treatment = 1
    ),
    dict(
        name='survey',
        display_name='survey',
        num_demo_participants=1,
        app_sequence=['survey', 'payment_info'],
    ),
    dict(
        name='trust',
        display_name='trust',
        num_demo_participants=2,
        app_sequence=['trust', 'payment_info'],
    ),
    dict(
        name='experiment',
        display_name='experiment',
        num_demo_participants=2,
        app_sequence=['trust', 'dictator','payment_info'],
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""
PARTICIPANT_FIELDS = ['pagos']

SECRET_KEY = '6_x-_kse9=u*&%4fh9lul9hxriswh&4_@^ze-3_ydq(_l!_3u5'

INSTALLED_APPS = ['otree']
