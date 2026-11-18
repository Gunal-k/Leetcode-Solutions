class Solution:
    def destCity(self, paths: List[List[str]]) -> str:

        starting_cities = set()

        for path in paths:
            starting_cities.add(path[0])

        for path in paths:
            if path[1] not in starting_cities:
                return path[1]
