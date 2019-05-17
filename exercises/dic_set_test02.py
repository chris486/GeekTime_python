import time
id = [x for x in range(0, 100000)]
price = [x for x in range(200000, 300000)]
products = list(zip(id, price))

start_using_list = time.perf_counter()
find_unique_price_using_list(products)
end_using_list = time.perf_counter()
print("time elapse using list: {}".format(end_using_list - start_using_list))

start_using_set = time.perf_counter()
find_unique_price_using_set(products)
end_using_set = time.perf_counter()
print("time elapse using set: {}".format(end_using_set - start_using_set))


import timeit
print(timeit.timeit("{'name':'jason','age':99,'gemder':'male'}",number=10000))
print(timeit.timeit("dict({'name':'jason','age':99,'gemder':'male'})",number=10000))