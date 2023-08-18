# Operator precedence describes the order in which operations are performed
# Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first
print((10 + 3) - (6 + 3))

# Multiplication * has higher precedence than addition +, and therefor multiplications are evaluated before additions
print(20+5*2)

# Note:If two operators have the same precedence, the expression is evaluated from left to right
print(15 + 4 - 9 + 3)

# The precedence order is described in the table below, starting with the highest precedence at the top
# Operator	               Description
#   ()	                   Parentheses	
#   **	                   Exponentiation	
#   +x  -x  ~x	           Unary plus, unary minus, and bitwise NOT	
#   *  /  //  %	           Multiplication, division, floor division, and modulus	
#   +  -	               Addition and subtraction	
#   <<  >>	               Bitwise left and right shifts	
#   &	                   Bitwise AND	
#   ^	                   Bitwise XOR	
#   |	                   Bitwise OR	
#   ==  !=  >  >=  <  <=   is  is not  in  not in 	Comparisons, identity, and membership operators	
#   not	                   Logical NOT	
#   and	                   AND	
#   or	                   OR