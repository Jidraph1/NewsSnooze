from app import app
import urllib.request,json
from .models import source
from .models import articles

#Getting api key
api_key = app.config['NEWS_API_KEY']

#Getting the News base Url
base_url = app.config['NEWS_API_BASE_URL']

def get_source():
    """
    Function that gets the json response to our Url request
    """
    get_source_url = base_url.format(api_key)
    
    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_results = None
        if get_source_response['results']:
            source_results_list = get_source_response['results']
            source_results = process_results(source_result_list)

            return source_results

def process_results():
    """
    Function that processes the source result and tranforms them into a list of objects
    Args:
    source_list: A list of dictionaries that contain the source details
    Returns: 
    source_list: A list of source objects
    """

    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        title = source_item.get('title')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get ('category')

        source_object=source.Source(id,name,description,url,category)
        source_results.append(source_object)

    return source_results
