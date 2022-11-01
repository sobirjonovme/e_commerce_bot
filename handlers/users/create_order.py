from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery, Message
from data.config import ADMINS

from loader import dp, bot
from data.product import iphone_13, galaxy_s22,  FAST_SHIPPING, REGULAR_SHIPPING, PICKUP_SHIPPING
from keyboards.inline.product_keys import build_keyboard
from keyboards.default.main_menu import menu_button


@dp.message_handler(text="iPhone 13 Pro")
async def show_invoices(message: types.Message):
    caption = "<b>iPhone 13 Pro</b> telefoni.\n\n"
    caption += "Narxi: <b>9 700 000 so'm</b>"
    await message.answer_photo(
        photo="https://smartmania.cz/wp-content/uploads/2020/11/Apple_iPhone_12_Pro_001.jpg",
        caption=caption, reply_markup=build_keyboard("iphone_13")
    )


@dp.message_handler(text="Galaxy S22 Ultra")
async def show_invoices(message: types.Message):
    caption = "<b>Galaxy S22 Ultra</b> telefoni.\n\n"
    caption += "Narxi: <b>10 300 000 so'm</b>"

    await message.answer_photo(
        photo="https://www.zbozi.cz/magazin/wp-content/uploads/2022/02/galaxy-s22-ultra-nahled.jpg",
        caption=caption, reply_markup=build_keyboard("galaxy_s22")
    )


@dp.message_handler(Command("mahsulotlar"))
async def mahsulotlar_royxati(message: Message):
    await message.answer(
        text="Mahsulotlar ro'yxati",
        reply_markup=menu_button
    )


@dp.callback_query_handler(text="product:iphone_13")
async def book_invoice(call: CallbackQuery):
    await bot.send_invoice(chat_id=call.from_user.id,
                           **iphone_13.generate_invoice(),
                           payload="payload:iphone_13")
    await call.answer()


@dp.callback_query_handler(text="product:galaxy_s22")
async def praktikum_invoice(call: CallbackQuery):
    await bot.send_invoice(chat_id=call.from_user.id,
                           **galaxy_s22.generate_invoice(),
                           payload="payload:galaxy_s22")
    await call.answer()


@dp.shipping_query_handler()
async def choose_shipping(query: types.ShippingQuery):
    if query.shipping_address.country_code != "UZ":
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        ok=False,
                                        error_message="Chet elga yetkazib bera olmaymiz")
    elif query.shipping_address.city.lower() == "tashkent":
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        shipping_options=[FAST_SHIPPING, REGULAR_SHIPPING, PICKUP_SHIPPING],
                                        ok=True)
    else:
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        shipping_options=[REGULAR_SHIPPING],
                                        ok=True)


@dp.pre_checkout_query_handler()
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query_id=pre_checkout_query.id,
                                        ok=True)
    await bot.send_message(chat_id=pre_checkout_query.from_user.id,
                           text="Xaridingiz uchun rahmat!")
    await bot.send_message(
        chat_id=ADMINS[0],
        text=f"Quyidagi mahsulot sotildi: {pre_checkout_query.invoice_payload}\n"
             f"ID: {pre_checkout_query.id}\n"
             f"Telegram user: {pre_checkout_query.from_user.first_name}\n"                                
             f"Xaridor: {pre_checkout_query.order_info.name}, "
             f"tel: {pre_checkout_query.order_info.phone_number}"
        )