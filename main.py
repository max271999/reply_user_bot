from telethon import TelegramClient, events
import json
api_id = '20106115'
api_hash = 'dec85d8e6ed650ba2ad7278faf953925'
phone_number = '+998991373339'  # Foydalanuvchi telefon raqami


client = TelegramClient('Abdulaziz_session', api_id, api_hash)

async def main():
    await client.start(phone=phone_number)

    @client.on(events.NewMessage)
    async def handler(event):
        incoming_message = event.message.message
        sender = await event.get_sender()

        # Guruh yoki kanal ekanligini tekshirish
        if event.is_group or event.is_channel:
            return  # Guruhlar yoki kanallarga javob bermaslik

        # Agar xabar sizdan kelmasa
        if sender.id != (await client.get_me()).id:
            with open("data.json","r")as f:
                data = json.load(f)
            if incoming_message.lower() in data["auto_reply"].keys() :  # "salom" so'zini tekshirish
                await event.reply(data[incoming_message.lower()])
            if incoming_message.lower() in data["auto_del"]:
                await event.message.delete()

    await client.run_until_disconnected()

client.loop.run_until_complete(main())