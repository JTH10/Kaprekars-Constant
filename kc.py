# Kaprekar's Constant finder (6174 routine)

def is_valid(num): 
    # Validate input: must be a 4-digit number with at least two unique digits
    return len(num) == 4 and num.isdigit() and len(set(num)) > 1
 
def kaprekars_f(n):
    # Perform one step of Kaprekar's routine by subtracting descending number from ascending number.
    desc = int(''.join(sorted(n, reverse=True))) 
    asc = int(''.join(sorted(n))) 
    result = desc - asc 
    return str(result).zfill(4)  # Ensure result is 4 digits with leading zeros

def main():
    while True: 
        num = input("Enter a 4-digit number (at least two different digits): ") 
        if is_valid(num): 
            break 
        print("Invalid input. Please try again.")

    steps = 0 
    while num != "6174": 
        x = ''.join(sorted(num, reverse=True)) 
        y = ''.join(sorted(num)) 
        new_num = kaprekars_f(num) 
        print(f"{x} - {y} = {new_num}") 
        num = new_num 
        steps += 1 
        
    print(f"You've reached Kaprekar's constant in {steps} steps!")
    
if __name__ == '__main__':
    main()
