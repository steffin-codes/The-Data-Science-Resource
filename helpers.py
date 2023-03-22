import urllib

GIT_REPO = 'https://raw.githubusercontent.com/steffincodes/data-scribbles/main/'
IS_LOCAL = True # commit with False

def get_file_content_as_string(path):
    if IS_LOCAL:
        with open(path,'r') as fp:
            return fp.read()
    else:
        url = GIT_REPO + path
        response = urllib.request.urlopen(url)
        return response.read().decode("utf-8")