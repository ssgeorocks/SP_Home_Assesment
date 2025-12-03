import os
from dotenv import load_dotenv

load_dotenv()

TEST_CREDENTIALS = {
    'email' : os.getenv('SP_EMAIL_TEST'),
    'password' : os.getenv('SP_PASSWORD_TEST')
}