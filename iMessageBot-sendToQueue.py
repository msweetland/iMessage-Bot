import sys
from iMessageBotServer import RedisQueue

q = RedisQueue('iMessageBot')
q.put(str({"message":sys.argv[1:][0], "from": sys.argv[1:][1]}))
