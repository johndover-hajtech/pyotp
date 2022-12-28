import pyotp
import time
import os

totp = pyotp.TOTP(os.environ['OTP_SECRET'])
print(totp.now())
