from address import Address
from mailing import Mailing

to_address = Address(400066, "Волгоград", "Ленина", 5, 25)
from_address = Address(350073, "Краснодар", "Командорская", 3, 279)

mailing = Mailing(from_address, to_address, 100, "4564645646")

print(mailing)
