words = ['this' , 'is', 'a', 'sentence', '.']
def word_inplace(words):
            return words[::-1]
            
print(word_inplace(words))

a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'
alist = a_text.lower().split()
new_dict = {}
def dictionary(alist):
    for e in alist:
        new_dict[e] = alist.count(e)
    return new_dict
print(dictionary(alist))

list = [1,2,3,4,5,6,23,5,643,7,754]

def search_algorithm(list, target):
    for e in list:#O(n)
        if e == target:#O(1)
            return target#O(1)
# time complexity = linear or O(n)
print(search_algorithm(list, 6))
