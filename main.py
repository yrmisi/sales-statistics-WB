import os
from typing import List

from dotenv import load_dotenv, find_dotenv

from custom_decorators import measure_time
from indexes_start_and_end_period import get_indexes_period
from parsing_xlsx_file_with_sales_statistics import collect_sales_statistics
from parser_of_paths_to_files_with_reports import paths_to_reports


@measure_time
def main() -> None:
    sum_sales = 0
    sum_incomes = 0
    total_sum_cost_price = 0
    total_sum_sales = 0
    total_sum_sales_after_deduction = 0
    total_sum_payable = 0
    if not find_dotenv():
        exit("Переменное окружение не загружено, т.к. отсутствует файл .env")
    else:
        load_dotenv()
    # url_file: str = os.getenv("URL_WEEKLY_REPORTS")
    url_file: str = os.getenv("URL_DAILY_REPORTS")

    start_period: str | None = None
    end_period: str | None = None
    paths_to_files: List[str] = paths_to_reports(url_file)
    start_idx, end_idx, start_period_str, end_period_str = get_indexes_period(
        paths_to_files, start_period, end_period
    )
    for f in paths_to_files[start_idx:end_idx]:
        (
            sale,
            income,
            cost_price,
            total_sale,
            total_sales_after_deduction,
            total_payable,
        ) = collect_sales_statistics(f)
        sum_sales += sale
        sum_incomes += income
        total_sum_cost_price += cost_price
        total_sum_sales += total_sale
        total_sum_sales_after_deduction += total_sales_after_deduction
        total_sum_payable += total_payable

    profitability: float = round(sum_incomes * 100 / sum_sales, 2)
    sum_sales: float = round(sum_sales, 2)
    sum_incomes: float = round(sum_incomes, 2)
    total_sum_cost_price: float = round(total_sum_cost_price, 2)
    percentage_of_expenses: float = round(total_sum_payable * 100 / total_sum_sales, 2)
    total_sum_sales: float = round(total_sum_sales, 2)
    total_sum_sales_after_deduction: float = round(total_sum_sales_after_deduction, 2)
    total_sum_payable: float = round(total_sum_payable, 2)
    total_net_profit: float = round(total_sum_payable - total_sum_cost_price, 2)
    percentage_of_net_profit_in_sales = round(
        total_net_profit * 100 / total_sum_sales, 2
    )
    tax: float = round(total_sum_sales * 0.06, 2)

    print(
        f"Total for the period from {start_period_str} by {end_period_str}: \n"
        f"{sum_sales=}, {sum_incomes=}, {profitability=}% \n"
        f"{total_sum_sales=}, {total_sum_sales_after_deduction=}, \n"
        f"{total_sum_payable=}, {percentage_of_expenses=}% \n"
        f"{total_sum_cost_price=}, {total_net_profit=}, {percentage_of_net_profit_in_sales=}% \n"
        f"{tax=}"
    )


if __name__ == "__main__":
    main()
