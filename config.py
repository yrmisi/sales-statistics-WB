from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Setting(BaseSettings):
    model_config = SettingsConfigDict(env_file=Path(__file__).parent.joinpath(".env"))
    url_weekly_reports: str
    url_daily_reports: str


setting = Setting()
