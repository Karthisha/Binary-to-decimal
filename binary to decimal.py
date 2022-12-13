def binary_to_decimal(binary):
  decimal = 0
  index = 0
  while binary > 0:
    digit = binary % 10
    decimal += digit * (2 ** index)
    binary = binary // 10
    index += 1
    
  return decimal
print(binary_to_decimal(1010))  
print(binary_to_decimal(10001)) 
print(binary_to_decimal(110101))  
