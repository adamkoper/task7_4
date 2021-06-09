
from faker import Faker
fake = Faker()
from timeit import default_timer as timer

start = timer()
for x in range(400):
    base_card = [(fake.first_name(), fake.last_name(), fake.phone_number(), fake.ascii_email()) for i in range(x)]
end = timer()

print(end - start)



