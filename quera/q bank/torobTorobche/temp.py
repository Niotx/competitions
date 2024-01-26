def is_convertible(n, table1, table2):
    # Initialize dictionaries to count the occurrences of numbers in both tables
    count_table1 = {i: 0 for i in range(1, n * n + 1)}
    count_table2 = {i: 0 for i in range(1, n * n + 1)}

    # Count the occurrences of numbers in the first table
    for row in table1:
        for num in row:
            count_table1[num] += 1

    # Count the occurrences of numbers in the second table
    for row in table2:
        for num in row:
            count_table2[num] += 1

    # Compare the counts of occurrences for each number
    for num in range(1, n * n + 1):
        if count_table1[num] != count_table2[num]:
            return "NO"

    return "YES"

# Input the number of scenarios
t = int(input())
results = []

# Process each scenario
for _ in range(t):
    n = int(input())
    table1 = [list(map(int, input().split())) for _ in range(n)]
    table2 = [list(map(int, input().split())) for _ in range(n)]
    result = is_convertible(n, table1, table2)
    results.append(result)

# Output the results for each scenario
for result in results:
    print(result)
