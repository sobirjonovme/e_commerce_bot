
from aiogram import types

menu_button = types.ReplyKeyboardMarkup(
    keyboard=[
        [
            types.KeyboardButton(
                text="iPhone 13 Pro"
            ),
            types.KeyboardButton(
                text="Galaxy S22 Ultra"
            ),
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
