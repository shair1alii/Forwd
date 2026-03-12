from telethon import TelegramClient, events
from telethon.sessions import StringSession

api_id = 21367965             # تمہارے api_id
api_hash = "198b8590c4c2656e8bc4e2b721e71416"   # تمہارے api_hash

session_str = "1BJWap1sBuwNGiy9EYUCKi-XtpadrG5rEd0Ti8yUwMVS-_foR2Tki9wCvJzH9XRxZ3NYuE59tli5THrLQ78coscp6PNSmKRW2WAgSBrIstZSSvSnNU4dAHRTif3FwT7CUTCgZaTbBUujoUSKivwlC-Xv56Yd8q8KsEeGwu6GWqcbLuKhvuQrvR7qwI7hvY4Te0l-jblYEiTYUiQYy4lbwsnhvZI2Brf-OQVnttLjiJyPEDaAsT4kFWPint5Mf5PFtSTQGJyeQY0dLpBuemIwpXDHIFIncqr1dHwtreX6I1IJjbIHpN9V89hXixA6Q8cMtmr9cyvHyOHrXePBKdgVD_qAD2NT1yBI="

source_group = -1002781143657  # جہاں سے forward کرنا ہے
target_group = -1003099447280  # کہاں forward کرنا ہے

client = TelegramClient(StringSession(session_str), api_id, api_hash)

@client.on(events.NewMessage(chats=source_group))
async def handler(event):
    await client.send_message(target_group, event.message)

client.start()
client.run_until_disconnected()
