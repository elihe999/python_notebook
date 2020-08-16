from config import huey
from tasks import count_beans

if __name__ == '__main__':
    count_beans(100)
    print("Count 100")
