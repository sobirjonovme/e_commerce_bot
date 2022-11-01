from aiogram import types
from aiogram.types import LabeledPrice

from utils.misc.product import Product


iphone_13 = Product(
    title="iPhone 13 Pro",
    description="Telefonni xarid qilish uchun quyidagi tugmani bosing.",
    currency="UZS",
    prices=[
        LabeledPrice(
            label='phone',
            amount=9_700_000_00,  # 9 700 000.00 UZS
        ),
        LabeledPrice(
            label='Chegirma',
            amount=-300_000_00,  # -300 000.00 UZS
        ),
    ],
    start_parameter="create_invoice_iphone",
    photo_url='https://smartmania.cz/wp-content/uploads/2020/11/Apple_iPhone_12_Pro_001.jpg',
    photo_width=1280,
    photo_height=564,
    # photo_size=600,
    # need_email=True,
    need_name=True,
    need_phone_number=True,
    need_shipping_address=True,  # foydalanuvchi manzilini kiritishi shart
    is_flexible=True,
)

galaxy_s22 = Product(
    title="Samsung Galaxy S 22 Ultra",
    description="Telefonni xarid qilish uchun quyidagi tugmani bosing.",
    currency="UZS",
    prices=[
        LabeledPrice(
            label='s22_ultra',
            amount=10_300_000_00,  # 10 300 000.00 UZS
        ),
        LabeledPrice(
            label='Chegirma',
            amount=-300_000_00,  # -300 000.00 UZS
        ),
    ],
    start_parameter="create_invoice_s22_ultra",
    photo_url='https://www.zbozi.cz/magazin/wp-content/uploads/2022/02/galaxy-s22-ultra-nahled.jpg',
    photo_width=1280,
    photo_height=564,
    # photo_size=800,
    need_name=True,
    need_phone_number=True,
    need_shipping_address=True,  # foydalanuvchi manzilini kiritishi shart
    is_flexible=True,
)

REGULAR_SHIPPING = types.ShippingOption(
    id='post_reg',
    title="Fargo (3 kun)",
    prices=[
        LabeledPrice(
            'Maxsus quti', 5_000_00),
        LabeledPrice(
            '3 ish kunida yetkazish', 30_000_00),
    ]
)
FAST_SHIPPING = types.ShippingOption(
    id='post_fast',
    title='Express pochta (1 kun)',
    prices=[
        LabeledPrice(
            '1 kunda yetkazish', 40_000_00),
    ]
)

PICKUP_SHIPPING = types.ShippingOption(
    id='pickup',
    title="Do'kondan olib ketish",
    prices=[
        LabeledPrice("Yetkazib berishsiz", 0)
    ]
)