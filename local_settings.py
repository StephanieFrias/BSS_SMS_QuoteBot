'''
Configuration Settings

Includes keys for Twilio, etc.  Second stanza intended for Heroku deployment.
'''

# Uncommet to configure in file.
ACCOUNT_SID = "AC9bda99a6330ad8c75de80fddac19e7a7" 
AUTH_TOKEN = "b4f942e6b561270b682ff5aa73f351a9"
BSSSPAM_APP_SID = "AP9608d4a6e1007caf24801e71f5f6e3f5"
BSS_SPAM_ID = "+13056005508"


# Begin Heroku configuration - configured through environment variables.
import os
ACCOUNT_SID = os.environ['ACCOUNT_SID']
AUTH_TOKEN = os.environ['AUTH_TOKEN']
BSSSPAM_APP_SID = os.environ['BSSSPAM_APP_SID']
BSS_SPAM_ID = os.environ['BSS_SPAM_ID']
