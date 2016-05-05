from slackbot.bot import Bot
from slackbot.bot import listen_to
import slackbot_settings

@listen_to('筋トレ')
def fight(message):
	message.reply('その意気じゃ！！!:muscle:')
	message.react('muscle')

@listen_to('muscle')
def muscle(message):
	message.send(':muscle::muscle:')
	message.react('muscle')

if __name__ == "__main__":
	bot = Bot()
	bot.run()
