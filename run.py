from slackbot.bot import Bot
from slackbot.bot import listen_to
import slackbot_settings

@listen_to('筋トレ')
def fight(message):
	message.reply('その意気じゃ！！!:muscle:')
	message.react('muscle')

@listen_to('muscle')
@listen_to('マッスル')
def muscle(message):
	message.send(':muscle::muscle:')
	message.react('muscle')

@listen_to('しない')
def anger(message):
	message.reply('筋肉してこそ人生だ:rage:')
	message.react(':volcano:')

@listen_to('ダブルバイセプス')
@listen_to('ラットスプレッド')
@listen_to('サイドチェスト')
@listen_to('サイドトライセプス')
@listen_to('アブドミナル & サイ')
@listen_to('アブドミナル&サイ')
@listen_to('モストマスキュラー')
@listen_to('オリバーポーズ')
def muscle(message):
	message.send('キレてるキレてるー！！ :muscle::muscle:')
	message.react('muscle')

if __name__ == "__main__":
	bot = Bot()
	bot.run()
