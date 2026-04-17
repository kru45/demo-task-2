import os
import sys

# Jenkins will "inject" the secret into this variable
token = os.getenv('API_KEY') 

# Make sure this string matches what you typed in Jenkins Credentials
if token == "SUPER_SECRET_123":
    print("SUCCESS: Authenticated with Internal API.")
else:
    # If we are here, it means 'token' is either None or the wrong string
    print(f"ERROR: Unauthorized! Received: {token}") 
    sys.exit(1)
