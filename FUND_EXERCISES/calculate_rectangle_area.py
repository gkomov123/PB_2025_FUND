rect_width = int(input())
rect_height = int(input())

def rect_area(width:int, height:int) -> int:
    return width * height

result = rect_area(width=rect_width, height=rect_height)
print(result)