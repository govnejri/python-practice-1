driver_name = input("Enter driver name: ")
destination = input("Enter destination: ")
distance = float(input("Enter distance (km): "))
fuel_consumption = float(input("Enter fuel consumption (L/100km): "))
fuel_price = float(input("Enter fuel price (KZT/L): "))

litres_needed = distance * fuel_consumption / 100
fuel_cost = litres_needed * fuel_price

if distance < 100:
    category = "Short trip"
elif distance < 500:
    category = "Medium trip"
else:
    category = "Long trip"

print("=" * 30)
print(f"Driver : {driver_name}")
print(f"Destination : {destination.upper()}")
print(f"Distance : {distance} km")
print(f"Fuel cost : {fuel_cost} KZT")
print(f"Category : {category}")
print("=" * 30)

print("Cost breakdown:")
for km in range(100, int(distance) + 1, 100):
    cost_so_far = (km * fuel_consumption / 100) * fuel_price
    print(f"{km} km \u2192 {cost_so_far} KZT")

print(f"Destination uppercase : {destination.upper()}")
print(f"Destination lowercase : {destination.lower()}")
print(f"Length : {len(destination)}")
print(f"Letter 'a' count : {destination.lower().count('a')}")
