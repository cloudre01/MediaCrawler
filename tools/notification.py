import httpx


class TelegramNotifier:
    def __init__(self, bot_token, chat_id):
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.base_url = f"https://api.telegram.org/bot{bot_token}"

    async def send_message(self, message):
        async with httpx.AsyncClient() as client:
            url = f"{self.base_url}/sendMessage"
            params = {"chat_id": self.chat_id, "text": message}
            await client.post(url, params=params)
