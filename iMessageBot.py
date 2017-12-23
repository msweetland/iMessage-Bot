import os
import subprocess
import re
import ast
import time
from iMessageBotServer import RedisQueue

# send text, bool for response
def sendText(number=None, message=None):
    try:
        cmd = '''osascript sendMessage.applescript {} "{}"'''.format(number,message)
        result = subprocess.check_output(cmd, shell=True)

        if result[:-1] == "False":
            return False
        else:
            return (True)
    except:
        return False


# check contacts if name is present - return tuple (bool, num)
def validContact(name=None):
    try:
        cmd = '''osascript searchContacts.applescript "{}"'''.format(name)
        result = subprocess.check_output(cmd, shell=True)

        if result[:-1] == "False":
            return (False, None)
        else:
            return (True, result[:-1])
    except:
        return (False, None)

def validNumber(number):
    pass




def main():
    q = RedisQueue('iMessageBot')

    x = 0
    while (True):
        time.sleep(1)
        print x, q.size()
        x += 1
        if not q.empty():
            time.sleep(1)
            m = q.pop()
            m = ast.literal_eval(m)
            print m['message']
            number = m['from'].split('+')[1]
            sendText(number,'bot response')






if __name__ == '__main__':
    main()
    #print sendText('16266644912','hello')
