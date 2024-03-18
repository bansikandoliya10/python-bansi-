#does not support array[list]
cars = ["namo","nanoxl"]
cars[0] = "banny"
print (cars[0])
print (len(cars))
cars.append("honda")
cars.append("honda1")
cars.pop(0)
cars.remove("honda1")
for x in cars:
    print (x)