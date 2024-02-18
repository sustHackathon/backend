# Project Name: TripMate 

## Description:

TripMate is a web-based platform that empowers budget-conscious travelers to plan personalized and affordable trips. It seamlessly integrates various functionalities to streamline the travel planning process, making it more accessible and enjoyable for users.

## Key Features:

###  Personalized Itinerary Planning:
 Users provide their desired destinations, budget, and preferences. TripMate suggests budget-friendly hotels, transportation options, and tourist attractions, creating a customized itinerary.
### Cost-Effective Recommendations: 
Prioritizes affordable choices while maintaining quality, ensuring users stay within their budget.
### Comprehensive Information: 
Provides detailed descriptions, ratings, and reviews for hotels, transportation, and attractions, enabling informed decision-making.
### User-Friendly Interface:
 Intuitive design facilitates easy navigation and exploration of recommended options.


## Project Structure:

### tripmate
### ├── admin.py                # Administrative functionalities (if applicable)
### ├── auth.py                 # User authentication and authorization logic
### ├── chatBot.py              # Chatbot implementation (if applicable)
### ├── config.py               # Configuration settings for various components
### ├── database.py             # Database connection and interaction mechanisms
### ├── forAll.py               # General utility functions (if applicable)
### ├── main.py                 # Application entry point
### ├── models.py               # Data models representing entities (e.g., users, trips, hotels)
### ├── oauth2.py               # OAuth authentication (if applicable)
### ├── prac.py                 # Practice-related code modules (if applicable)
### ├── README.md               # This file (project documentation)
### ├── router.py               # API routing and request handling
### ├── schedule.py             # Task scheduling functionalities (if applicable)
### ├── schemas.py              # Data validation and serialization/deserialization
### ├── tourist.py              # Tourist-related logic and functionalities
### ├── __init__.py             # Initializes the package
### ├── ai.py                   # Artificial intelligence modules (if applicable)


# Dependencies:
aiohttp==3.9.3
aiohttp-retry==2.8.3
aiosignal==1.3.1
alembic==1.13.1
altair==5.2.0
annotated-types==0.5.0
anyio==3.7.1
APScheduler==3.10.4
apturl==0.5.2
asgiref==3.5.0
asttokens==2.4.1
async-timeout==4.0.3
attrs==21.2.0
backoff==2.2.1
bardapi==0.1.39
bcrypt==3.2.0
beautifulsoup4==4.12.3
blinker==1.7.0
branca==0.7.1
Brlapi==0.8.3
cachetools==5.3.2
certifi==2020.6.20
cffi==1.16.0
chardet==4.0.0
charset-normalizer==3.3.2
click==8.1.7
colorama==0.4.4
command-not-found==0.3
cryptography==3.4.8
cupshelpers==1.0
dbus-python==1.2.18
decorator==5.1.1
defer==1.0.6
distro==1.7.0
distro-info==1.1+ubuntu0.2
dnspython==2.4.2
docker==5.0.3
docker-compose==1.29.2
dockerpty==0.4.1
docopt==0.6.2
duplicity==0.8.21
ecdsa==0.18.0
email-validator==2.0.0.post2
exceptiongroup==1.1.3
executing==2.0.1
fastapi==0.103.2
fasteners==0.14.1
Flask==3.0.2
folium==0.15.1
frozenlist==1.4.1
future==0.18.2
gitdb==4.0.11
GitPython==3.1.41
google-ai-generativelanguage==0.4.0
google-api-core==2.17.0
google-auth==2.27.0
google-cloud-language==2.13.1
google-generativeai==0.3.2
googleapis-common-protos==1.62.0
GoogleBard==2.1.0
greenlet==2.0.2
grpcio==1.60.1
grpcio-status==1.60.1
gyp==0.1
h11==0.14.0
h2==4.1.0
hpack==4.0.0
httpcore==0.18.0
httplib2==0.20.2
httptools==0.6.0
httpx==0.25.0
hyperframe==6.0.1
idna==3.3
importlib-metadata==4.6.4
ipython==8.21.0
itsdangerous==2.1.2
jedi==0.19.1
jeepney==0.7.1
Jinja2==3.1.2
jose==1.0.0
jsonschema==3.2.0
keyboard==0.13.5
keyring==23.5.0
language-selector==0.1
launchpadlib==1.10.16
lazr.restfulclient==0.14.4
lazr.uri==1.0.6
lockfile==0.12.2
louis==3.20.0
macaroonbakery==1.3.1
Mako==1.1.3
Markdown==3.5.2
markdown-it-py==3.0.0
MarkupSafe==2.1.5
matplotlib-inline==0.1.6
mdurl==0.1.2
monotonic==1.6
more-itertools==8.10.0
MouseInfo==0.1.3
multidict==6.0.5
mysql-connector-python==8.1.0
netifaces==0.11.0
numpy==1.26.4
oauthlib==3.2.0
olefile==0.46
openai==0.28.0
opencage==2.4.0
orjson==3.9.7
packaging==23.2
pandas==2.2.0
paramiko==2.9.3
parso==0.8.3
passlib==1.7.4
pexpect==4.8.0
phonenumbers==8.13.29
pillow==10.2.0
pipreqs==0.4.13
prompt-toolkit==3.0.43
proto-plus==1.23.0
protobuf==4.21.12
psycopg2-binary==2.9.8
ptyprocess==0.7.0
pure-eval==0.2.2
pyarrow==15.0.0
pyasn1==0.5.0
pyasn1-modules==0.3.0
PyAutoGUI==0.9.54
pycairo==1.20.1
pycparser==2.21
pycups==2.0.1
pydantic==2.4.2
pydantic-extra-types==2.1.0
pydantic-settings==2.0.3
pydantic_core==2.10.1
pydeck==0.8.1b0
PyGetWindow==0.0.9
Pygments==2.17.2
PyGObject==3.42.1
PyJWT==2.3.0
pymacaroons==0.13.0
PyMsgBox==1.0.9
PyNaCl==1.5.0
pyparsing==2.4.7
pypdf==4.0.1
pyperclip==1.8.2
PyRect==0.2.0
pyRFC3339==1.1
pyrsistent==0.18.1
PyScreeze==0.1.30
python-apt==2.4.0+ubuntu2
python-dateutil==2.8.2
python-debian==0.1.43+ubuntu1.1
python-dotenv==1.0.0
python-jose==3.3.0
python-multipart==0.0.6
python3-xlib==0.15
pytweening==1.0.7
pytz==2022.1
pywhatkit==5.4
pyxdg==0.27
PyYAML==5.4.1
reportlab==3.6.8
requests==2.31.0
rich==13.7.0
rsa==4.9
schedule==0.6.0
SecretStorage==3.3.1
six==1.16.0
smmap==5.0.1
sniffio==1.3.0
socksio==1.0.0
soupsieve==2.5
SQLAlchemy==2.0.21
stack-data==0.6.3
starlette==0.27.0
streamlit==1.31.0
streamlit-chat==0.1.1
systemd-python==234
tenacity==8.2.3
texttable==1.6.4
toml==0.10.2
toolz==0.12.1
tornado==6.4
tqdm==4.66.1
traitlets==5.14.1
twilio==8.13.0
typing_extensions==4.8.0
tzdata==2023.4
tzlocal==5.1
ubuntu-advantage-tools==8001
ubuntu-drivers-common==0.0.0
ufw==0.36.1
ujson==5.8.0
unattended-upgrades==0.1
urllib3==1.26.5
usb-creator==0.3.7
uvicorn==0.23.2
uvloop==0.17.0
validators==0.22.0
vboxapi==1.0
wadllib==1.3.6
watchdog==4.0.0
watchfiles==0.20.0
wcwidth==0.2.13
websocket-client==1.7.0
websockets==11.0.3
Werkzeug==3.0.1
wikipedia==1.4.0
wsproto==1.0.0
xdg==5
xkit==0.0.0
xyzservices==2023.10.1
yarg==0.1.9
yarl==1.9.4
zipp==1.0.0



# Installation:

1. Clone the repository: git clone gh repo clone sustHackathon/backend
2. Install dependencies: pip install -r requirements.txt

