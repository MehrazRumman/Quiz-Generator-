#!python3
#randomquiz-creates quizzes with questions and answers\\
#random order,along with the answer key
import random
#the data ,keys are state or country and values are capitals
capitals={"bangladesh":"Dhaka","India":"delhi","italy":"rome","greece":"athens","pakistan":"islamabad",
"Afghanistan":	"Kabul","Albania":	"Tirana","Algeria":	"Algiers","Andorra	Andorra": "la Vella","Angola"	:"Luanda",
"Antigua and Barbuda":	"Saint John's","Argentina"	:"Buenos Aires","Armenia"	:"Yerevan","Australia"	:"Canberra",
"Austria":	"Vienna","Azerbaijan"	:"Baku", "Bahamas":	"Nassau","Bahrain":	"Manama","Bangladesh":	"Dhaka",
"Barbados":	"Bridgetown","Belarus":	"Minsk","Belgium":	"Brussels","Belize":	"Belmopan","Benin":	"Porto-Novo",
"Bhutan":	"Thimphu","Bolivia":	"Sucre (de jure)","La Paz": "seat of government","Bosnia and Herzegovina":	"Sarajevo",
"Botswana"	:"Gaborone","Brazil":	"Brasilia","Brunei":	"Bandar Seri Begawan","Bulgaria":	"Sofia",
"Burkina Faso":"	Ouagadougou","Burundi":	"Gitega","Cabo":"Verde","Praia":"Cambodia","Phnom":"Penh","Cameroon":"Yaounde",
"Canada":"Ottawa","CentralAfricanRepublic":"Bangui","Chad":"NDjamena","Chile":"Santiago","China":"Beijing","Colombia":
"Bogotá","Comoros":"Moroni","Congo DemocraticRepublicoftheKinshasa":"Congo", "RepublicoftheBrazza":"ville","CostaRica":
"SanJoseCoted","Ivoire	Yamoussoukro":"bal sal",    "Croatia":"Zagreb","Cuba":"Havana","Cyprus":"Nicosia"}
#generate35 quiz files
for quiznum in range(35):
    #todo: create the quiz and answer key files
    qf=open("C:\\Users\\Lenovo\\Desktop\\quizProject\\quiz%s.txt" % (quiznum+1) , "w")
    akf=open("C:\\Users\\Lenovo\\Desktop\\quizProject\\ans%s.txt" % (quiznum+1) , "w")

    #todo:write out the header for the quiz
    qf.write("name:\n\nDate:\nperiod:\n\n")
    qf.write((" "*20)+"State capitals quiz(form %s)"%(quiznum+1))
    qf.write("\n\n")


    #todo: shuffle the order of the states
    s=list(capitals.keys())
    random.shuffle(s)

    #todo : loop through all 50 countries,making a question for each
    for questionnum in range(50):
        #get right and wrong answer.
        ca=capitals[s[questionnum]]
        wa=list(capitals.values())
        del wa[wa.index(ca)]
        wa=random.sample(wa,3)
        ao=wa+[ca]
        random.shuffle(ao)
        #todo : write the question and answer options to quiz file
        qf.write("%s.what is the capital of %s?\n"%(questionnum+1,s[questionnum]))
        for i in range(4):
            qf.write("  %s. %s\n " %("ABCD"[i],ao[i]))
            qf.write("\n")
        #todo: write the answer key to file
        akf.write("%s. %s\n" % (questionnum+1,"ABCD"[ao.index(ca)]))
    qf.close()
    akf.close()





