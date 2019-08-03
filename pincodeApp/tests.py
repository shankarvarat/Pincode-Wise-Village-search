from django.test import TestCase

# Create your tests here.
with open('C:/Users/hp/Desktop/pincode.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        _, created = pincode.objects.get_or_create(
            Village=row[0],
            Pincode=row[1],
            District=row[2],
            StateName=row[3],
        )