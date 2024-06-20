# Hàm tìm max trong sliding window bằng slicing solution
def max_list(num_list, k):
    max_list = []
    for i in range(len(num_list)):
        # Kiểm tra độ dài của sliding window nếu = k thì thêm max vào max_list[]
        if len(num_list[i: i+k]) == k:
            max_list.append(max(num_list[i: i+k]))
    return max_list


num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
print(max_list(num_list, k))
