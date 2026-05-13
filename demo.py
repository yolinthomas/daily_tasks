status="start"
while status=="start":
    user=input("user input:")
    if "ur name" == user:
        print("AI:my self nemo")
    elif "how are u?" == user:
        print ("AI:yah good,u")
    elif "fine gud"== user:
        print ("AI: ok")
    elif "what are u doing" == user:
        print ("AI:nthg replying to u")
    elif "what is your age?" == user:
        print ("AI:i have no age,Iam a bot")
    elif "where ru from" == user:
        print ("AI:iam from internet")
    elif "do you have friends" == user:
        print ("AI:yes,all users are my friends")
    elif "what is your hobby?" == user:
        print ("AI:my hobby is chatting with people")
    elif "do u eat food" == user:
        print("AI:no,i run on electricity")
    elif "do u sleep" == user:
        print ("AI:no,iam always awake")
    elif "bye" == user:
        status="stop"
    else:
        print ("invalid")
    
