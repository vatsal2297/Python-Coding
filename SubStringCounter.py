#Program which counts the number of occurance of a given substring in a given string

def count_substring(string, sub_string):
    counter = 0
    testString = ""
    #print("before if condition")
    if string.find(sub_string, 0, len(string)) > -1:
        for ch in range(0, (len(string) - len(sub_string)) + 1):
            #print("i = {}".format(ch))
            testString = string[ch:ch+len(sub_string)]
            #print(testString)
            if testString == sub_string:
                #print("testString = {} & substring = {}".format(testString,sub_string))
                counter += 1
    #print(string.find(sub_string, 0, len(string)))
    #print("after if condition")
    return counter

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print("count = {}".format(count))