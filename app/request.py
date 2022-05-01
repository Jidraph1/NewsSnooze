from app import app
import urllib.request,json
from .models import source
from .models import articles

#Getting api key
api_key = app.config['NEWS_API_KEY']

