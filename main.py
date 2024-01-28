import timeit
from typing import Callable


from kmp import kmp_search
from bm import boyer_moore_search
from rk import rabin_karp_search

def read_file(filename): 
    with open(filename, 'r', encoding='cp1251') as f:
        return f.read()
    
def benchmark(func, text_, pattern_):
    setup_code = f"from __main__ import {func.__name__}"
    stmt = f"{func.__name__}(text, pattern)"
    return timeit.timeit(stmt=stmt, setup=setup_code, globals={'text': text_, 'pattern': pattern_}, number=10)

if __name__ == "__main__":
    text = read_file('article_1.txt')
    real_pattern = 'пошуку вимагає'
    fake_pattern = 'достобіса'
    
    results = []
    for pattern in (real_pattern, fake_pattern):
        time = benchmark(boyer_moore_search, text, pattern)
        results.append((boyer_moore_search.__name__, pattern, time))
        time = benchmark(kmp_search, text, pattern)
        results.append((kmp_search.__name__, pattern, time))
        time = benchmark(rabin_karp_search, text, pattern)
        results.append((rabin_karp_search.__name__, pattern, time))
    print(results)

    title = f"{'|Алгоритм': <30} | {'Підрядок' : <30} | {'Час виконанняб сек' : <30}"
    print(title)
    print("-" * len(title))
    for result in results:
        print(f"{result[0]: <30} | {result[1] : <30} | {result[2] : <20.5f}")
    

       #print(f"{'|Algorythm': <20} | {'Time small data' : <20} | {'Time medium  data' : <20}")
    #print(f"{'-'*20} | {'-'*20} | {'-'*20}")
    #print(f"{'|Insertion sort': <20} | {time_small_insertion : <20.5f} | {time_medium_insertion : <20.5f}")
    #print(f"{'|Merge sort': <20} | {time_small_merge : <20.5f} | {time_medium_merge : <20.5f}")
    #print(f"{'|Timsort': <20} | {time_small_timsort : <20.5f} | {time_medium_timsort : <20.5f}")