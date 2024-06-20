# Hàm đếm chữ trong 1 file txt
def word_count(filename):
    word_count = {}
    # Đọc file
    with open(filename, 'r', encoding="utf-8") as f:
        lines = f.readlines()
        # Duyệt từng dòng của file
        for line in lines:

            # Chuyển thành viết thường và xoá dấu câu
            line = line.lower()
            line = line.replace(',', '').replace(
                '.', '').replace('?', '').replace('!', '')

            # Tạo list từ các chữ trong dòng
            word_in_line = line.split()

            # Vòng for đếm từ
            for word in word_in_line:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
    return word_count


filename = 'C:\Users\USER\Desktop\AIO2024\AIO2024-Exercise\Week2\P1_data.txt'
print(word_count(filename))
