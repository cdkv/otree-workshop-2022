from os import environ
SESSION_CONFIG_DEFAULTS = dict(real_world_currency_per_point=0.08, participation_fee=0)
SESSION_CONFIGS = [dict(name='instructions', num_demo_participants=None, app_sequence=['Instructions']), dict(name='post_survey', num_demo_participants=None, app_sequence=['Post_survey']), dict(name='full_experiment', num_demo_participants=None, app_sequence=['Instructions', 'initial_stage', 'main_stage', 'Post_survey']), dict(name='initial_main_bots', num_demo_participants=None, app_sequence=['initial_stage', 'main_stage', 'Post_survey'], use_browser_bots=True), dict(name='initialmain', num_demo_participants=None, app_sequence=['initial_stage', 'main_stage']), dict(name='initial2_test', num_demo_participants=6, app_sequence=['initial_stage2', 'main_stage']), dict(name='full_experiment2', num_demo_participants=None, app_sequence=['Instructions', 'initial_stage2', 'main_stage', 'Post_survey'])]
LANGUAGE_CODE = 'en'
REAL_WORLD_CURRENCY_CODE = 'GBP'
USE_POINTS = True
DEMO_PAGE_INTRO_HTML = ''
PARTICIPANT_FIELDS = ['time_outs', 'bribes', 'role', 'order_firm_condition', 'order_official_condition', 'payment', 'finished']
SESSION_FIELDS = ['prolific_completion_url']
ROOMS = [dict(name='waiting_room', display_name='Waiting Room')]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

SECRET_KEY = 'blahblah'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']


