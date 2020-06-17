import threading
import web, bot

t = threading.Thread(target=web.run)
t.start()
bot.run()
