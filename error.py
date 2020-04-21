#
# source:: https://www.python-course.eu/python3_exception_handling.php
#
# Example 1

# Without error handling
# def multiply_val():
#     n = int(input("please enter a valid int number "))
#     print("Anwser: "+str(n * 2))

# With error handling
# def multiply_val():
#     while True:
#         try:
#             n = int(input("please enter a valid int number "))
#             print("Anwser: "+str(n * 2))
#             break
#         except ValueError:
#             print("Invalid data type. Please pass in an integer.")

# multiply_val()


# Example 2: Using multiple except clauses
# import sys

# Without error handling
# def compute_readfile(filepath):
#     file = open(filepath)
#     strdata = file.readline()
#     val = int(strdata.strip())
#     print("total value from the file is: ",val)


# With error handling option I
# def compute_readfile(filepath):
#     try:
#         file = open(filepath)
#         strdata = file.readline()
#         val = int(strdata.strip())
#         print("total value from the file is: {0}".format(val))
#     except IOError as error:
#         errno, strerror = error.args
#         print("I/O error({0}): {1}".format(errno,strerror))
#     except ValueError:
#         print("No valid integer in in line")
#     except:
#         print("Unexpected error:", sys.exc_info()[0])
#         raise

# With error handling option II
# def compute_readfile(filepath):
#     try:
#         file = open(filepath)
#         strdata = file.readline()
#         val = int(strdata.strip())
#         print("total value from the file is: {0}".format(val))
#     except (IOError, ValueError):
#         print("An I/O error or a ValueError occurred")
#     except:
#         print("Unexpected error:", sys.exc_info()[0])
#         raise

# compute_readfile('app.txt')


# Example 3
# def format_user_data(user):
#     name, age = user
#     try:
#         age += 1
#         return "{0} is {1} years old".format(name,age) 
#     except (ValueError,  TypeError):
#         return "user age must be a valid integer"

# rs = format_user_data({ "age": "1", "name": "James Moore NTW."})
# print(rs)