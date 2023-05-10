#!/usr/bin/env python3
""" Main file """

get_page = __import__('web').get_page
import time

url1 = "https://reqbin.com/echo/get/json?delay=10000/"
url2 = "https://httpbin.org/stream/1?delay=5"

print(get_page(url1))

print(get_page(url1))

time.sleep(10)
print(get_page(url1))

print(get_page(url2))


