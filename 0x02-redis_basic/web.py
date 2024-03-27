#!/usr/bin/env python3

import requests
import redis
import time
from functools import wraps

def track_and_cache(func):
    @wraps(func)
    def wrapper(url):
        # Connect to Redis
        redis_conn = redis.Redis()

        # Track how many times the URL was accessed
        redis_conn.incr(f"count:{url}")

        # Check if the URL content is cached
        cached_content = redis_conn.get(f"cache:{url}")
        if cached_content:
            return cached_content.decode()

        # If not cached, fetch the content
        content = func(url)

        # Cache the content with an expiration time of 10 seconds
        redis_conn.setex(f"cache:{url}", 10, content)

        return content

    return wrapper

@track_and_cache
def get_page(url):
    # Simulate a slow response from the server
    # Remove this line in production code
    time.sleep(5)

    # Get the HTML content of the URL
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return f"Failed to fetch page: {response.status_code}"

if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk/delay/5000/url/http://www.example.com"
    print(get_page(url))
