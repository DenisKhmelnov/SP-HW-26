import re
from typing import List, Iterable, Set


def filter_query(param: str, data: Iterable) -> Iterable:
    return filter(lambda x: param in x, data)

def map_query(param: str, data: Iterable) -> Iterable:
    col_number = int(param)
    return map(lambda x: x.split(' ')[col_number], data)

def unique_query(data: Iterable, *args, **kwargs) -> Set:
    return set(data)

def sort_query(param: str, data: Iterable) -> List:
    return sorted(data, reverse=param == 'desc')

def limit_query(param: str, data: Iterable) -> List:
    limit = int(param)
    return list(data[:limit])

def filter_regex(param: str, data: Iterable) -> List:
    output = []
    for string in data:
        query_match = re.findall(param, string)
        if query_match:
            output.extend(query_match)
    return output
