class Vector2():

	def __init__(self, x, y):
		self.x = float(x)
		self.y = float(y)

	def __str__(self):
		return "<{}, {}>".format(self.x, self.y)

	def __add__(self, other):
		return Vector2(self.x + other.x, self.y + other.y)

	def __sub__(self, other):
		return Vector2(self.x - other.x, self.y - other.y)

	def __mul__(self, scalar):
		if not type(scalar)	in [float, int]:
			raise TypeError('Scalar needs to be a number')
		else:
			return Vector2(self.x * scalar, self.y * scalar)

	def __div__(self, scalar):			
		return Vector2(self.x / scalar, self.y / scalar)		

my_vec = Vector2(10, 10)