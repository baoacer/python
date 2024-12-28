from datetime import datetime

second = 51100

house = second // 3600
minute = (second % 3600) // 60
second = (second % 3600) % 60

print(f"{house}:{minute}:{second}") 