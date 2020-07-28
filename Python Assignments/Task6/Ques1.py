# Write a program in Python to allow the error of syntax to go in exception. HINT: use SyntaxError
try:
    eval("print 'add'")
except SyntaxError:
    print ('MUHAHA THIS IS A ERROR')
