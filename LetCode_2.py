def move_zeros(data: list) -> list:
    size = len(data)
    left = right = 0
    while right < size:
        if data[right] == 0:
            right += 1
        else:
            data[left], data[right] = data[right], data[left]
            right += 1
            left += 1
    return data


if __name__ == "__main__":
    arr = [1, 2, 0, 0, 3, 4, 0, 0, 0, 7]
    print(move_zeros(data=arr))