import random
while True:
    so_bi_mat = random.randint(1,100)
    so_lan_doan = 0
    while True:
        so = int(input("Mời người dùng nhập số (1 - 100): "))
        so_lan_doan+=1
        if so == so_bi_mat:
            print("Chúc mừng, bạn đã đoán đúng số bí mật!")
            break
        elif so > so_bi_mat:
            print("Nhỏ hơn chút!")
        elif so < so_bi_mat:
            print("Lớn hơn chút!")
        if so_lan_doan >= 10:
            print(f"Bạn đã hết lượt đoán, GAME OVERRRR!")
            break
        else:
            print(f"Còn {10 - so_lan_doan} lượt")
    choi_lai = input("Bạn có muốn chơi lại không? (co / khong): ").strip().lower()
    if choi_lai != "co":
        break