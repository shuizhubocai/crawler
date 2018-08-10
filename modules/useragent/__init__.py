from .chrome import chrome
from .firefox import firefox
from .mozilla import mozilla
from .opera import opera
from .safari import safari
import random

def getUserAgent(type=''):
    type = type.lower()
    userAgent = {
        'chrome': chrome,
        'firefox': firefox,
        'mozilla': mozilla,
        'opera': opera,
        'safari': safari,
        'all': chrome + firefox + mozilla + opera + safari
    }
    if (type == 'chrome' or type == 'firefox' or type == 'mozilla' or type == 'opera' or type == 'safari'):
        ua = random.choice(userAgent[type])
    else:
        ua = random.choice(userAgent['all'])
    return ua

