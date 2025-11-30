from telegram import Bot
import asyncio
TELEGRAM_TOKEN = "8468238355:AAGEhFTaVbmdh-8f58t3WQ1nVsyO44NmRUQ"
CHAT_ID = "6904548577"
async def send_message_async(query):
    bot = Bot(token=TELEGRAM_TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=f"Escalation: {query}")

def escalate_to_telegram(query):
    try:
        asyncio.run(send_message_async(query))
    except Exception as e:
        print("Escalation failed:", e)


