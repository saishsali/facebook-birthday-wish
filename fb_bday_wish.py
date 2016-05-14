import facebook
from datetime import datetime

access_token = 'users-access-token'

graph = facebook.GraphAPI(access_token, version = '2.5')

args = {'fields' : 'birthday, name', 'limit': 1000}
friends = graph.get_connections('me', 'friends', **args)

current_date = datetime.now()

for friend in friends['data']:
    if 'birthday' in friend:
        birthdate = datetime.strptime(friend['birthday'], '%m/%d/%Y')
        if birthdate.date == datetime.now() and birthdate.month == datetime.now():
            print 'Wishing' + friend['name']
            graph.put_object(parent_object = friend['id'], connection_name = 'feed', message = 'Happy birthday! Have fun :)')
            
