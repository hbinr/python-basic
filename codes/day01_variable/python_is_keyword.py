import keyword

print('\n'.join(keyword.kwlist))
if keyword.iskeyword("pass"):
    print ("builtin keyword")
else:
    print ("It can be defined.")

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
#     nonlocal
#     not
#     or
#     pass
#     raise
#     return
#     try
#     while
#     with
#     yield