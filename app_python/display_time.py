from fastapi import APIRouter
import datetime
import pytz

from fastapi.responses import PlainTextResponse

api = APIRouter(tags=['match'])


class MoscowTime:
    @staticmethod
    def get_current_time():
        tz = pytz.timezone('Europe/Moscow')
        return datetime.datetime.now(tz=tz)


@api.get("/", response_class=PlainTextResponse)
def get_current_moscow_time():
    current_moscow_time = MoscowTime.get_current_time()
    return f"Current time in Moscow: " \
           f"{current_moscow_time.strftime('%Y-%m-%d %H:%M:%S')}"
