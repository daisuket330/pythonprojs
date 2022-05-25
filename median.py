def median(iterable):
#     #""obtains the central value of a series.
#     sorts the iterable and returns middle vlue if there is an even number
#     args:
#         iterable:a series of ordereable items.
#     returns:the median value.
items = sorted(iterable)
median_index = (len(items))