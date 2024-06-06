from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup

# Токен бота
BOT_TOKEN = "7372628238:AAGkkSpywcbDjQuGrTn5_IC2G0m5trY5h-E"


desc_1 = """
Примечание ⤵️ 
 Аккаунт со 2 СЕЗОНА
👑 Уровень аккаунта:  64
🛍 Редкие скины:
Косички 
Котёнок питомец
Верх спортивного костюма 
Верх гонщик красно-черный
Миф. Маска вторжение
Миф. Костюм Йор (spy family) 

Скины на транспорт :
Tesla Roadster 🩷
УАЗ Сыр 
Spy family дача

Прокачки : 
М416 лёд (1 уровень) 
М416 рёв ящера (4 уровень) 
Стилет Семья шпиона йор ( 3 уровень) full
Фамас первозданный свет (1 уровень) 
Томпсон (1 уровень) 
Арбалет кошмарный цирк (3 уровень)full
Скорпион золотой шифр (2 уровень) 
М762 любовный концерт ( 7 уровень) full
Aкm драконья маскировка (1 уровень) 
М762 8-битныф пони (1 уровень) 
МG3 дракон (1 уровень)
"""

desc_2 = """
Уровень:  71
Внешность: FULL.
Завоеватель есть.

Костюмы ⬇️ : 
MIF костюм «Вторжение»
MIF костюм «Ледник»
MIF костюм «Чёрная акула»
MIF костюм «Рок-звезда»
MIF костюм «Мумия» 
MIF костюм «Стильный убийца»
MIF костюм «Зимняя королева»
MIF костюм «Особый PMGC»
MIF костюм «Брюс ли»
Костюм «Black pink»
MIF шлем «Звездный след»
MIF шлем «Рок звезда»
MIF маска «Лучник-скелет»
MIF маска «Вторжение» 
Шлем «Ледник»

Скины на 🚘⬇️ : 
рб Maserati (+ киллчат красная)
"""

desc_3 = """
👑 Уровень аккаунта: 55

👑Золотой костюм - восставший из пламени 
👑Золотой костюм - ледяная невеста 
👑Золотой головной убор - крылья ночи 
👑Золотая маска - восставший из пламени

🔘MIF Шлем - Inferno 
🔘MIF Костюм + эмоция - гладиатор
🔘MIF Костюм + эмоция - вторжение 
🔘MIF Костюм + эмоция - морской змей
🔘MIF Костюм + эмоция - стильный убийца 

❗3 ДОДЖА ❗

🔘Прокачиваемые оружия:
М416 рев ящера - 6ур 
М416 шут - 7ур (фулл)
М762 крылья ночи - 4ур
Юмп 8 бит - 4 ур 
Дп28 дракон из нефрита - 3ур
Юмп - 2ур
AKM - пиратское золото - 4ур (озолочен)
Бизон - 2ур
"""

# Словарь данных для продажи (пример)
accounts_data = [
    {"login": "kakasho313@mail.ru", "password": "wowowowo1212", "price": 10000, "desc": desc_1},
    {"login": "keoasm@gmail.com", "password": "ffo349jf24", "price": 15000, "desc": desc_2},
    {"login": "gkretgi@gmail.com", "password": "a3fi23f23_", "price": 20000, "desc": desc_3},
]

# Создание экземпляра бота
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Главная клавиатура
main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
main_keyboard.add("Показать товары", "Информация")

# Клавиатура для отображения товаров
products_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
for i, account in enumerate(accounts_data):
    products_keyboard.add(f"{i+1}. {account['login']} ({account['price']} руб.)")
products_keyboard.add("Назад")

# Клавиатура для информации
info_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
info_keyboard.add("Назад")

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Привет! \n\nЯ могу помочь тебе купить данные для аккаунтов.", reply_markup=main_keyboard)

# Обработчик кнопки "Показать товары"
@dp.message_handler(text="Показать товары")
async def show_products(message: types.Message):
    await message.reply("**Список товаров:**", reply_markup=products_keyboard, parse_mode='MARKDOWN')

# Обработчик кнопок с номерами товаров. Используем regexp для поиска сообщения с продуктом.
@dp.message_handler(regexp=r"\d\.\s()")
async def buy_product(message: types.Message):
    try:
        product_number = int(message.text[0])
        if 1 <= product_number <= len(accounts_data):
            product = accounts_data[product_number - 1]
            await message.reply(f"**Данные для аккаунта:**\n\nЛогин: {product['login']}\nПароль: {product['password']}\nЦена: {product['price']} руб.\n\nОписание товара: \n{product['desc']} \n\n**Оплата:**\n(Вставьте инструкции по оплате)", reply_markup=info_keyboard, parse_mode='MARKDOWN')
        else:
            await message.reply("Неверный номер товара.")
    except ValueError:
        await message.reply("Неверный формат номера товара.")

# Обработчик кнопки "Назад"
@dp.message_handler(text="Назад")
async def go_back(message: types.Message):
    await message.reply("**Главное меню:**", reply_markup=main_keyboard, parse_mode='MARKDOWN')

# Обработчик кнопки "Информация"
@dp.message_handler(text="Информация")
async def show_info(message: types.Message):
    await message.reply("**Информация о боте:**\n\n Этот бот предназначен для покупки аккаунтов в PUBG. Пользователь может просматривать доступные аккаунты, их характеристики и цены, а также совершать покупку напрямую через бота. Таким образом, можно быстро и удобно получить доступ к нужному аккаунту без лишних действий.", reply_markup=info_keyboard, parse_mode='MARKDOWN')

# Запуск бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)