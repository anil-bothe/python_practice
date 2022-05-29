original_list = [2, 4, 6]
"""
result = []
for item in original_list:
    if item == 2:
        result.append(i)

print(result)

"""


# result = list(filter(lambda x: x == 2, original_list))

"""
result = []
for i in original_list:
    if i > 2:
        result.append(i)

"""

result = list(filter(lambda x: x > 2, original_list))

print(result)

