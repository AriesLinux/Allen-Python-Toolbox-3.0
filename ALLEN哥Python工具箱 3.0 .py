print("*************************")
print("        HELLO SIR        ")
print("  This is an tools box   ")
print("    You can choose ONE   ")
print("*************************")

print()
print("1. BMI Tools (VIP)")
print("2. ENG AVG Tools (Free)")
print("3. Travel Plan TimeTable (Free)")
print("4. Purchase Amount (Free)")
print("5. Personal DATA card (Free)")
print()


choose = input("Your choose: ")

if choose == "1":
    print()
    print("Okey Get!!!")
    print("Your Choose is 1.")
    print("BMI Tools Loading")
    import time
    total_length = 50

    print("加载中...")

    for i in range(total_length + 1):
       percent = (i / total_length) * 100
       bar = '#' * i + '-' * (total_length - i)
       print(f"\r[{bar}] {percent:.2f}%", end='')
       time.sleep(0.2)

    print("\n加载完成！")
    
    print("您好，欢迎使用BMI工具 BY ALLEN")
    print()
    kg = int(input("请输入您的体重（Kg）："))
    print()
    highest = float(input("请输入您的身高（M）："))
    print()
    print("好的已经收到您的选择")
    print("请等待结果出来")
    import time
    total_length = 50

    print("加载中...")

    for i in range(total_length + 1):
       percent = (i / total_length) * 100
       bar = '#' * i + '-' * (total_length - i)
       print(f"\r[{bar}] {percent:.2f}%", end='')
       time.sleep(0.2)
    
    BMI = kg/highest*2
    name = input("HI，结果已经出来，请输入您的姓名：")
    tel = input("您好，请输入您的电话：")
    print()
    print("好的，请联系ALLEN哥，以获得您的BMI指数以及体脂报告，请支付50元")
    KEY = input("如果您已经购买密钥，请输入您的购买密钥以解锁您的BMI")
    if KEY == "ALLENBMIPRO":
        print("感谢您的购买,多谢你支持我的Python事业")
        print("这个就是您的体脂检测报告：")
        print()
        print()
        print("**********************************")
        print("             你好",name            )
        print("         您的BMI：",BMI            )
        print("         您的电话：",tel           )
        
elif choose == "2":
     print()
     print("Okey Get!!!")
     print("Your Choose is 2.")
     print("ENG AVG Tools Loading")
     import time
     total_length = 50

     print("加载中...")

     for i in range(total_length + 1):
       percent = (i / total_length) * 100
       bar = '#' * i + '-' * (total_length - i)
       print(f"\r[{bar}] {percent:.2f}%", end='')
       time.sleep(0.2)

     print("\n加载完成！")
     print("您好，欢迎使用英文平均分计算工具 BY ALLEN")
     print()
     
     marks = []  
     i = 0  
     avg = 0  
     while True:
         eng = int(input("输入您的英文成绩，当你要看到平均分计算结果时，请输入[-1]: "))
         if eng == -1: 
             break
         marks.append(eng)
         i =i + 1 
     if marks: 
         avg = sum(marks) / len(marks) 
         print(f"平均分是: {avg:.2f}")
         
     else:
        print("没有输入任何成绩！")


elif choose == "3":
    print("好的，您选择了旅游计划表")
    print()
    
    mudidi = input("请输入目的地：")
    day = input("请输入行程天数：")
    fee = int(input("请输入预算（HKD）："))
    startdate = input("请输入出发日期：")
    people = int(input("请输入同行人数："))


    avange = 0
    avange = fee/people;

    print("                             ")
    print("========  旅游计划表 ========")
    print("目的地：",mudidi)
    print("出发日期：",startdate)
    print("行程天数：",day,"天")
    print("同行人数：",people,"人")
    print("总预算：HKD",fee)
    print("每人平均预算：HKD",avange)
    print("=============================")


elif choose == "4":
    a = int(input("Enter purchase amount: "))
    membership = input("Enter membership Type   VIP👑 (v) /Regular😏 (r) / Non-member🚫 (n):  ").lower()
 
    if membership == "n":
       print("Your membership is 😏Non-member😏")
       if a >= 1000:
          final_amount = a * 0.9
       else:
          final_amount = a

    elif membership == "v":
       print("Your membership is 👑VIP👑")
       if a >= 1000:
         final_amount = a * 0.8
       else:
         final_amount = a * 0.9

    else:
      print("Your membership is #Regular")
      print("   🚫*OR NO ENTER*🚫       ")
      if a >= 1000:
        final_amount = a * 0.85
      else:
        final_amount = a * 0.95

    print("##############################")
    print("#                            #")
    print(f"Final amount: ${final_amount}")
    print("#                            #")
    print("##############################")


elif choose == "5":
   name = input("HI,Please Enter your name?")
   age = int(input("Please Enter your age?"))
   highest = int(input("Please Enter your highest?(CM)"))
   favourite = input("Please Enter your favourite?")


   print("======Persoal DATA card========")
   print("Name:",name)
   print("Age:",age)
   print("Highest:",highest,"cm")
   print("Your favourite:",favourite)
   print("===============================")













else:print("*** Is look at you arr not Enter any things OR Not Enter 1-5.. ***")

