import datetime as dt
from rich.console import Console
from rich.table import Table
from application.salary import calculate_salary
from application.db.people import get_employees

console = Console(force_terminal=True)

if __name__ == "__main__":

    calculate_salary()
    get_employees()

    current_time = dt.datetime.now()
    table = Table(title="Current Date and Time", show_header=True, header_style="bold magenta")
    table.add_column("Date", justify="center", style="blue", no_wrap=True)
    table.add_column("Time", justify="center", style="blue")

    table.add_row(current_time.strftime("%Y-%m-%d"), current_time.strftime("%H:%M:%S"))

    console.print(table)
