#Project Description
"""
Sal's Shipping
Sal runs the biggest shipping company in the tri-county area, Sal’s Shippers. Sal wants to make sure that every single one of his customers has the best, 
and most affordable experience shipping their packages.
In this project, you’ll build a program that will take the weight of a package and determine the cheapest way to ship that package using Sal’s Shippers.
Sal’s Shippers has several different options for a customer to ship their package:

-Ground Shipping, which is a small flat charge plus a rate based on the weight of your package.
-Ground Shipping Premium, which is a much higher flat charge, but you aren’t charged for weight.
-Drone Shipping (new), which has no flat charge, but the rate based on weight is triple the rate of ground shipping.

"""
weight = 41.5

#Ground Shipping
if weight <= 2:
  cost = weight * 1.50 + 20.00
elif weight > 2 and weight <=6:
  cost = weight * 3.00 + 20.00
elif weight > 6 and weight <= 10:
  cost = weight * 4.00 + 20.00
else:
  cost = weight * 4.75 + 20.00

ground_shipping = cost
print(f"Ground Shipping: ${cost:.2f}")

#Premium Shipping
premium_ground_shipping = 125.00
#print(f"Ground Shipping Premium: ${premium_ground_shipping:.2f}")

#Drone Shipping
if weight <= 2:
  cost = weight * 4.50 
elif weight > 2 and weight <=6:
  cost = weight * 9.00
elif weight > 6 and weight <= 10:
  cost = weight * 12.00
else:
  cost = weight * 14.25

drone_shipping = cost
print(f"Drone Shipping ${drone_shipping:.2f}")

if  ground_shipping > drone_shipping:
  print(f"Drone Shipping(Cheap) ${drone_shipping:.2f}")
else:
  print(f"Ground Shipping(Cheap) ${ground_shipping :.2f}")
