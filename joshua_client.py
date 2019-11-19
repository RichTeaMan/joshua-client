#!/usr/bin/env python3

import json
import requests
import re

# for reasons unknown, this Joshua endpoint doesn't actually translate anything
baseUrl = 'http://joshua.richteaman.com/translate'

def translate(translateInput: str) -> str:
    result = []

    # text is split into sentences by periods and newlines.
    sentences = re.split(r"[\.\n]", translateInput)

    for sentence in sentences:
        result.append(translateSentence(sentence))
    
    # sentences rejoined by spaced periods.
    return ". ".join(result)

def translateSentence(sentence: str) -> str:

    result = ""

    if sentence:
        url = baseUrl + '?q=' + sentence.replace(' ', '+')
        try:
            response = requests.get(url)
        except Exception as ex:
            print("Request failed with sentence '%s'." % sentence)
            raise ex
        if response.status_code != 200:
            # this should be logged better
            raise RuntimeError('Unsuccessful result from joshua API')

        # a lot more error detection should be done here
        json_data = json.loads(response.text)
        translations = json_data["data"]["translations"]
        for translation in translations:
            result += translation["translatedText"]
    return result

translation = translate("""
Ladies up in here tonight
No fighting
We got the refugees up in here
No fightin', no fightin'
Shakira, Shakira
I never really knew that she could dance like this
She makes a man wants to speak Spanish
Como se llama, bonita, mi casa, su casa (sí, sí)
Shakira, Shakira
Oh, baby, when you talk like that
You make a woman go mad
So be wise and keep on
Reading the signs of my body
I'm on tonight
You know my hips don't lie
And I'm starting to feel it's right
All the attraction, the tension
Don't you see, baby, this is perfection?
Hey, girl, I can see your body moving
And it's driving me crazy
And I didn't have the slightest idea
Until I saw you dancing
And when you walk up on the dance floor
Nobody cannot ignore the way you move your body, girl
And everything so unexpected, the way you right and left it
So you can keep on shaking it
I never really knew that she could dance like this
She makes a man want to speak Spanish
Como se llama, bonita, mi casa, su casa (sí, sí)
Shakira, Shakira
Oh, baby, when you talk like that
You make a woman go mad
So be wise and keep on
Reading the signs of my body
I'm on tonight
You know my hips don't lie
And I am starting to feel you, boy
Come on, let's go, real slow
Don't you see, baby, así es perfecto?
If I know I am on tonight, my hips don't lie
And I'm starting to feel it's right
All the attraction, the tension
Don't you see, baby, this is perfection?
Shakira, Shakira
Oh, boy, I can see your body moving
Half animal, half man
I don't, don't really know what I'm doing
But you seem to have a plan
My will and self-restraint
Have come to fail now, fail now
See, I am doing what I can, but I can't so you know
That's a bit too hard to explain
Baila en la calle de noche
Baila en la calle de día
Baila en la calle de noche
Baila en la calle de día
I never really knew that she could dance like this
She makes a man want to speak Spanish
Como se llama, bonita, mi casa, su casa (sí, sí)
Shakira, Shakira
Oh, baby, when you talk like that
You know you got me hypnotized
So be wise and keep on
Reading the signs of my body
Senorita, feel the conga
Let me see you move like you come from Colombia
Mi vida en Barranquilla se baila así sé
En Barranquilla se baila asi
Yeah, she's so sexy
Every man's fantasy
A refugee like me back with the Fugees from a third world country
I go back like when 'Pac carried crates for Humpty Humpty
We leave the whole club dizzy
Why the CIA wanna watch us?
Colombians and Haitians
I ain't guilty
It's a musical transaction
No more do we snatch ropes
Refugees run the seas 'cause we own our own boats
I'm on tonight, my hips don't lie
And I'm starting to feel you, boy
Come on, let's go, real slow
Baby, like this is perfecto
No fightin'
Oh, you know I'm on tonight, and my hips don't lie
And I am starting to feel it's right
The attraction, the tension
Baby, like this is perfection
No fightin', no fightin', no fightin'""")
print(translation)
