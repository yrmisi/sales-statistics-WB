NAME_AND_NUMBER_OF_COLUMNS: dict[str, int] = {
    "Номер поставки": 0,
    "Артикул поставщика": 0,
    "Обоснование для оплаты": 0,
    "Вайлдберриз реализовал Товар (Пр)": 0,
    "К перечислению Продавцу за реализованный Товар": 0,
    "Услуги по доставке товара покупателю": 0,
    "Кол-во": 0,
    "Общая сумма штрафов": 0,
    "Хранение": 0,
    "Платная приемка": 0,
}


def get_number_column(column_names: tuple) -> dict[str, int]:
    """Функция 'get_number_column' получает на вход кортеж из названий столбцов таблицы и
    отправляет словарь 'NAME_AND_NUMBER_OF_COLUMNS' c указанием названием столбцов и их номерами
    """
    for idx, cell in enumerate(column_names, start=1):
        if NAME_AND_NUMBER_OF_COLUMNS.get(cell.value) is not None:
            NAME_AND_NUMBER_OF_COLUMNS[cell.value] = idx
    return NAME_AND_NUMBER_OF_COLUMNS
