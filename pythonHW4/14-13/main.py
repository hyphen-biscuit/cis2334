# Dashiell Wendt 2033998
num_calls = 0

def partition(user_id_list, i, k):
    midpoint = i + (k - i) // 2
    center = user_id_list[midpoint]
    
    done = False
    l = i
    h = k
    while not done:
        while user_id_list[l] < center:
            l = l + 1
        while center < user_id_list[h]:
            h = h - 1
        if l >= h:
            done = True
        else:
            temp = user_id_list[l]
            user_id_list[l] = user_id_list[h]
            user_id_list[h] = temp
            l = l + 1
            h = h - 1
    return h
    
def quicksort(user_id_list, i, k):
    j = 0
    global num_calls
    num_calls += 1
    if i >= k:
        return
    j = partition(user_id_list, i, k)
    quicksort(user_id_list, i, j)
    quicksort(user_id_list, j + 1, k)
    return

if __name__ == "__main__":
    user_id_list = []
    user_id = input()
    while user_id != "-1":
        user_id_list.append(user_id)
        user_id = input()
    quicksort(user_id_list, 0, len(user_id_list) - 1)
    print(num_calls)
    for user_id in user_id_list:
        print(user_id)