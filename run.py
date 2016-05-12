from slackbot.bot import Bot
from slackbot.bot import listen_to
import slackbot_settings, json, requests
import random as rd

@listen_to('筋肉ルーレット')
def roulette(message):
	try:
		muscleRoulette = ['腕立て伏せ', '腹筋', 'スクワット', 'フロントプランク', 'ヒップリフト']
		message.reply(rd.randint(0, len(muscleRoulette) - 1))
		message.react('muscle')
	except Exception as e:
		print(type(e))

@listen_to('muscle')
@listen_to('マッスル')
def muscle(message):
	try:
		message.send(':muscle::muscle:')
		message.react('muscle')
	except Exception as e:
		print(type(e))

@listen_to('しない')
@listen_to('ダメだ')
@listen_to('だめだ')
@listen_to('つかれた')
@listen_to('疲れた')
def anger(message):
	try:
		message.reply('筋肉あってこそ人生だ:rage:')
		message.react('volcano')
	except Exception as e:
		print(type(e))

@listen_to('ダブルバイセプス')
@listen_to('ラットスプレッド')
@listen_to('サイドチェスト')
@listen_to('サイドトライセプス')
@listen_to('アブドミナル & サイ')
@listen_to('アブドミナル&サイ')
@listen_to('モストマスキュラー')
@listen_to('オリバーポーズ')
def muscle(message):
	try:
		message.send('キレてるキレてるー！！ :muscle::muscle:')
		message.react('muscle')
	except Exception as e:
		print(type(e))

if __name__ == "__main__":
	bot = Bot()
	bot.run()
