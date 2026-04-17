import os
import sys

# We look for a variable named 'API_KEY'
token = os.getenv('my-internal-api-key')

if token == "SUPER_SECRET_123":
    print("SUCCESS: Authenticated with Internal API.")
    print("DATA: {'status': 'active', 'server': 'us-east-1'}")
else:
    print("ERROR: Unauthorized! Token is missing or invalid.")
    sys.exit(1) # This tells Jenkins the build failed
