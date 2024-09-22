import re
from typing import Tuple


def get_indexes_period(
    path_files: list[str], start_period: str | None, end_period: str | None
) -> Tuple[int, int, str, str]:
    """Функция 'get_indexes_period' получает список url файлов, начало периода и его конец,
    проходиться по списку и ищет совпадения с началом и концом периода для определения индекса нахаждения url.
    Отправляет индекс начального и конечного url, а также строковые значения начального и конечного периода
    """
    pattern_data: str = r"\b\d{2}\.\d{2}\.\d{4}"
    if start_period is None:
        start_file: int = 0
        start_period_str: str = re.search(pattern_data, path_files[0], flags=0).group()
    else:
        start_file: int = min(
            path_files.index(file) for file in path_files if start_period in file
        )
        start_period_str: str = start_period

    if end_period is None:
        end_file: int = len(path_files)
        end_period_str: str = re.findall(pattern_data, path_files[-1])[-1]
    else:
        end_file: int = (
            max(path_files.index(file) for file in path_files if end_period in file) + 1
        )
        end_period_str: str = end_period
    return start_file, end_file, start_period_str, end_period_str
