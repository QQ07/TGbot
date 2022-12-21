import doer as d
import payCalculator as pc

def responses(msg):
    
    # print(msg[0])
    if msg[0] == "#":
        #  print ("calculating responses...")
         if(msg[:6]=="#admin"):
             return d.perform(msg[7:])
    
    elif msg[0:msg.find(' ')].lower() == "payroll":
        print("Calculating payroll")
        return pc.Payroll(msg)
    
    msg = msg.lower()
    if msg in ("hello", "hi", "sup", "hey"):
        return "Hey! How are you doing?"

    if msg in ("who are you", "who r u?", "who are you?"):
        return "I am Payroll Calculator bot!"
    if msg in ("what can you do"):
        return "I can calculate payroll of employees,\nclick /help to know more..."
    else :
        return "unable to get you"
    