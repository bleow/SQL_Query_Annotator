import preprocessing

# code
def test_sy():
    param = ['Bitmap Scan', 'Index Scan', 'Hash Join', 'Nested Loop Join', 'Materialization']
    result = preprocessing.permutation(param)
    print(result)

test_sy()