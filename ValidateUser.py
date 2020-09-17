import re
class Validation:
    def isEmail(self):
        try:
            while 1:
                email = input("Enter Email: ")
                emailRegex = re.compile(r"[\w.+-]+@[\w-]+\.[\w]{2,5}")
                if(re.search(emailRegex,email)):
                    return email
                else :
                    print("<< Enter valid email >>")
        except:
            pass
    
    def isPhone(self):
        try:
            while 1:
                phone = input("Enter Mobile no.: ")
                phoneRegex = re.compile(r"^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s0-9]*$")
                if(re.search(phoneRegex,phone)):
                    return phone
                else :
                    print("<< Enter valid phone number >>")
        except:
            pass