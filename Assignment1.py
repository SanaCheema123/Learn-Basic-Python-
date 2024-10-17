#(A + B - C * D) + (A / B / C / D) / (first * second * second)
A=45
B=24
C=23
D=42
first=11
second=41
third=14
#solving above equation using post method
#1st Method 
result=(A + B - C * D)
#A + B - C * D) + (A / B / C / D)
result=result+ (A / B / C / D)
#(A + B - C * D) + (A / B / C / D) / (first * second * second)
result=result/ (first * second * second)
print(result)
#solving above equation using post method
#2nd Method
result=(A + B - C * D)
#A + B - C * D) + (A / B / C / D)
result+= (A / B / C / D)
#(A + B - C * D) + (A / B / C / D) / (first * second * second)
result/=(first * second * second)
print(result)
#3rd Method 
result=((A + B - C * D) + (A / B / C / D) / (first * second * second))
print(result)