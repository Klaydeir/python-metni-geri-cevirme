def reverse(value, output=[]):
    #range(start, stop, step)
    for i in range(len(value) - 1, -1, -1):
        output.append(value[i])
    
    return "".join(output)

text = input("What's up: ")
print("Your reversed text is: {}".format(reverse(text)))