#!/usr/bin/env python

import math
import numpy
import itertools

def get_list_of_indices(element,array):
    match_list=[]
    for index in range(len(array)):
        if(array[index]==element):
            match_list.append(index)
    return match_list

def possible_combinations_generator(below_this_row_index,deviation):
    if (deviation==0):
        yield [0]*(number_of_rows-below_this_row_index)
    else:
        if(below_this_row_index < number_of_rows-1):
            deviation_allowable=min([deviation,len(index_list[below_this_row_index])-1])
            for deviation_taken_up_by_this_row in range(0,1+deviation_allowable):
                below_combinations_generator=possible_combinations_generator(below_this_row_index+1,deviation-deviation_taken_up_by_this_row)
                for below_combinations in below_combinations_generator:
                    list_of_combinations=[deviation_taken_up_by_this_row]
                    list_of_combinations.extend(below_combinations)
                    yield list_of_combinations
        else:
            if(deviation < len(index_list[below_this_row_index])):
                yield [deviation]

def paths_generator(deviation):
    possible_combinations=possible_combinations_generator(0,deviation)
    for possible_combination in possible_combinations:
        raw_paths=[]
        for row_index in range(0,number_of_rows):
            raw_paths.append(index_list[row_index][possible_combination[row_index]])
        unpacked_paths=itertools.product(*raw_paths)
        for path in unpacked_paths:
            yield list(path)
    # raw_paths,raw_paths_copy=itertools.tee()
    # # print "raw_paths:"
    # # for path in raw_paths_copy:
    # #     print path
    # for path in raw_paths:
    #     unpacked_paths=itertools.product(*path)
    #     for unpacked_path in unpacked_paths:
    #         # print "unpacked_path:"
    #         # print list(unpacked_path)
    #         yield list(unpacked_path)

def path_exists(path):
    exists=True
    for row_index in range(0,number_of_rows-1):
        if(not(path[row_index]==path[row_index+1] or path[row_index]+1==path[row_index+1])):
            exists=False
            break
    return exists

def pathsum(path):
    totalsum=0
    for row_index in range(0,number_of_rows):
        totalsum=totalsum+triangle[row_index][path[row_index]]
    return totalsum

def initialize(filename):
    global number_of_rows,triangle,sorted_triangle,index_list
    triangle_file=open(filename,'r')
    triangle=[]
    number_of_rows=0
    for array in triangle_file:
        triangle.append([int(number) for number in array.split(' ')])
        number_of_rows=number_of_rows+1

    sorted_triangle=[]
    for row in triangle:
        sorted_triangle.append(sorted(row,reverse=True))

    index_list=[]
    for row_index in range(0,number_of_rows):
        row=triangle[row_index]
        sorted_row=sorted_triangle[row_index]
        index_list_row=[get_list_of_indices(sorted_row[0],row)]
        last_element_for_which_index_created=sorted_row[0]
        for element in sorted_row[1:]:
            if (element==last_element_for_which_index_created):
                continue
            else:
                index_list_row.append(get_list_of_indices(element,row))
                last_element_for_which_index_created=element
        index_list.append(index_list_row)

if __name__ == "__main__":
    initialize('eighteen.dat')
    print "triangle:"
    print triangle
    print "sorted_triangle:"
    print sorted_triangle
    print "index_list:"
    print index_list

    deviation=0
    deviation_remaining=0
    path_found=False
    deviation_for_which_path_found=0
    list_of_path_to_sum=[]
    while (not(path_found)):
        print "Checking deviation = ",deviation
        list_of_paths=paths_generator(deviation)
        for path in list_of_paths:
            # print "Checking path:"
            # print path
            if(path_exists(path)):
                path_found=True
                print "Path found:"
                print path
                deviation_for_which_path_found=deviation
                print "deviation for which path found:"
                print deviation
                list_of_paths_to_sum.append(path)
                # break
        if (not(path_found)):
            deviation=deviation+1
        if (deviation > (number_of_rows*(number_of_rows+1))/2):
            print "something has gone wrong"
            break

    maxsum=0
    for path in list_of_paths_to_sum:
        # print "path is: ", path
        sum_of_path = pathsum(path)
        print "sum of path is: ", sum_of_path
        if (sum_of_path > maxsum):
            maxsum=sum_of_path
    print "maximum sum is: ", maxsum


# def index_list_from_this_row_generator(row_index):
#     global deviation_remaining
#     for deviation_taken_up_by_this_row in range (0,min([deviation_remaining+1,len(index_list[row_index])])):
#         deviation_remaining = deviation_remaining-deviation_taken_up_by_this_row
#         index_list_array_from_this_row=index_list[row_index][deviation_taken_up_by_this_row]
#         yield index_list_array_from_this_row

# def possible_indices_generator(deviation,path_so_far,row_index):
#     deviation_remaining=deviation
#     print "deviation: ", deviation
#     print "path_so_far: ", path_so_far
#     print "row index: ", row_index
#     if (row_index>=number_of_rows):
#         if (deviation==0):
#             yield path_so_far
#         else:
#             return
#     else:
#         for deviation_taken_up_by_this_row in range (0,min([deviation+1,len(index_list[row_index])])):
#             deviation_remaining = deviation-deviation_taken_up_by_this_row
#             path_so_far.append(index_list[row_index][deviation_taken_up_by_this_row])
#             for total_path in possible_indices_generator(deviation_remaining,path_so_far,row_index+1):
#                 yield total_path

# def raw_paths_generator(deviation):
#     # global deviation_remaining
#     # deviation_remaining=deviation
#     raw_paths=possible_indices_generator(deviation,[],0)
#     for raw_path in raw_paths:
#     for row_index in range(0,number_of_rows):
#         print "row_index = ", row_index
#         print "index_list: ", index_list[row_index]
#         print "len(index_list): ", len(index_list[row_index])
#         print "min: ", min([deviation_remaining,len(index_list[row_index])])
#         print "range: ", range (0,1+min([deviation_remaining,len(index_list[row_index])]))
#         for deviation_taken_up_by_this_row in range (0,min([deviation_remaining+1,len(index_list[row_index])])):
#             print "deviation taken up by this row = ",deviation_taken_up_by_this_row
#             deviation_remaining = deviation_remaining-deviation_taken_up_by_this_row
#             print "deviation remaining = ",deviation_remaining
#             index_list_array_from_this_row=index_list[row_index][deviation_taken_up_by_this_row]
#             print "index_list_array_from_this_row:"
#             print index_list_array_from_this_row
#             for counter_index_list_array_from_this_row in range(0,len(index_list_array_from_this_row)):
#                 raw_paths.append(index_list_array_from_this_row)
        

#     print "for deviation=",deviation,", raw_paths:"
#     print raw_paths
#     return raw_paths

# def paths_unpacker(path):
#     paths=itertools.product(*path)
#     for path in paths:
#         yield path



# def possible_indices_generator(deviation,row_index):
#     if (row_index==number_of_rows-1):
#         if(deviation>=len(index_list[row_index])):
#             return
#         else:
#             yield index_list[row_index][deviation]
#     else:
#         for deviation_taken_up_by_this_row in range (0,min([deviation+1,len(index_list[row_index])])):
#             deviation_remaining = deviation-deviation_taken_up_by_this_row
#             rest_of_possible_indices_generated=possible_indices_generator(deviation_remaining,row_index+1)
#             for rest_of_possible_indices in rest_of_possible_indices_generated_backup:
#             for rest_of_possible_indices in rest_of_possible_indices_generated:
#                 yield [index_list[row_index][deviation_taken_up_by_this_row]].append(rest_of_possible_indices)


# def paths_generator(deviation):
#     raw_paths=possible_indices_generator(deviation,0)
#     for path in raw_paths:
#         unpacked_paths=itertools.product(*path)
#         for unpacked_path in unpacked_paths:
#             yield list(unpacked_path)

# def possible_indices_generator(deviation,row_index):
#     print "deviation: ", deviation, ", row_index: ", row_index
#     if (row_index==number_of_rows-1):
#         if(deviation>=len(index_list[row_index])):
#             print "ran out of indices in last row"
#             return
#         else:
#             # print "final yield:"
#             # print index_list[row_index][deviation]
#             yield index_list[row_index][deviation]
#     else:
#         # print "range: ", range (0,min([deviation+1,len(index_list[row_index])]))
#         for deviation_taken_up_by_this_row in range (0,min([deviation+1,len(index_list[row_index])])):
#             deviation_remaining = deviation-deviation_taken_up_by_this_row
#             # print "deviation_taken_up_by_this_row: ", deviation_taken_up_by_this_row
#             # print "deviation_remaining: ", deviation_remaining
#             # print "pre-append: ", [index_list[row_index][deviation_taken_up_by_this_row]]
#             rest_of_possible_indices_generated,rest_of_possible_indices_generated_backup=itertools.tee(possible_indices_generator(deviation_remaining,row_index+1))
#             # for rest_of_possible_indices in rest_of_possible_indices_generated_backup:
#                 # print "rest of possible indices:"
#                 # print rest_of_possible_indices
#             for rest_of_possible_indices in rest_of_possible_indices_generated:
#                 # print "to yield:"
#                 # print [index_list[row_index][deviation_taken_up_by_this_row]].append(rest_of_possible_indices)
#                 print "preappend: ", [index_list[row_index][deviation_taken_up_by_this_row]], ", to append: ", rest_of_possible_indices, ", row_index: ", row_index
#                 print "soon to be latest: ", [index_list[row_index][deviation_taken_up_by_this_row]].append(rest_of_possible_indices)
#                 yield [index_list[row_index][deviation_taken_up_by_this_row]].append(rest_of_possible_indices)

# Format of return list: (config, row index of chosen element, starting row of chosen element, boolean:end configuration reached?)
# def next_config(list_return_format):
#     config=list_return_format[0]
#     row_index_of_chosen_element=list_return_format[1]
#     starting_row=list_return_format[2]
#     global end_configuration_reached
#     if (row_index_of_chosen_element < number_of_rows-1):
#         available_positions_in_next_row=0
#         index_of_next_available_row=row_index_of_chosen_element
#         while(available_positions_in_next_row==0):
#             index_of_next_available_row = index_of_next_available_row+1
#             available_positions_in_next_row=(len(index_list[index_of_next_available_row])-1)-config[index_of_next_available_row]
#             if (index_of_next_available_row==number_of_rows-1):
#                 if (available_positions_in_next_row==0):
#                     starting_row=starting_row+1
#                     row_index_of_chosen_element=starting_row
#         config[row_index_of_chosen_element] = config[row_index_of_chosen_element]-1
#         config[index_of_next_available_row] = config[index_of_next_available_row]+1
#         return [config,index_of_next_available_row,starting_row]
#     else:

# def configs_generator():
#     config_to_return=start_config
#     for row_index in range(0,number_of_rows-1):
#         for pushed_below in range(0,start_config[row_index]):
#             config_to_return[row_index]=config_to_return[row_index]-pushed_below
#             for remaining_rows_index in range(0,number_of_rows):
#                 if (config_to_return[remaining_rows_index]+pushed_below < len(index_list[remaining_rows_index])):
#                     config_to_return[remaining_rows_index]=config_to_return[remaining_rows_index]+pushed_below

# #return config: [last row with nonzero deviation, start configuration]
# def generate_start_config(deviation):
#     config=[]
#     last_row=0
#     deviation_remaining=deviation
#     for row_index in range(0,number_of_rows):
#         available_positions=min([deviation_remaining,len(index_list[row_index])-1])
#         config.append(available_positions)
#         if (available_positions>0):
#             last_row=row_index
#         deviation_remaining = deviation_remaining - available_positions
#     return [last_row,config]

# def generate_end_config(deviation):
#     config_reversed=[]
#     deviation_remaining=deviation
#     normal_order=range(0,number_of_rows)
#     normal_order.reverse()
#     reversed_order=normal_order
#     for row_index in reversed_order:
#         available_positions=min([deviation_remaining,len(index_list[row_index])-1])
#         config_reversed.append(available_positions)
#         deviation_remaining = deviation_remaining - available_positions
#     config_reversed.reverse()
#     config=config_reversed
#     return config
