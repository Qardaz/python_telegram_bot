from loader import bot
import handlers
from config import default_commands

if __name__ == '__main__':
    bot.set_my_commands(default_commands)
    bot.infinity_polling()
