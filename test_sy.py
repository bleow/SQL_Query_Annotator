import preprocessing

# test code to verify correctness
def test_sy():
    param = ['Bitmap Scan', 'Index Scan', 'Index-only Scan', 'Hash Join', 'Nested Loop Join', 'Materialization']
    result = preprocessing.permutation(param)
    print(result)

test_sy()