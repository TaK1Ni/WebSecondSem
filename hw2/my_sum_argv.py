import sys

def my_sum_argv(arr):
    return sum(map(int, arr))

if __name__ == "__main__":
    args = sys.argv[1:]  
    if not args:
        print("Usage: python my_sum_argv.py num1 num2 num3  ")
    else:
        nums = [int(num) for num in args]  
        result = my_sum_argv(nums)
        print(result)