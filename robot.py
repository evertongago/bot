import aiml

kernel = aiml.Kernel()
kernel.setBotPredicate('name', 'Rambo')
kernel.setBotPredicate('master', 'Sam Trautman')
kernel.learn("database.xml")

while True:
    print kernel.respond(raw_input(">> "))
