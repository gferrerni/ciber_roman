import os
import sys
import json
from vtapi3 import VirusTotalAPIFiles, VirusTotalAPIError

import pybase64

VIRUSTOTAL_API_KEY = os.getenv('VIRUSTOTAL_API_KEY')
vt_files = VirusTotalAPIFiles(VIRUSTOTAL_API_KEY)


try:
    result = vt_files.upload(sys.argv[1])
except VirusTotalAPIError as err:
    print(err, err.err_code)
else:
    if vt_files.get_last_http_error() == vt_files.HTTP_OK:
        result = json.loads(result)
        result = json.dumps(result, sort_keys=False, indent=4)
        hash = pybase64.b64decode(result["data"]["id"])
        print(hash.split(':')[0])
	
    else:
        print('HTTP Error [' + str(vt_files.get_last_http_error()) +']')
