print('hello world')
print(3+7)


def greet(msg):
    # new (f-string)
    print("#### new ####")
    print(f"Hello, {msg}")
    print(f"{msg=}")
    print(f"{msg * 2=}")
    # old
    print("#### old ####")
    print("Hello, " + msg)
    print("Hello, %s" % msg)
    print("Hello, {0}".format(msg))


greet("さーさー")

# Execute
# hello world
# 10
# #### new ####
# Hello, さーさー
# msg='さーさー'
# msg * 2='さーさーさーさー'
# #### old ####
# Hello, さーさー
# Hello, さーさー
# Hello, さーさー
