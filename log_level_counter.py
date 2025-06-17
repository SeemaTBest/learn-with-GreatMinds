def log_level_counter(logs):
    counter = {}
    for log in logs:
        level = log.split(":")[0].strip()
        if level in counter:
            counter[level] += 1
        else:
            counter[level] = 1
    return counter

log_messages = [
    "INFO: Application started",
    "ERROR: Failed to connect to DB",
    "DEBUG: Variable x = 10",
    "INFO: User logged in",
    "WARNING: Disk space low",
    "ERROR: Null pointer exception",
    "INFO: Application stopped"
]

counts = log_level_counter(log_messages)
print("Counting:", counts)

