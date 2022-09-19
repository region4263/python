from logic import get_list_elements, doing_simple, mass_operation, get_list_kmplx, mass_operation_kmplx
from aiogram import Bot, Dispatcher, types, executor


bot = Bot(token="YOUR_TOKEN")
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    Этот handler будет вызыван когда пользователь отправит
    команду `/start` или `/help`
    """
    await message.reply(
        f"Привет!\nЯ калькулятор!\nЗдесь ты можешь работать с рациональными и комплексными числами\n"
        f"Рациональные числа: через команду 'rational' вводим данные\n"
        f"ПРИМЕР:    /rational 6/10+1.5\n"
        f"Комплексные числа: через команду 'complex' вводим данные\n"
        f"ПРИМЕР:    /complex (-6+7i)+(4-3i)\n")


@dp.message_handler(commands=['rational'])
async def main(message: types.Message):
    expression: str = message.text
    arr = get_list_elements(expression)
    arr = doing_simple(arr)
    result = mass_operation(arr)
    await message.answer(f'Результат выражения\n{expression}={result}')


@dp.message_handler(commands=['complex'])
async def main(message: types.Message):
    expression: str = message.text
    arr = get_list_kmplx(expression)
    result = mass_operation_kmplx(arr)
    await message.answer(f'Результат выражения\n{expression}={result}')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
