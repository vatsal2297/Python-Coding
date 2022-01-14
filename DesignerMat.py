# This code prints designer mat, given input of two numbers which are deminsions of mat (eg. 11 33)

def designer_mat(n):
    # your code goes here
    num, totalWidth = n.split(' ')
    num = int(num)
    totalWidth = int(totalWidth)
    tempList = []
    tempListRev = []

    for i in range(1,num,2):
        tempList.append((".|." * i).center(totalWidth,'-'))
        tempListRev.append((".|." * i).center(totalWidth,'-'))

    tempList.append("WELCOME".center(totalWidth,'-'))
    tempListRev.reverse()
    tempList.extend(tempListRev)

    for i in tempList:
        print(i)

if __name__ == '__main__':
    n = input()
    designer_mat(n)

"""
Size: 7 x 21 
    ---------.|.---------       
    ------.|..|..|.------         
    ---.|..|..|..|..|.---       
    -------WELCOME-------
    ---.|..|..|..|..|.---       
    ------.|..|..|.------       
    ---------.|.---------       
    
Size: 11 x 33
    ---------------.|.---------------       
    ------------.|..|..|.------------       
    ---------.|..|..|..|..|.---------       
    ------.|..|..|..|..|..|..|.------       
    ---.|..|..|..|..|..|..|..|..|.---       
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---       
    ------.|..|..|..|..|..|..|.------       
    ---------.|..|..|..|..|.---------       
    ------------.|..|..|.------------       
    ---------------.|.---------------       
"""
