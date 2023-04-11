# Kaprekars-Constant
A calculator for Kaprekar's constant


## About Kaprekars Constant:

Kaprekar's constant is a mathematical concept named after the Indian mathematician D.R. Kaprekar. It is also known as the 6174 or the Kaprekar's routine.

The constant is derived from the process of repeatedly subtracting the smallest number that can be formed from a four-digit number created by arranging its 
digits in descending order from the largest number that can be formed by arranging its digits in ascending order. For example, starting with the number 
4321, the process would be as follows:


Arrange the digits in descending order: 4321

Arrange the digits in ascending order: 1234

Subtract the smaller number from the larger number: 4321 - 1234 = 3087

Repeat the process with the result: 8730 - 0378 = 8352 - 2358 = 6174


The process will always result in the number 6174 after at most 7 iterations, regardless of the starting number. Once 6174 is reached, the process will 
continue to produce the same result of 6174 with each subsequent iteration.

Kaprekar's constant is interesting because it demonstrates how even simple mathematical processes can lead to complex and unexpected results.





## About the Calculator:
This is a Python program that calculates Kaprekar's constant for a given four-digit number.

### Prerequisites 

Before running the program, you need to make sure that Python 3 is installed on your computer. If it is not, you can download it from the official 
Python website: https://www.python.org/downloads/

### Usage 

To use the program, simply run the kc.py file from the command line:

python3 kc.py <br/>
You will be prompted to enter a four-digit number. Once you enter the number, the program will arrange the 4 digits in both ascending and desending 
order, subtract the smaller number from the larger, print the results and repeat until Kaprekar's constant(6174) is reached.

### Example 
Here is an example of how to use the program:

python3 kc.py <br/>
Give me a 4 digit number: 1224 <br/>
1224 <br/>
4221 - 1224 = 2997 <br/>
9972 - 2799 = 7173 <br/>
7731 - 1377 = 6354 <br/>
6543 - 3456 = 3087 <br/>
8730 - 0378 = 8352 <br/>
8532 - 2358 = 6174


### Limitations 
There are some limitations to the 4 digit numbers that can be used to achieve Kaprekar's constant. If 3 of the 4 digits are the same, the 4th digit can 
not also be the same, or 1 digit greater or less than the other 3 repeating digits. for example, 1111, 1112 & 1113 will not work.

