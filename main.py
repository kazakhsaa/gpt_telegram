from pyrogram import Client, filters
import openai
from config import API_ID, API_HASH, BOT_TOKEN, OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.text & ~filters.regex(r'^/'))
async def handle_message(client, message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message.text}],
        )
        await message.reply_text(response.choices[0].message['content'].strip())
    except Exception as e:
        await message.reply_text(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    app.run()
