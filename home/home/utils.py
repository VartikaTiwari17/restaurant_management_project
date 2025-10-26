# Utility functions for the home app

def estimate_table_turnover_time(table_capacity: int) -> int:
    """
    Estimate the dining duration for a table based on its seating capacity.

    Args:
        table_capacity (int): Number of seats at the table.

    Returns:
        int: Estimated dining duration in minutes.
    """
    if table_capacity <= 2:
        return 60  # small table
    elif table_capacity <= 4:
        return 90  # medium table
    else:
        return 120  # large table
