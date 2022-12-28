import pyotp
import time

totp = pyotp.TOTP('pcvrvcc3nasssimv33fde2fhk5ukfizs')
print(totp.now())
