def get_summ(one, two, delimiter='&'):
   one=str(one)
   two=str(two)
   #final_sum =' '.join ([one, delimiter, two])  
   final_sum= (f'{one}{delimiter}{two}')
   print(final_sum)
   print(final_sum.upper())

get_summ('Learn', 'python', '&')

