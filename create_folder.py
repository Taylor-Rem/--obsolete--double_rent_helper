from datetime import datetime
import os

now = datetime.now()
day = now.day
month = now.month
year = now.year
username = "taylorremund"

path = f"/Users/{username}/Desktop/double_rent_helper/{year}/{month}/{day}"


if not os.path.exists(path):
    os.makedirs(path)


file_name = os.listdir(path)[-1]
file_path = os.path.join(path, file_name)
