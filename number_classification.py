numbers_input = list(map(int, input().split(", ")))

positive = [num for num in numbers_input if num >= 0]
negative = [num for num in numbers_input if num < 0]
even = [num for num in numbers_input if num % 2 == 0]
odd = [num for num in numbers_input if num % 2 == 1]

print("Positive:", ", ".join(map(str, positive)))
print("Negative:", ", ".join(map(str, negative)))
print("Even:", ", ".join(map(str, even)))
print("Odd:", ", ".join(map(str, odd)))