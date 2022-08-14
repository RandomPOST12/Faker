from faker import Faker
fake = Faker()
with open('fakedata','w') as f:
    for _ in range(100):
        f.write(f'{fake.name()} {fake.email()} \n')

