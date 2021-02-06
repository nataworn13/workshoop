# 2.จงเขียนตารางสูตรคูณให้ผลลัพท์ที่ออกมาเป็นแบบตัวอย่างด้านล่างโดยใช้คำสั่ง for

for num in range(2, 13):
    print("    [", num, "]")
    for multi in range(1, 13):
        print(num, " * ", multi, " : ", num * multi)
    print("-------------------")