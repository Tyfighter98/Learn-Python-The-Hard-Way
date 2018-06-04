print("Marry had a little lamb.")
# We can use the .format style on a quotation block inside a print function
print("Its fleece was white as {}.".format("snow"))
print("And everywhere that Marry went.")
# By the "* 20" means print the stuff before in quotations 20 times
print("." * 20)

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r\n"

# The end = " " at the end of the print statement tells the print statement what to do at the end
# Without it Cheese would be on a seperate line than Burger
# We could also make it into one word by including the statement but removign the space inside the quotes
print(end1 + end2 + end3 + end4 + end5 + end6, end = "")
print(end7 + end8 + end9 + end10 + end11 + end12, end = "\nThe end!" * 3)