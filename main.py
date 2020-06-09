name = "bruno"

print("hello world")
print(name)

loop_condition = True

while loop_condition:
    print("Loop Condition keeps: %s " %(loop_condition) )
    loop_condition = False

my_integers = [5, 7, 1, 3, 4]
print(my_integers[0]) # 5
print(my_integers[1]) # 7
print(my_integers[4]) # 4

names = [
    "bruno",
    "bianca",
    "angelo"    
]

print(names[0])

names.append("bruna")

for name in names:
    print(name)

dicionary = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}

print(dicionary["key1"])

eu = {
    "nome": "bruno candiani",
    "idade": 24
}

eu["idade2"] = 25

print("Ola, meu nome eh %s, e eu tenho %i anos") %(eu["nome"], eu["idade"])
print(eu)

dictionary = { 
    "aso": "asome_va",
    "achave": "avalor",
    "a": "aletra"
}

for dic in dictionary:
    print("%s --> %s" %(dic, dictionary[dic]))

dictionary = { "some_key": "some_value" }

for key, value in dictionary.items():
    print("%s --> %s" %(key, value))
