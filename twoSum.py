



def twoSum(array, target):
    hashmap = {}
    potentialMatch = 0

    for i in range(len(array)):
        hashmap[array[i]] = i 
        print(hashmap[array[i]], "i", i)

    for i in range(len(array)):
        potentialMatch = target - array[i] 
        print("PotentialMatch", hashmap[potentialMatch])
        if potentialMatch in hashmap and hashmap[potentialMatch] != i:
            return [i, hashmap[potentialMatch]]    

array = [10,40,50,60,80,90,100]
print(twoSum(array, 140))