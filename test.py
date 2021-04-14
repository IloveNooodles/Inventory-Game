responses = {}
polling_active = True

while polling_active:
    name = input("what's your name ?")
    response = input("which mountain would you like to climb")

    responses[name] = response

    repeat = input("would you like to take another poll (Y/N)")
    if repeat == 'N':
        polling_active = False

for name, response in responses.items():
    print(f"{name}, would liek to climb {response}") 
