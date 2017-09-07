from math import sqrt
from math import factorial
from time import time
from pprint import pprint
from itertools import combinations


def euc_dist(city1, city2):
    return sqrt(pow(city1[0] - city2[0], 2) + pow(city1[1] - city2[1], 2))


def n_choose_k(n, k):
    if n < k:
        return 0
    else:
        return factorial(n) / factorial(k) / factorial(n - k)


def n_choose_k_table(num_of_cities):
    """Computes a dictionary which caches all possible n choose k computations."""
    table = {}
    for n in range(num_of_cities):
        for k in range(1, n + 2):
            table[(n, k)] = n_choose_k(n, k)
    return table


def comb_index(comb_start, comb, nck_table):
    
    return sum([nck_table[(y - comb_start, x + 1)]
                for x, y in enumerate(comb)])


def tsp(num_of_cities, dist_dict):
    nck_table = n_choose_k_table(num_of_cities)
    last_min = [[0 for i in range(num_of_cities + 1)]
                for j in range(2, num_of_cities + 1)]
    for city in range(2, num_of_cities + 1):
        last_min[comb_index(2, (city,), nck_table)][city] = dist_dict[(1, city)]
    for m in range(3, num_of_cities + 1):
        current_min = [[0 for i in range(num_of_cities + 1)]
                       for j in range(nck_table[(num_of_cities - 1, m - 1)])]
        for s_except_1 in combinations(range(2, num_of_cities + 1), m - 1):
            s_index = comb_index(2, s_except_1, nck_table)
            for j in s_except_1:
                s_except_1_j = list(s_except_1)[:]
                s_except_1_j.remove(j)
                s_except_1_j_index = comb_index(2, s_except_1_j, nck_table)
                current_min[s_index][j] = min(
                    [last_min[s_except_1_j_index][k] + dist_dict[(k, j)]
                     for k in s_except_1_j])
        del last_min
        last_min = current_min[:]
        del current_min
    out = min([dist_dict[(city + 2, 1)] + dist
               for city, dist in enumerate(last_min[0][2:])])
    return out, last_min


def main():
    city_num = 1
    cities = {}
    dist_dict = {}
    #with open('test.txt') as file_in:
    with open('r.txt') as file_in:
        next(file_in)
        for line in file_in:
            cities[city_num] = [float(x) for x in line.strip().split(' ')]
            city_num += 1
    for x, y in combinations(range(1, city_num), 2):
        print(x,y)
        dist_dict[(x, y)] = euc_dist(cities[x], cities[y])
        dist_dict[(y, x)] = dist_dict[(x, y)]
    pprint(dist_dict)
    return tsp(city_num - 1, dist_dict)


if __name__ == '__main__':
    start = time()
    print(main())
    print(time() - start)
