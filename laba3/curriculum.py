def summarise_curriculum(filename: str):
    with open(filename, "r", encoding="utf-8") as f:
        subjects = {}

        for line in f:
            name, hours = line.split(":")
            name = name.strip()

            hours_sum = 0
            for time in hours.split():
                time = time.strip()
                hour,_ = time.split("(")
                hour = int(hour)
                hours_sum += hour
            subjects[name] = hours_sum
        return subjects
