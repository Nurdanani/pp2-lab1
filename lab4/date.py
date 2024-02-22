# ex1
from datetime import datetime, timedelta
x = datetime.now()
y = timedelta(days=5)
z= x - y
print(z)

# ex2
from datetime import datetime, timedelta
x=datetime.now()
y=timedelta(days=1)
yes=x-y
tom=x+y
print(yes)
print(x)
print(tom)

# ex3
from datetime import datetime
x=datetime.now()
y=x.replace(microsecond=0)
print(y)

# ex4
from datetime import datetime
x=datetime(2024, 2, 21, 18, 0, 0)
y=datetime(2024, 2, 21, 17 ,45, 0)

dif=x-y
difsec=dif.total_seconds()
print(difsec)