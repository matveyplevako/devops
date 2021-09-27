from fastapi import APIRouter
import datetime
import pytz

from fastapi.responses import PlainTextResponse

api = APIRouter()


class MoscowTime:
    @staticmethod
    def get_current_time():
        tz = pytz.timezone('Europe/Moscow')
        return datetime.datetime.now(tz=tz)


def save_current_access_time():
    now = datetime.datetime.now()
    with open("shared/time.txt", "a") as file:
        file.write(str(now) + "\n")


@api.get("/", response_class=PlainTextResponse)
def get_current_moscow_time():
    current_moscow_time = MoscowTime.get_current_time()
    save_current_access_time()
    return f"Current time in Moscow: " \
           f"{current_moscow_time.strftime('%Y-%m-%d %H:%M:%S')}"


@api.get("/visits", response_class=PlainTextResponse)
def get_visits():
    with open("shared/time.txt") as file:
        return ''.join(file.readlines())
