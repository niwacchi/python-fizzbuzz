class FizzBuzz:
  def __init__(self,limit):
    self.limit = limit;

  def output(self):
    for i in range(self.limit):
      if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
      elif i % 3 == 0:
        print("Fizz")
      elif i % 5 == 0:
        print("Buzz")
      else:
        print(i)

fizzBuzz = FizzBuzz(20)
fizzBuzz.output()
   
