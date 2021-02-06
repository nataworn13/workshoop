# 1.จงเขียนตารางสูตรคูณให้ผลลัพท์ที่ออกมาเป็นแบบตัวอย่างด้านล่างโดยใช้คำสั่ง while

number = 2
mutiple = 1

while number < 13:
    print("[ ", number, " ]")
    while mutiple < 13:
        print(number, " * ", mutiple, " = ", number * mutiple)
        mutiple = mutiple + 1
    print("---------------------")
    print()
    number = number + 1
    mutiple = 1