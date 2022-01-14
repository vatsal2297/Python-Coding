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
    ---------.|.---------       1
    ------.|..|..|.------       3  
    ---.|..|..|..|..|.---       5
    -------WELCOME-------
    ---.|..|..|..|..|.---       5
    ------.|..|..|.------       3
    ---------.|.---------       1
    
Size: 11 x 33
    ---------------.|.---------------       1
    ------------.|..|..|.------------       3
    ---------.|..|..|..|..|.---------       5
    ------.|..|..|..|..|..|..|.------       7
    ---.|..|..|..|..|..|..|..|..|.---       9
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---       9
    ------.|..|..|..|..|..|..|.------       7
    ---------.|..|..|..|..|.---------       5
    ------------.|..|..|.------------       3
    ---------------.|.---------------       1
"""