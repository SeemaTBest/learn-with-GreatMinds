def log_level_counter_file(filename):
    counter = {}
    
    with open(filename, 'r') as file:
        for line in file:
            if ":" in line:
                level = line.split(":")[0].strip()
                if level in counter:
                    counter[level] += 1
                else:
                    counter[level] = 1

    return counter

# Example usage
file_path = "logs.txt"
counts = log_level_counter_file(file_path)
print("Log Level Counts from file:", counts)
