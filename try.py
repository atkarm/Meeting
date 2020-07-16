from _datetime import datetime, date, timezone

import eastern as eastern

# loc_dt = eastern.localize(datetime.utcnow())
# print(loc_dt)

my_str = "hello123456789"
print(len(my_str))
print(my_str[10:12])
print(my_str[11])
print(my_str[12])
a = int(my_str[10:12])
n = int(my_str[9:11])
print(a)
print(n)
print(a-n)