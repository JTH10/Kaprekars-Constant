import string
import math
import re


def main():

    while True:
        num = input("Give me a 4 digit number: ")
        #if len(num) == 4 and num.isdigit() and num != "0000" and num != "1000" and num != "0100" and num != "0010" and num != "0001" and num != "9998" and num != "8889":
        #if is_valid_number(num):
        temp_num = sorted(num)
        temp_num_rev = sorted(num,reverse=True)
        #temp_num = ''.join(temp_num)
        pattern = re.compile(r"^(?!(000[01]|111[0-2]|222[1-3]|333[2-4]|444[3-5]|555[4-6]|666[5-7]|777[6-8]|888[7-9]|999[89]))\d{4}$")
        if pattern.match(''.join(temp_num)) and pattern.match(''.join(temp_num_rev)):
            print(num)
            break
        else:
            print("Invalid input. Try again.")

 
#Stumped...Figure out how to convert a int into a string.
    while True:
        temp_y = sorted(num)
        temp_x = sorted(num,reverse=True)
        new_num = kaprekars_f(num)
        print( ''.join(temp_x), "-", ''.join(temp_y), "=", new_num)
        num = new_num

        if new_num == "6174" or new_num == "0":
            break


def kaprekars_f(n):
   x2 = sorted(n, reverse=True)
   y2 = sorted(n)
   y1 = "".join(y2)
   x1 = "".join(x2) 
   y = int(y1)
   x = int(x1)
   if y > x:
        z = y - x
        return str(z)
   else:
        z = x - y
        return str(z)


#def is_valid_number(number):
#    pattern = re.compile(r'^(?!(\d)\1{3})(?!(\d)\d\1(?:\1[+-]1|[+-]\d\1))\d{4}$')
#    return True if pattern.match(number) else False
    
if __name__ == '__main__':
    main()
