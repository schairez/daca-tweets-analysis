
from datetime import datetime, timedelta
from typing import Generator


def get_date_ranges_list(start_date_str: str, end_date_str: str) -> Generator[str, None, None]:
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
    end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
    span = end_date - start_date
    for i in range(span.days + 1):
        next_day = start_date + timedelta(days=i)
        yield next_day.strftime('%Y-%m-%d')
