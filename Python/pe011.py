#Author - Jamie Woods
#https://projecteuler.net/problem=11


L01 = "08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08"
L02 = "49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00"
L03 = "81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65"
L04 = "52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91"
L05 = "22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80"
L06 = "24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50"
L07 = "32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70"
L08 = "67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21"
L09 = "24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72"
L10 = "21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95"
L11 = "78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92"
L12 = "16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57"
L13 = "86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58"
L14 = "19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40"
L15 = "04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66"
L16 = "88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69"
L17 = "04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36"
L18 = "20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16"
L19 = "20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54"
L20 = "01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"

DIMENSIONS = 20
NUM_ADJACENT = 4


def main():
    data_grid = get_data_grid()
    solution = find_highest_product(data_grid)
    print("The solution to problem 11 is " + str(solution))


def get_data_grid():
    data_grid = []
    for x in range(1, (DIMENSIONS + 1)):
        x = str(x)
        leading_zero = "0" + x if len(x) == 1 else x
        var_name = "L" + leading_zero
        data_row = globals()[var_name]
        formatted = get_formatted_data_row(data_row)
        data_grid.append(formatted)
    return data_grid


def get_formatted_data_row(unformatted):
    split = unformatted.split()
    output = []
    for x in split:
        output.append(int(x))
    return output


def find_highest_product(data_grid):
    current_highest = 0
    for row in range(0, DIMENSIONS):
        for col in range(0, DIMENSIONS):
            horizontal_buffer = []
            vertical_buffer = []
            left_diag_buffer = []
            right_diag_buffer = []
            for depth in range(0, NUM_ADJACENT):
                right_hori_x = col + depth
                left_hori_x = col - depth
                verti_y = row + depth

                if inside_limit(right_hori_x):
                    current_highest = calculate_product(horizontal_buffer, current_highest, data_grid[row][right_hori_x])
                if inside_limit(verti_y):
                    current_highest = calculate_product(vertical_buffer, current_highest, data_grid[verti_y][col])
                if inside_limit(left_hori_x) and inside_limit(right_hori_x) and inside_limit(verti_y):
                    current_highest = calculate_product(left_diag_buffer, current_highest, data_grid[verti_y][left_hori_x])
                    current_highest = calculate_product(right_diag_buffer, current_highest, data_grid[verti_y][right_hori_x])
    return current_highest


def inside_limit(num):
    if DIMENSIONS > num > 0:
        return True
    else:
        return False


def calculate_product(buffer, highest, current):
    if current == 0:
        return highest
    buffer.append(current)
    if len(buffer) == NUM_ADJACENT:
        prod = product_of_buffer(buffer)
        if prod > highest:
            highest = prod
        buffer.pop(0)
    return highest


def product_of_buffer(buffer):
    prod = 0
    first = True
    for x in buffer:
        if first:
            prod += x
            first = False
            continue
        prod *= x
    return prod


#Overwrite values to create a smaller, easier to test grid
def test():
    global DIMENSIONS
    DIMENSIONS = 6
    global NUM_ADJACENT
    NUM_ADJACENT = 3
    global L01
    L01 = "01 02 03 04 05 06"
    global L02
    L02 = "01 02 03 04 05 06"
    global L03
    L03 = "01 02 03 04 05 06"
    global L04
    L04 = "01 02 03 04 05 06"
    global L05
    L05 = "01 02 03 04 05 06"
    global L06
    L06 = "01 02 03 04 05 06"
    
    test_grid = get_data_grid()
    for row in test_grid: #should print 6 arrays with elements 1-6
        print(row)
    highest_product = find_highest_product(test_grid)
    print("The test solution is " + str(highest_product) + "; expected 216")


if __name__ == "__main__":
    main()
