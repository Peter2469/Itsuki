
async def duration(time):
    if time.endswith("s"):
        return time.replace("s", "")
    
    if time.endswith("m"):
        newtime = int(time).replace("m", "") * 60
        return int(newtime)

    if time.endswith("h"):
        newtime = int(time).replace("h", "") * 3600
        return int(newtime)
    
    if time.endswith("d"):
        newtime = int(time).replace("d", "") * 86400
        return int(newtime)
    else:
        return Exception