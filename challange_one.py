


mylist = [1, 0, 1, 0, 1, 0, 1, 1, 0]   #3
mylist = [1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0]   # 3
mylist = [1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0]   # 3

# mylist = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, ]

# mylist = [1]
# mylist = [1, 0]

# mylist = [1, 1]

"""adding descriptions ..."""

def calculate_length(in_list):

    def sublist_counter(index, input_list):
        inner_counter = 0
        ret_index = 0

        i = index
        while i < len(input_list)-1:
            ret_index = i

            if input_list[i]!= input_list[i+1]:
                inner_counter +=1
                i = i + 2   # if couple detected [1, 0, 1...] we need to jump with followed element 0 and start new chech with 1, because it 0 is allready counted
                ret_index = i

            elif input_list[i] == input_list[i+1]:

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



#  palindrome integer

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        # even
        elif len(str(x))%2 == 0 and len(str(x)) > 2:
            half = int(len(str(x))/2)
            x_str = str(x)
            x_lst = [i for i in str(x)]

            x_left = x_lst[:half]
            x_right = x_lst[half:]
            x_right.reverse()
            if x_right == x_left:
                return True
            elif x_right != x_left:
                return False
        # odd
        elif len(str(x))%2 != 0:
            x_str = str(x)

            middle = len(str(x))//2 + 1


            x_str = str(x)
            x_lst = [i for i in str(x)]

            x_left = x_lst[:middle-1]
            x_right = x_lst[middle:]

            x_right.reverse()

            if x_right == x_left:
                return True
            elif x_right != x_left:
                return False
        elif len(str(x)) == 0:
            return False

        elif len(str(x)) == 2:
            x_str = str(x)
            if x_str[0] == x_str[1]:
                return True
            else:
                return False
Solution().isPalindrome(1001)



class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        # even

        elif len(str(x))%2 == 0:


            x_str = str(x)
            half = int(len(x_str)/2)
            # print(half)
            for i in range(1, half+1):
                print(i, x_str[half-i], x_str[half-1+i])
                if x_str[half-i] == x_str[half-1+i]:
                    pass
                else:
                    return False
            return True

        # odd
        elif len(str(x))%2 != 0:
            x_str = str(x)

            middle = len(x_str)//2

            for i in range(1, middle+1):
                # print(i, x_str[middle-i], x_str[middle+i])
                if x_str[middle-i] == x_str[middle+i]:
                    pass
                else:
                    return False
            return True
                
        elif len(str(x)) == 0:
            return False

Solution().isPalindrome(00)
