# Demonstrate 5 common Python string methods

text = "  python programming is fun and easy!  "

print("Original text:", text)
print("1. strip() ->", text.strip())
print("2. upper() ->", text.upper())
print("3. lower() ->", text.lower())
print("4. replace() ->", text.replace("python", "Python"))
print("5. split() ->", text.strip().split())

# Extra example of find()
print("6. find('programming') ->", text.strip().find("programming"))