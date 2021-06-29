delimiter  = "*"
# ord() или chr()
A = [False, False, True, True]
B = [False, True, False, True]

header = "* A *" + " B " + "*"+" A and B "+ "*"

table_width = len(header)
# print (logical_A and logical_B)

print(delimiter * table_width)
print(header)
print(delimiter * table_width)

for lineNum in range(len(A)):
  inp_str = "* "+str(int(A[lineNum]))+" * "+str(int(B[lineNum]))+" *    "+str(int(A[lineNum] and B[lineNum]))+"    *"
  print(inp_str)
  print(delimiter * table_width)
