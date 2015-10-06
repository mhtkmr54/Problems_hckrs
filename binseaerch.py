def_binary_search(self,key):
"""Binarysearchforthegivenkeyinthesortedarray."""
	low,high=0,len(self.data)-1
    while low<=high:
		mid=(low+high)//2
		mid_key=self.data[mid]
        if key<mid_key:
			high=mid-1
        elif key>mid_key:
            low=mid+1
        else:
             return mid
    return high+1
