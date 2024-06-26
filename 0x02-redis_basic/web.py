#!/usr/bin/env python3
""" this web tracker and cache """

from functools import wraps
import redis
import requests
from typing import Callable

redis_ = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """ Decorator tracking the number URL """
    @wraps(method)
    def wrapper(url):  # sourcery skip: use-named-expression
        """ Wrapper decorator times URL is visited """
        redis_.incr(f"count:{url}")
        cached_html = redis_.get(f"cached:{url}")
        if cached_html:
            return cached_html.decode('utf-8')
        html = method(url)
        redis_.setex(f"cached:{url}", 10, html)
        return html

    return wrapper


@count_requests
def get_page(url: str) -> str:
    """ returns a URL HTML content """
    req = requests.get(url)
    return req.text
