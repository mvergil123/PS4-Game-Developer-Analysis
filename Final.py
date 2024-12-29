# Mike Vergil
# CSCI 128 Section L
# Final Project
# PS4 Games

# imports
import csv, matplotlib.pyplot as plt


# function to find all of the development names and put them into the list (x axis)
def get_x():
    developers = []

    file = open("ps4_games.csv", "r")
    csvreader = csv.reader(file)
    #skip the header
    header = next(csvreader)
    #append them in the lists
    for row in csvreader:
        developers.append(row[4])
    # return list for x axis values
    return developers


# function to find the number of times the developer appears
# you can do a for loop that iterates through each 
# then append it into a list because it should be in order.
def count_dev(dev_names):
    occurence = []
    for dev in dev_names:
        count = 0
        count = (dev_names.count(dev), dev)
        occurence.append(count)
        # clean up the y values
    # first one is going to be just getting rid of repeats and then I will get rid of the tuple

    unique_values = []
    appended_values = set()

    for item in occurence:
        if item[1] not in appended_values:
            unique_values.append(item)
            appended_values.add(item[1])
    return unique_values

    
def clean_y(values):
    y = []
    for i in values:
        y.append(float(i[0]))
    
    return y

def clean_x(developers):
    # clean up the list by making sure that they only appear once
    x = []
    for dev in developers:
        if dev not in x:
            x.append(dev)
    return x


# function to create the graph and show/store it
def create_graph(x,y):
    plt.bar(x, y)
    plt.title("Developers on Best Selling PS4 Games")
    plt.xlabel("Developer")
    plt.ylabel("Occurence")
    plt.xticks(rotation=90)
    plt.savefig("goat_developer.png")

# find the best developer
def find_goat(developers):
    #should be square enix
    count = 0
    goat = ""
    for d in developers:
        if int(d[0]) > count:
            count = int(d[0])
            goat = d

    return goat




# General code
if __name__ == "__main__":
    dev = get_x()
    y_tuple = count_dev(dev)
    y = clean_y(y_tuple)
    x = clean_x(dev)
    create_graph(x,y)
    winner = find_goat(y_tuple)
    print("OUTPUT The developer with the most games on the list is", winner[1],"with", winner[0], "games!")

