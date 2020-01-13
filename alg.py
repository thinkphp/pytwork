class Algorithm:

      vec = []

      len = -1

      def __init__(self, arr):

          self.vec = arr

          self.len = len(arr)

          self.sorting_with_bubblesort()

      def get(self):

          return self.vec 
 
      def sorting_with_bubblesort( self ):      

           finished = 0

           size = self.len

           while finished == 0:

                 swapped = 0

                 for i in range(0, size - 1):

                     if self.vec[i] > self.vec[i+1]:

                        self.vec[i], self.vec[i+1] = self.vec[i+1], self.vec[i]

                        swapped = 1

                 if swapped == 1:

                     size = size - 1
  
                 else: finished = 1

                      
ob = Algorithm([8,6,5,4,3])

print ob.get()



                    
