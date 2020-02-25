import hashlib
from datetime import timedelta, date


def daterange(date1, date2):
    for n in range(int((date2 - date1).days) + 1):
        yield date1 + timedelta(n)


start_dt, end_dt = date(2015, 1, 1), date(2019, 5, 14)
for dt in daterange(start_dt, end_dt):
    date = dt.strftime("%Y-%m-%d")
    sha256 = hashlib.sha256(date.encode('utf-8')).hexdigest()
    if sha256.startswith('f50130d'):
        print(date)
        print(sha256)
        break
