'''
Name: Corin Chepko
Date: 11/01/23
Program Description: https://open.kattis.com/problems/everywhere
Algorithm:
    input number of test cases
    for each test case:
        input number of cities
        for each city:
            if city is key in map, add 1 to value
            if city not key, add with a value of 1
'''

import sys

def test():
    cities = ["Denver","GrandJunction","Olathe", "Denver", "Denver"]
    assert process_test_case(cities) == 3
    print("All test passes!",file=sys.stderr)

def process_test_case(cities):
    #print(cities)
    places = {}
    for city in cities:
        if city in places:
            places[city] += 1
        else: #add to map with value 1
            places[city] = 1
    return len(places)

def main():
    test()

    test_cases = int(input())
    for j in range(test_cases):
        num_cities = int(input())
        cities = []
        for i in range(num_cities):
            city = input()
            cities.append(city)
        unique_cities = process_test_case(cities)

        print(unique_cities)

# if I'm the main program, run my main function,
#  otherwise just my functions are available
if(__name__ == '__main__'):
    main()