#from googleplayapi import download
#from googleplay import GooglePlayAPI
#from gpapi.googleplay import GooglePlayAPI
import sys

from gpapi.googleplay import GooglePlayAPI

# Create global variables for easy settings change and use.
LOCALE = "us_US"
TIMEZONE = "America/Chicago"
MAX_RESPONSE = 34
APP_NAME = sys.argv[1]
EMAIL = ""
PASSWORD = ""
AUTH_TOKEN = ""

# Create instance of API with ( locale, time zone )
server = GooglePlayAPI(locale = LOCALE, timezone = TIMEZONE)

# Login using just username and password.
print("\nTrying log in with just email and password\n")
server.login(email = EMAIL, password = PASSWORD) #, auth_token = AUTH_TOKEN)
#gsfId = server.gsfId
gsfId = 0
print(gsfId)
#authSubToken = server.authSubToken
authSubToken=""
print(authSubToken)

# Now that we've been authorized once, we can use the gsfID and token previously
# generated to create a new instance w/o email or password.
print("\nTrying secondary login with ac2dm token and gsfId saved...\n")
server = GooglePlayAPI(locale = LOCALE, timezone = TIMEZONE)
server.login(gsfId = gsfId, authSubToken = authSubToken)

# Search the Play Store using `search` function
# First: Search query for the Play Store.
# Specify the maximum amount of apps that meet criteria that can be returned.
# Third param is `offset`. Determines if you want to start at a certain
# index in the returned list. Default is `None`.
m = server.details(packageName=APP_NAME)
print(m)
vc = m['details']['appDetails']['versionCode']
ot = m['offer'][0]['offerType']
#    def download(self, packageName, versionCode=None, offerType=1, expansion_files=False):
data = server.download(packageName = APP_NAME, versionCode=vc, offerType=ot)

with open("data/"+data['docId'] + '.apk', 'wb') as first:
    for chunk in data.get('file').get('data'):
        first.write(chunk)



#print(data)
#open("data/"+APP_NAME+".apk", "wb").write(data['file']['data'])

'''
# Get the version code and the offer type from the app details
print vc

# Download
print "Downloading %s..." % sizeof_fmt(doc.details.appDetails.installationSize),
data = api.download(packagename, vc, ot)
print "Done"
'''


# Get the suggested search options from our desired app name
#print("Search Suggestions for `%s`:" % APP_NAME)
#print(server.searchSuggest(APP_NAME))

'''
# Print our max limit and then the actual amount returned
print("Max #of Results: %i" % MAX_RESPONSE)
print("Actual #of Results: %d" % len(apps))

# if at least 1 app found, then print out its ID.
if len(apps) > 0:
    print("Found apps: ")
    # each app acts as a Dictionary
    for _app in apps:
        #print("App[docID]: %s" % _app["docId"])
        print(_app)
'''
