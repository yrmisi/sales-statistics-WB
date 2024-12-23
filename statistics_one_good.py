def get_statistics_one_good(
    all_goods: dict, list_goods: list[str]
) -> tuple[float, ...]:
    sales = 0
    quantity = 0
    margin = 0
    for values in all_goods.values():
        for good, sales_figures in values.items():
            if good in list_goods:
                sales += sales_figures[0]
                quantity += sales_figures[3]
                margin += sales_figures[5]

    return sales, quantity, margin
