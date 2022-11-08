#Dash Wendt 2033998
def selection_sort_descend_trace(integers):
   for i in range(len(integers) - 1):
        index_smallest = i
        for j in range(i + 1, len(integers)):
            if integers[j] > integers[index_smallest]:
                index_smallest = j
        temp = integers[i]
        integers[i] = integers[index_smallest]
        integers[index_smallest] = temp
        for num in integers:
            print(str(num), end=' ')
        print()

if __name__ == "__main__":
    integers = [int(num) for num in input("").split()] 
    selection_sort_descend_trace(integers)