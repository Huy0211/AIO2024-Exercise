def edit_distance(text1, text2):
    # Tạo ma trận khoảng cách có kích thước (len(text1) + 1) x (len(text2) + 1)
    # Khởi tạo hàng và cột đầu tiên để biểu thị chi phí xóa tất cả các ký tự khỏi một
    # chuỗi hoặc chèn tất cả các ký tự từ chuỗi kia.
    distance = [[i for i in range(len(text2) + 1)]] + \
        [[0] + [j for j in range(1, len(text1) + 1)]]

    # Lặp lại ma trận, tính toán khoảng cách chỉnh sửa tối thiểu cho mỗi ô.
    for i in range(1, len(text1) + 1):
        for j in range(1, len(text2) + 1):
            if text1[i - 1] == text2[j - 1]:
                # Không cần chỉnh sửa nếu ký tự giống nhau
                distance[i][j] = distance[i - 1][j - 1]
            else:
                # Chi phí tối thiểu cho việc xóa, chèn hoặc thay thế
                distance[i][j] = min(
                    distance[i - 1][j], distance[i][j - 1], distance[i - 1][j - 1]) + 1

    return distance[len(text1)][len(text2)]


text1 = 'hola'
text2 = 'hello'
distance = edit_distance(text1, text2)
print(f"Edit distance between '{text1}' and '{text2}': {distance}")
