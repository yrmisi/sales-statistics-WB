import os

from dotenv import find_dotenv, load_dotenv
from pydantic import StrictStr
from pydantic_settings import BaseSettings

if not find_dotenv():
    exit("Переменное окружение не загружено, т.к. отсутствует файл .env")
else:
    load_dotenv()


class ReportsPathSetting(BaseSettings):
    path_file_weekly_reports: StrictStr = os.getenv("URL_WEEKLY_REPORTS")
    path_file_daily_reports: StrictStr = os.getenv("URL_DAILY_REPORTS")
