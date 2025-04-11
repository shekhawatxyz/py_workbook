def room_area(l,h):
    return l*h

if __name__ == "__main__":
    print("Enter length")
    l = int(input())
    print("Enter width")
    h = int(input())
    area = room_area(l, h)
    print(area)
