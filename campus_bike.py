class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        distances = []
        for i, worker in enumerate(workers):
            for j, bike in enumerate(bikes):
                distance = abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])
                distances.append((distance, i, j))
                print(distances)
		
        
        distances.sort()
        print(distances)

        result = [-1] * len(workers)
        bike_taken = set() 
        for distance, i, j in distances:
            if result[i] == -1 and j not in bike_taken:
                result[i] = j
                bike_taken.add(j)
        return result   
        
        
        
        # get distance of each worker with each bike, add the distance,i,j to list, resulting list of tuples. Sort the list, now we will have smallest distance first in the list.
        # we will have a result array filled with -1 with length of workers and a set to see if the bike is already taken or not. then we need to iterate through list of tuples and will 
        #check if result is -1 and the bike is not already taken, we will add j(bike index) to i(worker index) in result array.
        
        #tc == nm+nmlognm+ nm (length of distances) --> 2nm + nmlognm ---> nmlognm
        #sc == nm+n+m == nm
