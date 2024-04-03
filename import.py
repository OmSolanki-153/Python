print("OM AJIT SOLANKI")
import geometry
def pointShapeVolume(x,y,squareBase):
    if squareBase:
        base = geometry.squareArea(x)
    else:
        base = geometry.circleArea(x)
    return y*base/3
for i in dir(geometry):
    print(i)
print("\n Volume of Square = ",pointShapeVolume(1,5,True))
print("\n Volume of Circle = ",pointShapeVolume(1,5,False))
