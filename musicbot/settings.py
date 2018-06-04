"""Global configuration variables."""

########################
#   GENERAL SETTINGS   #
########################

driver = None

CHANNEL_ID = '451695099018084352'

########################
#   DISCORD SETTINGS   #
########################

DISCORD_TOKEN = 'NDM3MjE5ODgwMTc4MDI0NDQ4.DfMngw.aiilp7si6bfKWYaEgBqm-wcPn5k'
########################
#   SPOTIFY SETTINGS   #
########################

S_CLIENT_ID = '437219880178024448'
S_CLIENT_SECRET = 'fBPsb08xgnF0k2RNViRbG4JTBvjr_nGc'
S_REDIRECT_URI = 'https://discordapp.com/channels/@me'

S_URL = f"https://accounts.spotify.com/authorize/?" \
        f"client_id={S_CLIENT_ID}&" \
        f"response_type=code&" \
        f"redirect_uri={S_REDIRECT_URI}&" \
        f"scope=user-read-birthdate%20user-read-private%20" \
        f"user-read-email%20user-read-currently-playing&" \
        f"state=34fFs29kd09"

S_SCOPE = """user-read-birthdate
             user-read-private
             user-read-email
             user-read-currently-playing
             user-modify-playback-state"""

S_TOKEN = ''
