# BeautifulSoup is a library that is used to parse and navigate
# through HTML files.  We'll use it to pull the information
# out of the "drinks.html" file that is in the same folder
from bs4 import BeautifulSoup

# Start out by opening the "drinks.html" file. The 'r' indicates
# that we only want to read out of it. (other options would
# include 'w' for writing, and 'r+' for reading and writing)
document = open("./drinks.html", 'r')

# Read the full file into a string!  After this line, insert
# `print source` to see what it read
source = document.read()

# Give the source to BeautifulSoup to parse.  After this line,
# insert `print soup.prettify()` and compare it to the
# `print source` invocation earlier.
soup = BeautifulSoup(source, 'html.parser')

# I noticed that all the recipies are inside of a div with
# the class "blog_list_items", so I'll find that element.
main_content = soup.find(**{"class": "blog_list_items"})

# Each individual recipie is inside its own div with
# the class "row", so we'll find all of them and put them
# in a list
recipies = main_content.find_all("div", **{"class": "row"})

# For each of the recipies that we've found...
for recipie in recipies:
    # Extract the cocktail name from the "header 3" tag
    name = recipie.find("h3").text

    # Extract the ingredients list from the "list item" tag
    ingredients = recipie.find_all("li")

    # Print out the name
    print name

    # Followed by a list of ingredients!
    for ingredient in ingredients:
        print " *", ingredient.text

    # Followed by a new line
    print ""
