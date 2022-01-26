from itertools import product
from collections import ChainMap
from functools import reduce
from typing import Set, List, Callable

from .tables import Record


def select(table: Set[Record], conditions: List[Callable]) -> Set[Record]:
    """
        Selects the record in the table which satisfy the conditions.
        Args:
            table: Set[Row]
            conditions: List[Callable], a list of functions. Each function takes a record
                from the table as input and returns a boolean.
        Returns:
            table_out: Set[Row] with instances satisfying the conditions.
    """
    table_out: Set = {record for record in table if all(cond(record) for cond in conditions)}
    return table_out


def project(table: Set[Record], columns: List[str]) -> Set[Record]:
    table_out: Set = {Record({column: record[column] for column in columns}) for record in table}
    return table_out
