import os
import json
import random
import keyring
import markdown

codeFilePath = os.path.realpath(__file__)
parentFilePath = os.path.abspath(os.path.join(codeFilePath,os.pardir))
jsonFilePath = os.path.join(parentFilePath,"values.json")

with open(jsonFilePath) as file:
    d = json.load(file)

for key,value in d.items():
    if value == "":
        d[key] = input("Input "+ key  + ": ")

if keyring.get_password("emailPassword","username") == None:
    password = input("Sender email address password: ")
    keyring.set_password("emailPassword","username", password)


markdownPath = d["markdownPath"]

lineList = []
entryToEmail = []
iteratingLines = True

stringToEmail = ""


with open(markdownPath, encoding="utf8") as file:
    lines = file.readlines()
    for linenum,line in enumerate(lines):
        if len(line) > 2:
            if line[0] == "#" and line[1] == "#" and line[2] == " ":
                lineList.append(linenum)

    randomLine = random.choice(lineList)

    print(randomLine)


    while iteratingLines:
        entryToEmail.append(lines[randomLine])

        randomLine += 1
        print(randomLine)
        if lines[randomLine]:
            if len(lines[randomLine]) > 2:
                if lines[randomLine][0] == "#" and lines[randomLine][1] == "#" and lines[randomLine][2] == " ":
                    iteratingLines = False
        else:
            iteratingLines = False

    for line in entryToEmail:
        stringToEmail = stringToEmail + line
    
    import smtplib
    from email.message          import EmailMessage

    msg = EmailMessage()

    msg["Subject"] = "Journal"
    msg["From"] = d["EmailSender"]
    msg["To"] = d["EmailReceiver"]

    msg.set_content("test")

    html = markdown.markdown(stringToEmail)

    html = "<html><body style='font-size:24px'>" + html + "</body></html>"
    

    msg.add_alternative(html.format(), "html")

    password = keyring.get_password("emailPassword","username")

    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(d["EmailSender"], password)

    server.send_message(msg)

with open(jsonFilePath,"w") as data:
    json.dump(d,data)
