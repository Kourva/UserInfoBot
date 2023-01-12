# UserInfo bot
# GitHub: https://github.com/Kourva/UserInfoBot


# Imports
import telebot


# Import config
with open("conf.py") as data:
    exec(data.read())

    
# Define bot
bot = telebot.TeleBot(config["token"])
print("{:_^30}".format(" bot in running "))


# Class that creates a member with all needed stuff
class User:
    def __init__(self, message):
        # takes user info from message
        self.firstname = message.from_user.first_name  # first name
        self.lastname = message.from_user.last_name    # last name
        self.username = message.from_user.username     # username
        self.chatid = message.from_user.id             # chatid

    def whoami(self):
        # returns user info as string
        temp = config["whoami"].format(
            self.firstname, self.lastname, self.username, self.chatid
        )
        return temp


# Start command
@bot.message_handler(commands=["start"]) # handles only 'start' command
def start_command(message):
    # replies start message
    bot.reply_to(message, "Привет, Send any message to get your info")


# All messages
@bot.message_handler(func=lambda _: True) # handles all messages (our lambda is always True)
def all_messages(message):
    # generates a user from User class
    user = User(message)
    
    # replies user info using whoami() method
    bot.reply_to(message, user.whoami(), parse_mode="MarkdownV2") # uses 'MarkdownV2' to make chatid copiable
    
    
    
if __name__ == "__main__":
    # Run the bot in infinity mode
    bot.infinity_polling()
