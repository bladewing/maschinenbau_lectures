studenten = {"erich", "kurt", "franz", "herbert"}
studentinnen = {"linda", "heike", "anja"}
preistraeger = {"friedrich", "anja"}

studis = studenten | studentinnen

stud_preistraeger = preistraeger & studis

print(studis)
print(stud_preistraeger)
