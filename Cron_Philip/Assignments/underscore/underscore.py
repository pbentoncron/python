class Underscore(object):
    
    def map(self, arr, interatee):
        [val for i in range(10)]
        return [ iteratee(arr[index], index, arr) for index in range(len(arr))]

    def reduce(self, arr, iteratee, memo=none):
        for index in range(len(arr)):
            if not memo and index==0:
                memo = arr[0]
            else:
                memo = iteratee(memo, arr[index], index, arr)
        return memo

    def find(self, arr):
        for ele in arr:
            if predicate(ele): return ele

    def filter(self):
        return [ele for ele in arr if predicate(ele)]

    def reject(self):
        return [ele for ele in arr if not predicate(ele)]

_ = Underscore()

print _.map([1,2,3], lambda val, index, arr: num * 3 )

print _.find([1,2,3,4,5,6], lambda num: num%2==0)

print _.filter([1,2,3,4,5,6], lambda num: num%2==0)

print _.reduce([1,2,3], lambda num, index, arr: num + memo, 0)

