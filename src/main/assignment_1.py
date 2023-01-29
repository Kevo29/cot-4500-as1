binary = "010000000111111010111001"

x: float = 0 
y: float = 0 
def Question1(binary_string: str, value: float):

  if binary_string[0] == "1":
    sign: float = -1
  else: sign = 1

  exponent: float = float(int(binary_string[1:12], 2))
  mantissa: float = float(int(binary_string[12:], 2))

  value: float = sign * (1 + mantissa / 2**52) * 2**(exponent - 1023)
  x = value
  return round(x,5)


print(Question1(binary,x))
print("\n")

def Question2(binary_string: str):
  read = str(Question1(binary,x))
  if read[5] == "9":
    value = float(Question1(binary,x))
    value = round(value, 3)
  return value

print(Question2(binary))

print("\n")

def Question3(binary_string: str):
  read = str(Question1(binary,x))
  if read[3] == "9":
    value = float(Question1(binary,x))
    value = round(value, 3)
  return value

print(Question3(binary))
print("\n")


def Question4(absolute: float, relative: float):
  
  absolute = abs(Question1(binary,x)-Question3(binary))

  relative = abs(Question1(binary,x)-Question3(binary))/abs(Question1(binary,x))
  
  return absolute, relative

print(Question4(x,y))
print("\n")
