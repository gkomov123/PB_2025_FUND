file_path = input().split("\\")

for string in file_path:
    if "." in string:
        file_name, extension = string.split(".")
        print(f"File name: {file_name}")
        print(f"File extension: {extension}")
