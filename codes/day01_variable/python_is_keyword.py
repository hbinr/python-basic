import keyword

print('\n'.join(keyword.kwlist))
# 模块还提供了关键字的判断功能，如pass关键字	表示空的类、方法或函数的占位符
if keyword.iskeyword("pass"):
    print("builtin keyword")
else:
    print("It can be defined.")

# False
# None
# True
# and
# as
# assert
# async
# await
# break
# class
# continue
# def
# del
# elif
# else
# except
# finally
# for
# from
# global
# if
# import
# in
# is
# lambda
# nonlocal
# not
# or
# pass
# raise
# return
# try
# while
# with
# yield
# builtin keyword
