#Ride Cost Calculator   
"""Assume you travel 80 km to and fro in a day. 
    Cost of Diesel per litre is 80 INR 
    Your vehicle Fuel Average is 18 km/litre. 
    Now calculate the cost of driving per day to office.
    Take the distance travelled, cost of diesel and Fuel Average from input  """
#submitted by: Chirag Singh from Noida
#University roll no.:- 1813313036
    

distanceTravelled=float(input("Enter Distance Travelled by you per day(in km): "))
dieselCost=float(input("Enter cost of Diesel(in Rs/litre): "))
fuelAverage=float(input("Enter your vehicle Fuel Average(in km/litre): "))
dieselUsed=distanceTravelled/fuelAverage
costPerday=dieselUsed*dieselCost
print("Cost of driving per day to office: Rs.",costPerday,"/-")
