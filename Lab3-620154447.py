
def cubicSeries(n):

  i = 0  
  s = 0  

  if n <= 0:
        
      return 0

  else:
        
    while i <= n:
          
           s = s + i**3  
           i = i + 1
         
    return s       
                        

   

def cubicSeries_r(n):

      
       if n<=0:
           return 0

       else:

               return n**3 + cubicSeries_r(n-1)


def power(n):

    if n <= 0:
           return 0

    else:
           return n**n
           
def sumSeries(n):

       if n <= 0:
              return 0
       else:
             return power(n) + sumSeries(n-1)
               
       
       
       
       


   
