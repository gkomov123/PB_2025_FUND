def is_palindrome(numbers:str) -> bool:
    return numbers == numbers[::-1]


number_input = input().split(", ")
for number in number_input:
    print(is_palindrome(number))