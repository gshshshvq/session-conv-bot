import os
from pyrogram import Client
from dotenv import load_dotenv


load_dotenv()


if __name__ == "__main__":
    app = Client(
        ":memory:",
        api_id=os.environ.get("23843216"),
        api_hash=os.environ.get("6f5e604a5082cbe15df96042882ac8ad"),
        bot_token=os.environ.get("6222398027:AAHQwGGcTEISfthFVVmLgc4rP-gdMQWhwjg"),
        plugins=dict(root="modules"),
    )
    app.run()
