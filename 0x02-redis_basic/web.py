#!/usr/bin/env python3
import requests
import redis
import time
from typing import Callable


# Redis connection
redis_client = redis.Redis()


def get_page(url: str) -> str:
    """
    Fetches the HTML content of a URL and caches
    the result with a count of accesses.
    """
    try:
        # Track the number of accesses for this URL
        count_key = f"count:{url}"
        redis_client.incr(count_key)

        # Set expiration time to 10 seconds
        redis_client.expire(count_key, 10)

        # Fetch the HTML content from the URL
        response = requests.get(url)

        # Raise an exception for bad responses (4xx or 5xx)
        response.raise_for_status()

        return response.text

    except requests.RequestException as e:
        print(f"Error fetching URL '{url}': {e}")
        return ""

    except redis.RedisError as e:
        print(f"Redis error: {e}")
        return ""

    except Exception as e:
        print(f"Unexpected error: {e}")
        return ""
