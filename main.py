from app.trader import TraderBot

if __name__ == "__main__":
    bot = TraderBot()
    bot.run_forever(interval_seconds=30)
