def levenshtein_distance(token1, token2):

    M = len(token1) + 1
    N = len(token2) + 1

    # Khởi tạo ma trận D với kích thước M x N, ban đầu tất cả các ô là '#'
    D = [["#" for _ in range(N)] for _ in range(M)]

    for j in range(N):
        D[0][j] = j
    for i in range(M):
        D[i][0] = i

    # Tính toán các giá trị cho các ô còn lại trong ma trận
    for i in range(1, M):
        for j in range(1, N):
            cost = 0 if token1[i - 1] == token2[j - 1] else 1
            D[i][j] = min(
                D[i - 1][j] + 1,
                D[i][j - 1] + 1,
                D[i - 1][j - 1] + cost,  # Thay thế ký tự
            )
    # distance = D[i][j]
    return D


def traceback(source, target, D):
    # Chiều dài của các chuỗi source và target
    M = len(source)
    N = len(target)

    # Biến để lưu các bước chỉnh sửa
    operations = []

    # Bắt đầu từ ô cuối cùng của ma trận D
    i, j = M, N

    while i > 0 or j > 0:
        if i > 0 and D[i][j] == D[i - 1][j] + 1:
            # Xóa ký tự từ source
            operations.append(f"Xóa '{source[i-1]}' từ source")
            i -= 1
        elif j > 0 and D[i][j] == D[i][j - 1] + 1:
            # Thêm ký tự vào target
            operations.append(f"Thêm '{target[j-1]}' vào sau '{source[i-1]}'")
            j -= 1
        else:
            # Thay thế ký tự
            if source[i - 1] != target[j - 1]:
                operations.append(f"Thay thế '{source[i-1]}' bằng '{target[j-1]}'")
            i -= 1
            j -= 1

    # Đảo ngược danh sách thao tác để có thứ tự từ đầu đến cuối
    operations.reverse()

    return operations


# Ví dụ sử dụng
source = "yu"
target = "you"

matrix = levenshtein_distance(source, target)

# In ma trận
print("Ma trận D:")
for row in matrix:
    print(row)

# Tìm đường đi và in ra các bước chỉnh sửa
print("\nCác bước chỉnh sửa:")
steps = traceback(source, target, matrix)
for step in steps:
    print(step)
