questions = [
    "Do you have cough?",
    "Do you have fever?",
    "Do you have sore throat?",
    "Do you feel shortness of breath?",
    "Do you have itchy throat?",
    "Do you have runny nose?",
    "Do you have a headache?",
    "Do you have stuffy nose?",
    "Do you feel tired?"
]

threshold = {
    'Mild': 30,
    'Severe':50,
    'Extreme':75
}

def bot(questions, threshold):
    score = 0
    for q in questions:
        ans = input("{} Y|N: ".format(q))
        if ans.lower() == 'y':
            x = int(input("On a scale of 1-10 how bad is it? "))
            score += x
    
    if score>= threshold['Extreme']:
        print("You seem to show extreme symptoms of Covid-19. Please contact nearest hospital for immediate assistance and care.")
    elif score>=threshold['Severe']:
        print("You are showing severe symptoms of COVID-19. It is advised to get yourself checked with the RTPCR test for your safety.")
    elif score>=threshold['Mild']:
        print("You seem to have mild symptoms of COVID-19. It is advised to take care of yourself and see a doctor if the symptoms don't go away in a day or two.")
    else:
        print("You don't seem to have symptoms of COVID-19. But it is important to take care of yourself. Be careful, wear a mask and maintain safe distance from everyone around you.")

    print()
    print("Thank you! Take care. Visit www.arogyasetu.in for more information")

bot(questions, threshold)