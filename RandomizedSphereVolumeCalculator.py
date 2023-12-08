import random
from fractions import Fraction
import math

for _ in iter(int, 1):
	SmallFloat = float(input("Insert a small float: "))
	LargeFloat = float(input("Insert a large float: "))

	GeneratedFloat = float(random.uniform(SmallFloat, LargeFloat))
	print(GeneratedFloat)
	FourThirds = Fraction(4, 3)
	Pie = 3.14
	OutputtedFloat = float(float(FourThirds) * float(Pie) * math.pow(GeneratedFloat, 3))
	print(OutputtedFloat)