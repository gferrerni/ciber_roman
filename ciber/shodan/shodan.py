import shodan
import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print(f"{bcolors.BOLD}{bcolors.OKBLUE}SHODAN{bcolors.ENDC}")

SHODAN_API_KEY = os.getenv('SHODAN_API_KEY')
print(SHODAN_API_KEY)
api = shodan.Shodan(SHODAN_API_KEY)
try:
        results = api.search(sys.argv[1])
        print(f"{bcolors.OKGREEN} Resultados encontrados: {results['total']}{bcolors.ENDC}")
        for result in results['matches']:
                print("IP: {result['ip_str']}")
                print(result['data'])
                print('')
except shodan.APIError as e:
        print(f"{bcolors.FAIL}Error: {e}{bcolors.ENDC}")