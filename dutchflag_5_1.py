def pivot_arr(pivot_index, A):
    pivot = A[pivot_index]
    smaller = 0
    for i in range(len(A)):
        print('Checking', A[i], '>', pivot)
        if A[i] < pivot:
            print('Swapping', A)
            A[i], A[smaller] = A[smaller], A[i]
            print('\t', A)
            smaller += 1

    larger = len(A) - 1
    for i in reversed(range(len(A))):
        print('Checking', A[i], '<', pivot)
        if A[i] < pivot:
            break
        elif A[i] > pivot:
            print('Swapping', A)
            A[i], A[larger] = A[larger], A[i]
            print('\t', A)
            larger -= 1
    print(A)


def dutch_swap(pivot_index, A):
    pivot = A[pivot_index]
    smaller, equal, larger = 0, 0, len(A)
    print('\tStarting with', A, 'swaping on index', pivot_index)
    while equal < larger:
        print('Comparing', A[equal], 'and', pivot)
        if A[equal] < pivot:
            print('Swapping', A)
            A[smaller], A[equal] = A[equal], A[smaller]
            print('\t', A)
            smaller, equal = smaller + 1, equal + 1
        elif A[equal] == pivot:
            equal += 1
            print('\t', A)
        else:  # when A[equal] > pivot
            print('Swapping', A)
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]
            print('\t', A)
    print(A)


if __name__ == "__main__":
    arr = [4, 5, 2, 3, 1, 6, 8]
    arr1 = [4, 5, 2, 3, 1, 6, 8]
    pivot_arr(3, arr)
    dutch_swap(3, arr1)
