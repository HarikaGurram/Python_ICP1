def reverseofastring(input_str_new):

    return input_str_new[::-1]

input_str = input('Please enter the input string : ')
start = 3
stop = 4

if len(input_str) > stop:
    input_str_new = input_str[0:start:] + input_str[stop + 1::]
   
print ("String after removal of two characters is : " + input_str_new)

reverse_output = reverseofastring(input_str_new)

print("String after reversing the characters is : " + reverse_output)

