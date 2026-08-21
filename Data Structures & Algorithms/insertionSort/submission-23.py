
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        results = []

        # insertsion sort = insert val into sorted array (left subarray behind i)

        for i in range(len(pairs)):
            j = i - 1
            while j >= 0 and pairs[j].key > pairs[j + 1].key:
                tmp = pairs[j + 1]
                pairs[j + 1] = pairs[j]
                pairs[j] = tmp
                j -= 1

            results.append(list(pairs))

        return results