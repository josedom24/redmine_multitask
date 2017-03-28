import os
# Change working directory so relative paths (and template lookup) work again
os.chdir(os.path.dirname(__file__))
from redmine import app
# ... build or import your bottle application here ...
# Do NOT use bottle.run() with mod_wsgi
application = app
