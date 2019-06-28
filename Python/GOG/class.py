class Cat:
  def __init__(self):
    print("The object is created and the class is initialized")

  def amit(self, color, legs):
    self.color = color
    print("This is in the user-defined function")
    self.legs = legs

jangra = Cat()

print("\n\nThis is after initialization")

jangra.amit("silver", 23)