#!/usr/bin/env python3
import requests
import redis
import time
from typing import Callable

# Redis connection
redis_client = redis.Redis()

def get_page(url: str) -> str:
    """
    Fetches the HTML content of a URL and caches the result with a count of accesses.
    """
    # Track the number of accesses for this URL
    count_key = f"count:{url}"
    redis_client.incr(count_key)
    redis_client.expire(count_key, 10)  # Set expiration time to 10 seconds
    
    # Fetch the HTML content from the URL
    response = requests.get(url)
    return response.text

# Example usage
if __name__ == "__main__":
    # Example URL to test
    url = "http://slowwly.robertomurray.co.uk/delay/1000/url/http://www.example.com"
    
    # Fetch the page content and print
    html_content = get_page(url)
    print(html_content)

