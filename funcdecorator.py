print("OM AJIT SOLANKI")
class Numbers:
  multiplier=int(input("Enter a number :"))
  def __init__(self, x, y):
    self.x=x
    self.y=y
  def add(self):
      return self.x+self.y
  @classmethod
  def multiply(self,a):
      return a*self.multiplier
  @staticmethod
  def subtract(b,c):
      return b-c
  @property
  def value(self):
      pass
  @value.getter
  def value(self):
      return(self.x,self.y)
  @value.setter
  def value(self,xy_tuple):
      self.x,self.y=xy_tuple
      self.x*=100
      self.y*=100
  @value.deleter
  def value(self):
      print("Deleting Values")
      del self.x
      del self.y
n=Numbers(10,20)
print("Sum=",n.add())
print("Product=",n.multiply(10))
print("Difference=",n.subtract(5,3))
a,b=n.value
print(a,b)
n.value=9,6
a,b=n.value
print(a,b)
del n.value
