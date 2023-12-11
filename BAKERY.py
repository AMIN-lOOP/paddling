
prices = {"بربری": 5000, "لواش": 2000, "تافتون": 3000, "سنگگ": 4000, "باگت": 6000}

def get_user_info():
    full_name = input("لطفا نام و نام خانوادگی خود را وارد کنید: ")
    phone_number = input("لطفا شماره تماس خود را وارد کنید: ")
    return full_name, phone_number

def get_bread_order():
    while True:
        order = input("لطفا نوع نان مورد نظر خود را انتخاب کنید (بربری, لواش, تافتون, سنگگ, باگت): ")
        if order in prices:
            quantity = int(input(f"چند عدد نان {order} می‌خواهید؟ "))  
            return order, quantity  
        else:
            print("متاسفیم، نوع نان مورد نظر موجود نیست. لطفا نوع دیگری را انتخاب کنید.")

def main():
  
    user_name, user_phone = get_user_info()
    
    total_price = 0

    while True:
        bread, quantity = get_bread_order()  
        total_price += prices[bread] * quantity  
        more_order = input("آیا می‌خواهید نان دیگری سفارش دهید؟ (بله/خیر): ").lower()
        if more_order == "خیر":
            break
    
    print(f"خلاصه سفارش: {user_name} با شماره تماس {user_phone}")
    print(f"مجموع هزینه سفارش شما: {total_price} تومان است.")

if __name__ == "__main__":
    main()
