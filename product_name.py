from product_installation_data import product_name_by_article


def replacing_article_with_the_product_name(
    article_change_to_product: dict[int, dict[str, list[float | int]]]
) -> dict[int, dict[str, list[float | int]]]:
    """Функция 'replacing_article_with_the_product_name' получает словарь,
    в котором заменяет артикул товара на его наименование"""
    sales_statistics_copy = article_change_to_product.copy()

    for num, article_sales in sales_statistics_copy.items():
        article_sales_copy = article_sales.copy()

        for art in article_sales_copy:
            product_name: str = product_name_by_article[art]
            article_change_to_product[num][product_name] = article_sales.pop(art)

    return article_change_to_product
