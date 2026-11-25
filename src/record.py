from urllib.parse import urlsplit
from pathlib import Path
import json
import sys

def validate(record):
    if record.get('state') not in {'pending', 'reported'}:
        raise ValueError('Use pending or reported')
    if not record.get('asset') or not record.get('claim'):
        raise ValueError('Supply an asset and claim')
    if record['state'] == 'reported':
        slot = record.get('slot')
        ref = urlsplit(record.get('reference') or '')
        if type(slot) is not int or slot <= 0 or ref.scheme != 'https' or ref.hostname not in {'explorer.solana.com', 'solscan.io'} or not ref.path.startswith('/tx/') or len(ref.path) <= 4:
            raise ValueError('A reported claim requires a positive slot and a transaction link')
    return record['state']

if __name__ == '__main__':
    print(validate(json.loads(Path(sys.argv[1]).read_text())))
