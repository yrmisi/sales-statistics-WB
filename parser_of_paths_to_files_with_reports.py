from pathlib import Path
from typing import List, Generator


def paths_to_reports(path_to_files: str) -> List[str]:
    """Функция 'paths_to_reports' получает путь 'url' до директории, в которой парсит все файлы и
    собирает файлы с расширением '*.xlsx', после чего сортирует их по возрастанию даты и отправляет
    """
    BASE_PATH: Path = Path(path_to_files)
    files_path_obj: Generator[Path, None, None] = BASE_PATH.glob("*.xlsx")
    files_path: List[str] = [f.as_posix() for f in files_path_obj]
    files_path_sort: List[str] = sorted(files_path)
    return files_path_sort
