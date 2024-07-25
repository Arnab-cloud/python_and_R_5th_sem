"""
    Check if a number if prime and the sum of the digits of that number is even;
    for all the number in the range(100, 200)
"""

def isPrime(num):
    root_num = int(num**0.5)
    for i in range(2, root_num + 1):
        if not num%i:
            return "not prime"
    return "prime"

def isSumDigitsEven(num):
    sum_digits = 0
    while num:
        sum_digits += num%10
        num //= 10
    if sum_digits % 2:
        return "not even"
    return "even"

for num in range(100, 200):
    final_ans = f"{num}"
    is_even = isSumDigitsEven(num)
    is_prime = isPrime(num)
    if is_even == "even" and is_prime == "prime":
        final_ans = '"' +final_ans + '"'
    print(f"{final_ans} is {is_prime} and sum of digits is {is_even}")
