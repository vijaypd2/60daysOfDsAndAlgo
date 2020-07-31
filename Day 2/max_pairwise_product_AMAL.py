# python3
# def max_pairwise_product(numbers):
#     n = len(numbers)
#     max_product = 0
#     for first in range(n):
#         for second in range(first + 1, n):
#             max_product = max(max_product,
#                 numbers[first] * numbers[second])
#     return max_product
# def max_pairwise_productFast(numbers):
#     n=len(numbers)
#     max1_index=-1
#     max2_index=-1
#     for i in range(0,n):
#         if numbers[i]>numbers[max1_index]:
#             max1_index=i
#     print(numbers[max1_index])
#     for i in range(0,n):
#         if (i!=max1_index ) and ((max2_index==-1) or (numbers[i]>numbers[max2_index])):
#             max2_index=i
#     print(numbers[max2_index])
#     return (numbers[max1_index]*numbers[max2_index])


def max_pairwise_productSFast(numbers):
    m1 = max(numbers)
    numbers.remove(m1)
    m2 = max(numbers)
    return m1 * m2


if __name__ == "__main__":
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    # print(max_pairwise_product(input_numbers))
    print(max_pairwise_productSFast(input_numbers))
