from telethon import TelegramClient, events
from telethon.sessions import StringSession

api_id = 21367965             # تمہارے api_id
api_hash = "198b8590c4c2656e8bc4e2b721e71416"   # تمہارے api_hash

session_str = "1BJWap1sBu8JtF9pd_77DPEp9EiJenJCCDVhS6j9tGQA9D09Jwg3SDnevYDQUPKFY8JoyKTf9oBsOsDcrq0ablalb845UGJ2_OrFdG_ZHHeB0LGo2IB_vsPUYCaneMn_P96usaT7QwodEbbOoVZncbUYuvrkF81Ultn9WROXVh-ODvekQiqtXZazATDz4zk76sDH0oLokD94jTa-MsA3RRWAfhbbdCf5Y5Mlr_3Z9DsLN2cXdyhOUEVi9mRweqI2csXYY54olyR4c77OqFd5x16tl0XkZqi-IU6ciak0bNd2uP58PndtdwohU7kpanwKQWZ8725CWpxhopyOtst-yiZnUfmGqg3A="

source_group = -1002781143657  # جہاں سے forward کرنا ہے
target_group = -1003099447280  # کہاں forward کرنا ہے

client = TelegramClient(StringSession(session_str), api_id, api_hash)

@client.on(events.NewMessage(chats=source_group))
async def handler(event):
    await client.send_message(target_group, event.message)

client.start()
client.run_until_disconnected()
