from pypresence import Presence
import time as TIME

BTNS = [
    {
        "label": "VK",
        "url": "https://vk.com/misha_sok"
    },
    {
        "label": "GitHub",
        "url": "https://github.com/MishaSok"
    }
]

RPC = Presence("Сюда вставлять ID")
RPC.connect()
print('Starting...')

StartTime = TIME.time()
print('Connecting...')
RPC.update(
    state="Я люблю Python",
    details="Follow on my GitHub please",
    start=StartTime,
    buttons=BTNS,
    large_image="main",
    small_image='small_image',
    small_text='Большой текст',
    large_text="Маленький текст")

print('Discord status working...')

TIME.sleep(999999)
