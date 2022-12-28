import matplotlib.pyplot as plt

def assignment(new_list, new_index, old_list, old_index):
    new_list[new_index] = old_list[old_index]


def mergeSort(input_list):
    if (
        len(input_list) > 1
        and not len(input_list) < 1
        and len(input_list) != 0
    ):
        mid = len(input_list) // 2
        left = input_list[:mid]
        right = input_list[mid:]

        mergeSort(left)
        mergeSort(right)

        left_iter = 0
        right_iter= 0
        combined_iter = 0

        while left_iter < len(left) and right_iter< len(right):
            if left[left_iter] <= right[right_iter]:
                assignment(input_list, combined_iter, left, left_iter)
                left_iter += 1
            else:
                assignment(input_list, combined_iter, right, right_iter)
                right_iter+= 1
            combined_iter += 1

        while left_iter < len(left):
            input_list[combined_iter] = left[left_iter]
            left_iter += 1
            combined_iter += 1

        while right_iter< len(right):
            input_list[combined_iter] = right[right_iter]
            right_iter+= 1
            combined_iter += 1



my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

x = range(len(my_list))

fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, sharey = True, figsize=(14, 7))

ax1 = plt.subplot(1, 2, 1)
plt.ylabel("Wert", fontsize=20) 
plt.xlabel("Position in Liste", fontsize=20)
x = range(len(my_list))
plt.scatter(x, my_list, label="Listeneintrag")
plt.title("Liste vor Mergesort",fontsize=20)
plt.legend(loc="upper right", frameon=True, fontsize=15)

mergeSort(my_list)

ax2 = plt.subplot(1, 2, 2)
plt.xlabel("Position in Liste", fontsize=20)
plt.scatter(x, my_list, label="Listeneintrag")
plt.title("Liste nach Mergesort", fontsize=20)
plt.legend(loc="upper left", frameon=True, fontsize=15);
