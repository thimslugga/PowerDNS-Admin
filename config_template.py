import os
basedir = os.path.abspath(os.path.dirname(__file__))

# BASIC APP CONFIG
LOGIN_TITLE = "PowerDNS-Admin"
BIND_ADDRESS = '127.0.0.1'
PORT = 9393
DEBUG = True
WTF_CSRF_ENABLED = True
SECRET_KEY = 'iluvpowerdns'

# TIMEOUT - for large zones
TIMEOUT = 10

# LOG CONFIG
LOG_DIR = os.path.join(basedir, 'logs')
# For Docker, leave empty string - LOG_FILE = ''
LOG_FILE = 'logfile.log'
LOG_LEVEL = 'DEBUG'

# Upload
UPLOAD_DIR = os.path.join(basedir, 'upload')

# DATABASE CONFIG
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True

#PostgreSQL
SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@127.0.0.1/powerdnsadmin'

#SQLite
#SQLALCHEMY_DATABASE_URI = 'sqlite:////path/to/your/pdns.db'

#You'll need MySQL-python
#SQLA_DB_USER = 'powerdnsadmin'
#SQLA_DB_PASSWORD = 'powerdnspassword'
#SQLA_DB_HOST = '127.0.0.1'
#SQLA_DB_NAME = 'powerdnsadmin'

#MySQL
#SQLALCHEMY_DATABASE_URI = 'mysql://'+SQLA_DB_USER+':'\
#    +SQLA_DB_PASSWORD+'@'+SQLA_DB_HOST+'/'+SQLA_DB_NAME

# LDAP CONFIG
#LDAP_TYPE = 'ldap'
#LDAP_URI = 'ldaps://your-ldap-server:636'
#LDAP_USERNAME = 'cn=dnsuser,ou=users,ou=services,dc=duykhanh,dc=me'
#LDAP_PASSWORD = 'dnsuser'
#LDAP_SEARCH_BASE = 'ou=System Admins,ou=People,dc=duykhanh,dc=me'
# Additional options only if LDAP_TYPE=ldap
#LDAP_USERNAMEFIELD = 'uid'
#LDAP_FILTER = '(objectClass=inetorgperson)'

## AD CONFIG
#LDAP_TYPE = 'ad'
#LDAP_URI = 'ldaps://your-ad-server:636'
#LDAP_USERNAME = 'cn=dnsuser,ou=Users,dc=domain,dc=local'
#LDAP_PASSWORD = 'dnsuser'
#LDAP_SEARCH_BASE = 'dc=domain,dc=local'
## You may prefer 'userPrincipalName' instead
#LDAP_USERNAMEFIELD = 'sAMAccountName'
## AD Group that you would like to have accesss to web app
#LDAP_FILTER = 'memberof=cn=DNS_users,ou=Groups,dc=domain,dc=local'

# Github Oauth
GITHUB_OAUTH_ENABLE = False
GITHUB_OAUTH_KEY = 'GITHUB_OAUTH_KEY_GOES_HERE'
GITHUB_OAUTH_SECRET = 'GITHUB_OAUTH_SECRET_GOES_HERE'
GITHUB_OAUTH_SCOPE = 'email'
GITHUB_OAUTH_URL = 'http://127.0.0.1:5000/api/v3/'
GITHUB_OAUTH_TOKEN = 'http://127.0.0.1:5000/oauth/token'
GITHUB_OAUTH_AUTHORIZE = 'http://127.0.0.1:5000/oauth/authorize'

#Default Auth
BASIC_ENABLED = True
SIGNUP_ENABLED = True

# POWERDNS CONFIG
PDNS_STATS_URL = 'http://127.0.0.1:8081/'
PDNS_API_KEY = 'changeme'
PDNS_VERSION = '4.0.0'

# RECORDS ALLOWED TO EDIT
RECORDS_ALLOW_EDIT = ['A', 'AAAA', 'CNAME', 'SPF', 'PTR', 'MX', 'TXT']

# EXPERIMENTAL FEATURES
PRETTY_IPV6_PTR = False
