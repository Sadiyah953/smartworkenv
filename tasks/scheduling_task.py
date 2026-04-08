def schedule_task(data):
    event = data.get("event", "")
    time = data.get("time", "")
    return f"Scheduled {event} at {time}"