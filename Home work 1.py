## Mohsen Pourdehghan


regmsg = """ Hi there, thanks for the registration.
please answer the questions about yourself.
"""

print(regmsg)

fname= input("what is your first name? ")

lname= input("what is your last name? ")

age= int(input("How old are you? "))

country= input("Where is your country? ")

city= input("Which city do you come from? ")

address= input("Your home address? ")

email= input("Your business e-mail? ")

driving_licence= input("Do you have driving licence? Yes/No ")

degree= input("What is your degree of education? ")

work_xp= int(input("How many years of work experience do you have? "))


if age >= 20 and work_exp >= 2 :

    ## Scenario 1

    print(f"""

    Scenario 1:

    =======

    ♦ thanks for your submission, this is your info:

    First name: {fname}

    Last name: {lname}

    Age: {age}

    Country: {country}

    City: {city}

    Address: {address}

    Email: {email}

    Driving licence: {driving_licence}

    Degree: {degree}

    Years of work experience: {work_xp}

    =======

    ...Wait for the announcement!...

    """)

else :

    ## Scenario 2

    print(f"""

    Scenario 2:

    =======

    ♦ You do not have at least 2 years of work experience
        and at least 20 years of age.
    
    ...Sorry, we cant confirm your registration :(...

    """)

