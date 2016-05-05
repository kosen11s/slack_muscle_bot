from slacker import Slacker
import sys, os, time, json, datetime, requests
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')
import slackbot_settings

def getJson(url, parameters):
	r = requests.get(url, params = parameters)
	data = json.loads(r.text)

	return data

def muscleCounter(json):
	counter = 0
	for i in range(len(json)):
		if json[i]['name'] == 'muscle':
			counter = json[i]['count']
	return counter

def muscle(now):
	yesterday = now + datetime.timedelta(days = -1)
	muscleCount = 0

	url = 'https://slack.com/api/channels.list'
	parameters = {'token' : slackbot_settings.API_TOKEN}
	json = getJson(url, parameters)

	for i in range(len(json['channels'])):
		channelId = json['channels'][i]['id']
		parameters['channel'] = channelId
		url = 'https://slack.com/api/channels.history'
		json_2 = getJson(url, parameters)

		for j in range(len(json_2['messages'])):
			messagePostTime = datetime.datetime.fromtimestamp(float(json_2['messages'][j]['ts']))
			# Time comparison
			if messagePostTime >= yesterday:
				# Muscle Counter
				if 'reactions' in json_2['messages'][j]:
					muscleCount += muscleCounter(json_2['messages'][j]['reactions'])
			else:
				break
	
	return muscleCount

def postMessage(count):
	slack = Slacker(slackbot_settings.API_TOKEN)
	slack.chat.post_message(
		'muscle',
		'寝る前に今日も' + str(count) + '回腹筋してマッスルじゃ:muscle:',
		as_user=True)

if __name__ == '__main__':
	while(True):
		now = datetime.datetime.now().strftime('%H:%M:%S')
		if now == '22:00:00':
			muscleCount = muscle(datetime.datetime.now())
			time.sleep(1)
			postMessage(muscleCount)
