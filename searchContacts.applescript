on run {queryName}
	tell application "Contacts"
		try
			set p to value of phone 1 of (person 1 whose name = queryName)
		on error errMsg
			return {"False"}
		end try
	end tell
	return {p}
end run
