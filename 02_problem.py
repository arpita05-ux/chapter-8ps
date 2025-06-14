

def f_to_c(f):
   return 5*(f - 32)/9.  # formula 

f = int(input("Enter temperature in F: "))
c = f_to_c(f)

print(f"{round(c, 2)}°C")     # inside print for round figure at two place we use round(c, 2)

