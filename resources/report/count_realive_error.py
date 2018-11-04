with open("report.tex", "r") as file:
    lines = file.readlines()
    for index, line in enumerate(lines):
        if line.strip().startswith(("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")):
            elements = line.split("&")
            elements[0] = elements[0].strip()
            R = int(elements[1].replace(".", ""))
            K = int(elements[2].replace(".", ""))
            elements[3] = str(round(((K - R) / R) * 100, 2)) + "\%"
            lines[index] = "	" + "&".join(elements)
with open("report.tex", "w") as file:
    file.writelines(lines)
