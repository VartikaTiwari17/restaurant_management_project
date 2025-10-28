from home.models import Restaurant
r = Restaurant.objects.create(
    name="Spice Villa",
    address="Ayodhya",
    contact_number="9876543210",
    email="spicevilla@example.com"
)
print(r.has_delivery)
