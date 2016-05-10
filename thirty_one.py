#!/usr/bin/env python

from __future__ import print_function, division

def generate_possible_combinations(leftover, current_denomination_index, sorted_denominations):
    # print ("Calling for leftover = %d, current_denomination_index = %d, sorted_denominations = %s"%(leftover, current_denomination_index, sorted_denominations))
    if (current_denomination_index == len(sorted_denominations) - 1):
        if (leftover % sorted_denominations[current_denomination_index] == 0):
            yield [leftover // sorted_denominations[current_denomination_index]]
    else:
        for number_of_current_denomination in range(0, 1 + (leftover//sorted_denominations[current_denomination_index])):
            new_leftover = leftover - number_of_current_denomination * sorted_denominations[current_denomination_index]
            remaining_combinations_generator = generate_possible_combinations(new_leftover, current_denomination_index + 1, sorted_denominations)
            for remaining_combination in remaining_combinations_generator:
                possible_combination = [number_of_current_denomination]
                possible_combination.extend(remaining_combination)
                yield possible_combination

if __name__=="__main__":
    denominations = [1, 2, 5, 10, 20, 50, 100, 200]
    denominations.sort()
    denominations.reverse()
    required_sum = 200
    possible_combinations = generate_possible_combinations(required_sum, 0, denominations)
    # for possible_combination in possible_combinations:
    #     print ("One possible combination is %s"%(possible_combination))
    list_of_possible_combinations = list(possible_combinations)
    required_number = len(list_of_possible_combinations)
    print ("Required number is %d"%(required_number))
