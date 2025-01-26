string1 = "data"
string2 = "science"
string3 = "infinity"

len(string1)

string1.index("d")

string1[0]
string3[3:6]

string1.replace("a", "o")
string1a = string1.replace("a", "o")
print(string1a)

string4 = string1 + "-" + string2 + "-" + string3
print(string4)

string4.upper()
string4.lower()
string4.title()

string4.split("-")

string4.count("-")

print('Don't know')
print('Don"t know')

print("He said "one small step for man"")
print('He said "one small step for man"')


print('Don\'t know')
print("He said \"one small step for man\"")


a = 123
type(a)
b = str(a)
type(b)


my_string = "RED ALERT - Meltdown in sector 7G. please contact: Homer"

alert_level = "RED"
error_type = "Meltdown"
sector = "7G"
contact_name = "homer"

my_string = f"{alert_level} ALERT - {error_type} in sector {sector}. please contact: {contact_name}"
print(my_string)



alert_level = "AMBER"
error_type = "Overheating"
sector = "7H"
contact_name = "Lenny"

my_string = f"{alert_level} ALERT - {error_type} in sector {sector}. please contact: {contact_name}"
print(my_string)


my_string = "{} ALERT - {} in sector {}. please contact: {}".format(alert_level, error_type, sector, contact_name)
print(my_string)


my_string = "%s ALERT - %s in sector %s. please contact: %s" % (alert_level, error_type, sector, contact_name)
print(my_string)
















