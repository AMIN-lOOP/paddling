poems = [
    {"poem": "مرا در منزل جانان چه امید است که راه است / بدین قرار که من دارم او دارد بهانه ای", "poet": "خیام"},
    {"poem": "در نهاد ما تا چه مانده است جای / یا رب این چه سودا و این چه رای است", "poet": "مولوی"},
    {"poem": "من آن غریبم که دیر زمانیست / به کوی دوست درویش بمانیست", "poet": "حافظ"}
]

for d, poem_info in enumerate(poems):
    print(f"شعر {d + 1}:")
    print(poem_info["poem"])
    print()
    
    guess = input(f"نام شاعر شعر شماره {d + 1} را حدس بزنید: ")
    
    if guess == poem_info["poet"]:
        print("درست حدس زدید!")
    else:
        print(f"متاسفانه اشتباه است. شاعر این شعر {poem_info['poet']} است.")
    
    print() 
