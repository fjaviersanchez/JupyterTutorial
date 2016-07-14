#Solution code for exercise 1
#We make a loop to make the element by element product of two lists, we then compare to numpy
def list_product(list1,list2):
    new_list=list1
    if(len(list1)==len(list2)):
        try:
            for i,row in enumerate(list1):
                for j,el in enumerate(row):
                    new_list[i][j]=list1[i][j]*list2[i][j]
        except:
            print('Both arrays should have the same dimensions')
    return new_list
    
