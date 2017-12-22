import os
import subprocess

# send text, bool for response
def sendText(number, message):
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
def validContact(name):
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

def imessageHandler():
    pass





if __name__ == '__main__':

    print sendText('NUMBER','hello')
