string_input = input()
count = int(input())

def string_repeat(string:str, repeat:int) -> str:
    return string * repeat

print(string_repeat(string_input, count))