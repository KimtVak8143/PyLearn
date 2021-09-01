# # File I/O
#
# fp = open("data.txt", "r")
# for emp in fp.readlines():
#     print(emp)
# # print(fp.readable())  # Checks if file has Read access or not
#
# # print(fp.readline())   # Reads the single line and moves the location of cursor
# # print(fp.readlines())  # Puts each line in a list and prints it
# # print(fp.readlines()[1])
# # print(fp.read())   # Reads the whole doc
#
# fp.close()


# Writing
# fp = open("data.txt", "a")  # For append
fp = open("new.txt", "w")  # For writing
fp.write("\nKelly - Customer service")

fp.close()
