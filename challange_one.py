


mylist = [1, 0, 1, 0, 1, 0, 1, 1, 0]   #3
mylist = [1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0]   # 3
mylist = [1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0]   # 3

# mylist = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, ]

# mylist = [1]
# mylist = [1, 0]

# mylist = [1, 1]

def calculate_length(in_list):

    def sublist_counter(index, input_list):
        inner_counter = 0
        ret_index = 0

        i = index
        while i < len(input_list)-1:
            ret_index = i
            # print(i, ret_index)
            if input_list[i]!= input_list[i+1]:
                inner_counter +=1
                i = i + 2
                ret_index = i
                # print('case 1', i)
            elif input_list[i] == input_list[i+1] :
                # print('case 2', ret_index + 1)
                return ret_index+1, inner_counter
                
        # print('outer case')
        return ret_index+1, inner_counter


    count = 0
    if len(in_list) == 1:
        return count
    elif len(in_list) == 2:
        if in_list == [1,1] or in_list == [0, 0]:
            return count
        elif  in_list == [1,0] or in_list == [1, 0]:
            return 1
    else:
        index = 0
        sub_count = 0
        while index < len(in_list):
            # print('while index', index)
            index, sub_count = sublist_counter(index, in_list)
            # print('while loop >', index, sub_count)
            if sub_count > count:
                count = sub_count
            else:
                pass
            # break
    return count


print(calculate_length(mylist))