import random

first_name = input('first name: ')
print(" ")

last_name = input('last name: ')
print(" ")

fal_hafez = [
    'به یاد آر ز جوانی دف قَدَح کز بهر ما',
    'با دل شکسته هر که نشست ز پیش خود رفت',
    'خواجه تو بشنو از من پندی که سخت کارگر است',
    'دل مرده را چه حاجت که صد چاکر و چاک',
    'عشق تو در نهانخانه جان ما نشسته است',
    'نسیمی که ز کوی دوست امروز وزیدن گرفت',
    'چون صبح دمید خنک نسیم صبا بنافه',
    'دلا بجز عشق اگر کاریست بیخودی مکن',
    'پند مردم چو تو دانا چه حاجت که شنوی',
    'هر آنچه هست در این بزم میناست به مینا',
    'چه خوش گفت آن نکو سخن که یاران چو رختند',
    'برای رفتن به مسجد و منزل واگذاشتن',
    'به یاد آور که بر تازیانه‌ی دهر عجب می‌زدی',
    'بیا تا گل برافشانیم و می در ساغر اندازیم',
    'گره از کار ما بگشای خوش بستهٔ حافظ',
    'دوش گفتم به فلک کاین چرخ فلک دوار',
    'ابروی تو کمان از غمزه و کین افگن',
    'بلبلی بشنیدم که می‌نالید بکام صبح',
    'زلف تو چون بشد از غُبار غم بیرون',
    'بنال حافظ شبی چند زین فراق ولیکن',
    'دل الفت زده در عشق رخت ز رخ اندر',
    'دست از طلب ندارم تا کام من برآید',
    'یاد باد آنکه گفت ما را روزی',
    'خبر داری که چرخ فلک خورشید نو آرد',
    'خیال روی تو از دل و جان ما فزون است',
    'به هر روزی که از درگاه لطفش گذریم',
    'سر پیاله نهان کن که از دیدهٔ چران',
    'به رندان می گرفتار فرمای فروغ بخش',
    'با باده نشستن قدری از سروری است',
    'من اندر هوای روی تو بی تاب و قرارم'
]

selected_fal = random.choice(fal_hafez)
print(" ")

print("Horoscope ready: ")
print(" ")

print(selected_fal)
