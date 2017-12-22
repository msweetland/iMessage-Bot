import os
import subprocess
import re

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




if __name__ == '__main__':

    print sendText('16266644912','hello')
