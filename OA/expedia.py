cr = [[1,1], [1,2], [2,1], [2,2], [3, 3], [5,4], [4,5], [5,6]]
lines = []
for c, r in cr:
    lines.append(str(r) + ";" + str(c) + ";" + " ".join([str(i+1) for i in range(c*r)]))
for line in lines:
    rows, columns, nums = line.strip("\n").split(";")
    rows, columns, nums = int(rows), int(columns), nums.split(" ")
    while nums:
        i = 0 # initialize
        while i < columns and nums:
            i += 1
            print(nums.pop(0), end = " ")
        rows -= 1 # finished a row
        i = 0 # initialize
        while i < rows and nums:
            i += 1
            print(nums.pop(i * columns - i), end = " ")
        columns -= 1 # finished a column
        i = 0 # initialize
        while i < columns and nums:
            i += 1
            print(nums.pop(-1), end = " ")
        rows -= 1 # finished a row
        i = 0 # initialize
        while i < rows and nums:
            i += 1
            print(nums.pop((rows - i) * columns), end = " ")
        columns -= 1 # finished a column
