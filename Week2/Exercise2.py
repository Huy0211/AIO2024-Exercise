# Hàm đếm chữ
def count_characters(string):
    character_count = {}

    # Chuyển chuỗi sang dạng viết thường
    string = string.lower()

    # Vòng for chạy từng chữ trong chuỗi (Nếu key đã tồn tại thì +1, nếu không thì gán =1)
    for key in string:
        if key in character_count:
            character_count[key] = character_count[key] + 1
        else:
            character_count[key] = 1
    return character_count


string = 'Happiness'
print(f'{string}: {count_characters(string)}')

string = 'smiles'
print(f'{string}: {count_characters(string)}')
