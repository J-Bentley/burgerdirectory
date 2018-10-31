# Credit: Jordan Bentley 2016-01-26
# v2.0
# TODO: Clean code, Lists turn to dictonaries, rjust applied to loop function.

class text:
    BOLD = '\033[1m'
    END = '\033[0m'
    
def loop(burger): #wip, but working...
    for y in burger[0:1]:
        print "\n"+burger[2]
        print"  Bun Type:"
        print"      -"+ y
        y = burger[1]
        print"  Patty Type:"
        print"      -"+ y
        print"  Ingredients:"
    for x in burger[3:]:
        print "      -"+ x

TITLE = """\n__McDONALDS BURGER DIRECTORY__\n A list of burger ingredients\n\n Burgers\n    (1)Hamburger\n    (2)Cheeseburger\n    (3)Double Cheeseburger\n    (4)Junior Chicken\n    (5)McDouble
    (6)McChicken\n    (7)Filet\n    (8)Big Mac\n    (9)Quarter Cheese\n    (10)Quarter BLT\n    (11)Angus Bacon Cheese\n    (12)Angus Mighty\n    (13)The 12    \n\nEnter the number next to a burger to view it\n(0)Display menu\n(00)Exit Program"""

#LIST ASSIGNMENTS: Declares variables equal to a sequence of string constants.
#First/second sequences reserved for bun type/patty type (WIP)
hamburger = ["Regular", "Regular", text.BOLD +"Hamburger"+ text.END,"Ketchup", "Mustard", "Recon Onion", "Pickle"]
cheeseburger = ["Regular", "Regular", text.BOLD +"Cheeseburger"+ text.END,"Ketchup", "Mustard", "Recon Onion", "Pickle", "Cheese"]
double_cheeseburger = ["Regular", "Regular(x2)", text.BOLD +"Double Cheeseburger"+ text.END, "Ketchup", "Mustard", "Recon Onion", "Pickle(x2)", "Cheese(x2)"]
junior_chicken = ["Regular", "Junior", text.BOLD +"Junior Chicken"+ text.END, "Mayonaisse", "Shredded Lettuce"]
mcdouble = ["Regular", "Regular(x2)", text.BOLD +"McDouble"+ text.END, "Ketchup", "Mustard", "Recon Onion", "Pickle(x2)", "Cheese"]
mcchicken = ["Quarter", "McChicken", text.BOLD +"McChicken"+ text.END, "Mayonaisse", "Shredded Lettuce"]
filet = ["Regular(steamed)", "Filet", text.BOLD +"Filet"+ text.END, "TarTar Sauce", "Cheese(1/2)"]
big_mac = ["Mac bun", "Regular(x2)", text.BOLD +"Big Mac"+ text.END, "Mac Sauce", "Recon Onions", "Shredded Lettuce", "Pickle(x2)", "Cheese"]
quarter_cheese = ["Quarter", "Quarter", text.BOLD +"Quarter Cheese"+ text.END, "Ketchup", "Mustard", "Slivered Onion", "Pickle(x2)", "Cheese(x2)"]
quarter_blt = ["Quarter", "Quarter", text.BOLD +"Quarter BLT"+ text.END, "Ketchup", "Mustard", "Slivered Onion", "Mayonaisse", "Bacon", "Leaf Lettuce", "Tomato"]
angus_bacon = ["Angus", "Angus", text.BOLD +"Angus Bacon Cheese"+ text.END, "Ketchup", "Mustard", "Red Onion", "Bacon", "Cheese(x2)"]
angus_mighty = ["Angus", "Angus", text.BOLD +"Angus Mighty"+ text.END, "Mighty Sauce", "Bacon Peices", "Leaf Lettuce", "Tomato", "Grilled Onion"]
the12 = ["Sesame Seed", "Crispy/Grilled Chicken", text.BOLD+"The 12"+text.END, "Applewood Sauce", "Leaf Lettuce", "Tomato", "Swiss Cheese"]

menu = [hamburger, cheeseburger, double_cheeseburger, junior_chicken, mcdouble, mcchicken, filet, big_mac, quarter_cheese, quarter_blt, angus_bacon, angus_mighty, the12]

print TITLE

while True:
    
    inp = raw_input('>>>')
    
    #check for inp == a command
    if inp == "0":
        print TITLE
    elif inp == "00":
        print"> Program Exited."
        exit()
        
    else:
        try:
            loop(menu[int(inp) - 1])
            #execute function 'loop' with paramaeter = <inp>th sequence in menu list - 1
        except:
            print"> %s is not a valid entry!"% (str(inp))

