from os import environ

SESSION_CONFIGS = [
    dict(
        name='ASCMS_Pilot',
        display_name="ASCMS Pilot",
        num_demo_participants=2,
        app_sequence=['introwording', 'axiomwording', 'thankyou']
    ),

    dict(
        name='ejercicio',
        display_name="ejercicio",
        num_demo_participants=2,
        app_sequence=['axiomwording',]
    ),

    dict(
        name='ASCMS_Main',
        display_name="ASCMS Main",
        num_demo_participants=2,
        app_sequence=['mainstage', 'controls', 'thankyou']
    ),
    dict(
        name='ASCMS_Controls',
        display_name="ASCMS Control",
        num_demo_participants=2,
        app_sequence=['controls', 'thankyou']
    ),
]


# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=5.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'ES'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = './S'
USE_POINTS = False


ROOMS = [
    dict(
        name='xproom',
        display_name='Waiting room',
#        use_secure_urls=True
    ),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '8c+zro!d7^z8(&b(k5+h995d+a92pk%3)_raah!_it6fkqhuc9'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
