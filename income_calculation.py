from typing import Dict, List

from product_installation_data import cost_of_goods_delivered


def add_the_value_of_income(
    add_income: Dict[int, Dict[str, List[float | int]]]
) -> Dict[int, Dict[str, List[float | int]]]:
    for num, article_sales in add_income.items():
        for art, sales in article_sales.items():
            cost_of_goods: float = cost_of_goods_delivered[num][art]
            income_per_unit: float = (sales[1] - sales[2]) / sales[3] - cost_of_goods
            sum_cost_of_goods = cost_of_goods * sales[3]
            income: float = (sales[1] - sales[2]) - sum_cost_of_goods
            add_income[num][art].append(round(income_per_unit, 2))
            add_income[num][art].append(round(income, 2))
            add_income[num][art].append(round(sum_cost_of_goods, 2))

    return add_income
