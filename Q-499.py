# Write a “pager” program. Your solution should prompt for a filename, and display the text file 25 lines at a time, pausing 
# each time to ask the user to enter the word “continue”, in order to show the next 25 lines or enter the word “stop” to close 
# the file.


fname=input("Enter File Name: ")
with open(fname) as f:
    for i,j in enumerate(f):
        if i%25==0 and i:
            x=input("Press 'q' to exit and press any key to continue..")
            if x.lower()=="q":
                break
        else:
            print(j,end='')
