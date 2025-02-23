import binascii
import secrets
from argon2 import PasswordHasher
import os
import bcrypt

class Random_generator:

    # generates a random token using the secrets library for true randomness
    def generate_token(self, length=8, alphabet=(
    '0123456789'
    'abcdefghijklmnopqrstuvwxyz'
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    )):
        return ''.join(secrets.choice(alphabet) for i in range(length))

    # generates salt using the bcrypt library which is a safe implementation
    def generate_salt(self, rounds=12):
        return bcrypt.gensalt(rounds)

class Argon2_hasher:

    def __init__(self):
        self.ph = PasswordHasher()

    # produces the password hash using Argon2
    def password_hash(self, password):
        return self.ph.hash(password)

    # verifies that the hashed password matches the plain text version
    def password_verification(self, password, password_hash):
        try:
            return self.ph.verify(password_hash, password)
        except:
            return False

# a collection of sensitive secrets necessary for the software to operate
PRIVATE_KEY = os.environ.get('PRIVATE_KEY')
PUBLIC_KEY = os.environ.get('PUBLIC_KEY')
SECRET_KEY = os.environ.get('SECRET_KEY')
PASSWORD_HASHER = 'Argon2_hasher'

# Solution explanation:

# Some mistakes are basic, like choosing a cryptographically-broken algorithm
# or committing secret keys directly in your source code.

# You are more likely to fall for something more advanced, like using functions that
# seem random but produce a weak randomness.

# The code suffers from:
# - reinventing the wheel by generating salt manually instead of calling gensalt()
# - not utilizing the full range of possible salt values
# - using the random module instead of the secrets module

# Notice that we used the “random” module, which is designed for modeling and simulation,
# not for security or cryptography.

# A good practice is to use modules specifically designed and, most importantly,
# confirmed by the security community as secure for cryptography-related use cases.

# To fix the code, we used the “secrets” module, which provides access to the most secure
# source of randomness on my operating system. I also used functions for generating secure
# tokens and hard-to-guess URLs.

# Other python modules approved and recommended by the security community include argon2
# and pbkdf2.