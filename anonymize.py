import os
import json
import os.path
import random

# TODO: this could be done automatically...
courses = ["mib", "miea", "miec", "mieec", "mieic", "miem", "miemm", "mieq"]
years = list(range(2018, 2071)) # professor chibanga só faz erasmus até 2070

ID = 1
def get_next_user():
    global ID
    ID+=1
    animals = ["alligator", "anteater", "armadillo", "aurochs", "axolotl", "badger", "bat", "beaver", "buffalo", "camel", "capybara", "chameleon", "cheetah", "chinchilla", "chipmunk", "chupacabra", "cormorant", "coyote", "crow", "dingo", "dinosaur", "duck", "elephant", "ferret", "fox", "frog", "giraffe", "gopher", "grizzly", "hedgehog", "hippo", "hyena", "ibex", "ifrit", "iguana", "jackal", "jackalope", "kangaroo", "koala", "kraken", "leopard", "lemur", "liger", "loris", "manatee", "mink", "monkey", "moose", "narwhal", "Nyan Cat", "orangutan", "otter", "panda", "penguin", "platypus", "pumpkin", "python", "quagga", "rabbit", "raccoon", "rhino", "sheep", "shrew", "skunk", "squirrel", "tiger", "turtle", "walrus", "wolf", "wolverine", "wombat"]
    return "Anonymous %s %d" % (random.choice(animals).capitalize(), ID)

def anonymize_jsons(jsons):
    # read all users and ids
    users = {}
    for j in jsons:
        j = "archive/%s" % j
        if not os.path.isfile(j): exit(1) 
        with open(j, encoding="utf-8") as f:
            allocation = json.load(f)
            for s in allocation["students"]:
                users[s["id"]]=(get_next_user(), ID)

    # re-iterate and replace with secret
    for j in jsons:
        ja = "anonymous/%s" % j
        j  = "archive/%s" % j
        if not os.path.isfile(j): exit(1)
        # create folders if neeeded
        dira, _ = os.path.split(ja)
        if not os.path.exists(dira): os.makedirs(dira)
        # clear previous values and write output
        with open(j, encoding="utf-8") as f, open(ja, "w", encoding="utf-8") as of:
            allocation = json.load(f)
            anonymous = []
            for s in allocation["students"]:
                s["name"]=users[s["id"]][0]
                s["id"]=users[s["id"]][1]
                anonymous.append(s)
            json.dump(anonymous, of, ensure_ascii=False, indent=2)



for c in courses:
    for y in years:
        base = "archive/"
        path_to_json = "%s/%d/" % (c, y)
        if not os.path.isdir(base + path_to_json): continue
        jsons = [path_to_json + pos_json for pos_json in os.listdir(base + path_to_json) if pos_json.endswith('.json')]
        anonymize_jsons(jsons)
