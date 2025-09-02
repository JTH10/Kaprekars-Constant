# Kaprekars-Constant
A calculator for Kaprekar's constant


## About Kaprekars Constant:
Kaprekar's constant, named after Indian mathematician D. R. Kaprekar, refers to the number 6174, which emerges from a fascinating process known as Kaprekar's routine. This routine reveals how a simple algorithm can lead to a fixed point, showcasing the elegance of number theory.

The process works as follows:

Start with any four-digit number that has at least two different digits.

Rearrange its digits to form the largest and smallest possible numbers.

Subtract the smaller number from the larger.

Repeat the process with the result.

This routine will always reach 6174 within at most seven iterations. Once 6174 is reached, the process becomes stable:
7641 − 1467 = 6174, repeating indefinitely.

Example:

Starting with 4321:

Descending: 4321

Ascending: 1234

Subtract: 4321 − 1234 = 3087

Next: 8730 − 0378 = 8352

Then: 8532 − 2358 = 6174

No matter the valid starting number, the routine converges to 6174, making it a simple yet surprising demonstration of deterministic behavior in mathematics.

This project implements Kaprekar’s routine programmatically, highlighting how concise logic and iteration can uncover mathematical patterns.


## About the Calculator:
This is a simple Python program that calculates Kaprekar's constant (6174) for any valid four-digit number using Kaprekar's routine.

### Prerequisites 
Before running the program, ensure that Python 3 is installed on your system.
You can download it from the official website: https://www.python.org/downloads/

### Usage 

To run the program, open a terminal and execute the script:

python3 kc.py <br/>

You will be prompted to enter a four-digit number. The program will then:

Rearrange the digits in descending and ascending order.

Subtract the smaller number from the larger.

Display each step of the calculation.

Repeat the process until it reaches Kaprekar's constant (6174).

### Example 
Here is an example of how to use the program:

$ python3 kc.py
Give me a 4 digit number: 1224
1224
4221 - 1224 = 2997
9972 - 2799 = 7173
7731 - 1377 = 6354
6543 - 3456 = 3087
8730 - 0378 = 8352
8532 - 2358 = 6174

### Limitations 
There are a few important constraints to keep in mind:

The number must be four digits long (numbers like 0999 or 100 will not work unless padded or validated properly).

It must contain at least two different digits. Numbers with all identical digits (e.g., 1111, 2222) will always subtract to zero, not 6174.

The process does not work with fewer than four digits without modification (though similar routines exist for 3-digit numbers and other bases).

The program includes basic input validation to ensure these conditions are met.
