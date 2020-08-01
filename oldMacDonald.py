def oldMacDonald(s):
    upper1 = s[0].upper()
    upper2 = s[3].upper()

    newstr = upper1 + s[1:3:1] + upper2 + s[4::]

    return newstr

print(oldMacDonald("ahmadkhan"))