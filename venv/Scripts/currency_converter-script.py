#!C:\Users\Ofir\PycharmProjects\WorldOfGames\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'CurrencyConverter==0.13.11','console_scripts','currency_converter'
__requires__ = 'CurrencyConverter==0.13.11'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('CurrencyConverter==0.13.11', 'console_scripts', 'currency_converter')()
    )
