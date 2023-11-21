import json

import openai

from storage import append_json_to_file

exp_chords = {
    'chords': [
        {
            'chord_name': "Am",
            'velocity': 100,
            'time': 1000
        },
        {
            'chord_name': "Dm",
            'velocity': 103,
            'time': 1000
        },
        {
            'chord_name': "C",
            'velocity': 80,
            'time': 2000
        }
    ]
}


# Function to get a chord name from OpenAI
def get_chords_from_openai(chord_names: list):
    prompt = get_prompt(chord_names)
    response = get_json_from_gpt(prompt)
    chords = json.loads(response.choices[0].message.content)
    append_json_to_file(chords)
    print('chords: ', chords)
    return chords['chords']


def get_json_from_gpt(prompt):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        response_format={"type": "json_object"},
        temperature=1,
        messages=[
            {"role": "system",
             "content": "You are the best musician in the world. Always try to innovate and find new chords."},
            {"role": "user", "content": prompt}
        ]
    )
    return response


def get_prompt(chord_names):
    prompt = f"""
    Give me a chord progression in the key of A minor. here are the chord options:
    {', '.join(chord_names)}.
    I need you to return a json that looks like:
    {json.dumps(exp_chords)}
    
    Try to make a good chord progression with at least 8 chords.
    time field is in milliseconds, velocity is an int between 0-127 and it sets the volume of the chord 
    (try to make it sound humanly but around 80-120)
    """
    print("prompt:", prompt)
    return prompt

