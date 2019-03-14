#.7 Write a function that removes the dollar sign (“$”) in a string, named remove_dollar_sign, takes 1 arguments: s, where s is the input string, returns the new string with no dollar sign in it

def remove_dollar_sign(s):
    dolar_sigh = s.replace("$","")
    return dolar_sigh

n = input("Please enter a sentence with $:")
print("After remove $:",remove_dollar_sign(n))
string_with_no_dollars = remove_dollar_sign("$80% percent of $life is to show $up")
if string_with_no_dollars == "80% percent of life is to show up":
    print("Your function is correct")
else:
    print("Oops, there's a bug")

