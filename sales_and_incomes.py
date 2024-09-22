from typing import Tuple, Dict, List


def calculate_sales_turnover_and_income(
    sales_statistics: Dict[int, Dict[str, List[float | int]]]
) -> Tuple[float, float, float]:
    """Функция 'calculate_sales_turnover_and_income' на вход получает словарь с номером поставки,
    наименованием товара и его финансовыми показателями и выводит сумму продаж, доходность за день и себестоимость товара
    """
    sales: float = 0
    incomes: float = 0
    cost_price: float = 0

    for val in sales_statistics.values():
        for v in val.values():
            sales += v[0]
            incomes += v[5]
            cost_price += v[6]

    sales: float = round(sales, 2)
    incomes: float = round(incomes, 2)
    cost_price: float = round(cost_price, 2)
    return sales, incomes, cost_price
