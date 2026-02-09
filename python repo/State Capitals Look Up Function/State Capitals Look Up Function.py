states_and_capitals = {
    "Alabama": "Montgomery",
    "Arizona": "Phoenix",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Illinois": "Springfield",
    "Iowa": "Des Moines",
    "Louisiana": "Baton Rouge",
    "Michigan": "Lansing",
    "Minnesota": "Saint Paul",
    "Missouri": "Jefferson City",
    "Nevada": "Carson City",
    "New York": "Albany",
    "North Carolina": "Raleigh",
    "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City",
    "Oregon": "Salem",
    "Pennsylvania": "Harrisburg",
    "Tennessee": "Nashville",
    "Texas": "Austin",
    "Virginia": "Richmond",
}

state = input('Enter a state :')
state =state.title()
print('The Capital of ' + state + " is " + str(states_and_capitals.get(state, state + " was not found")))  
