on run {targetBuddyPhone, targetMessage}
    tell application "Messages"
        set targetService to 1st service whose service type = iMessage
        set targetBuddy to buddy targetBuddyPhone of targetService
        try
    			send targetMessage to targetBuddy
          return {"True"}
    		on error errMsg
    			return {"False"}
    		end try
    end tell
end run
