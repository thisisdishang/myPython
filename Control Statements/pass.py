# The pass Statement:
"""if statements cannot be empty, but if you for some reason have an if statement with no content,
put in the pass statement to avoid getting an error"""
"""The pass statement is used as a placeholder for future code. When the pass statement is executed, nothing happens,
but you avoid getting an error when empty code is not allowed."""
# Empty code is not allowed in loops, function definitions, class definitions, or in if statements
# If we do not use pass or simply enter a comment or a blank here, we will receive an IndentationError error message
w=150
x=100
if w>x:
    pass