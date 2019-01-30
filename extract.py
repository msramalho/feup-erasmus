from sys import argv, stderr
from sigpy import get_faculty
from sigpy.parser import *
from lxml.html import fromstring
from os.path import isfile, exists
from os import makedirs

# MAIN CONFIGURATIONS
USERNAME = 201403027 if len(argv) < 2 else argv[1]
YEAR = 2018 if len(argv) < 3 else argv[2]
ERASMUS_IDS = [(1012043, "miec"), (1012044, "mieec"), (1012045, "mieic"), (1012046, "mieb"), (1012047, "minas"), (1012025, "miem"), (1012026, "miemm"), (1012027, "mieq"), (1012024, "miea"), (1012023, "mib")]
ERASMUS_PAGE = "https://sigarra.up.pt/feup/pt/coop_candidatura_geral.ver_colocacoes_aluno?pi_processo_view_id=%s"

# WHAT TO EXTRACT
extract = {
    "model": "erasmus",
    "attributes": {
        "page_time": {"regex": "Data das Colocações provisórias: (.*)</p>"},
        "students": {
            "model": "student",
            "list": "True",
            "css": "#conteudoinner > table tr.d",
            "attributes": {
                "phase": {"xpath": ".//td[1]"},
                "order": {"xpath": ".//td[2]"},
                "name": {"xpath": ".//td[3]"},
                "id": {"xpath": ".//td[4]"},
                "grade": {"xpath": ".//td[5]"},
                "country": {"xpath": ".//td[6]"},
                "university": {"xpath": ".//td[7]"},
                "type": {"xpath": ".//td[8]"},
                "option": {"xpath": ".//td[9]"},
            }
        }
    }
}

# LOGIN AND SCRAPE
fac = get_faculty("feup", False)
fac.set_verbose(True)
if not fac.login(USERNAME):
    print("Failed login", file=stderr)
    exit(1)

# SAVE TO FILE
for id, course in ERASMUS_IDS:
    # sigpy parsing
    res = parse_class(fromstring(fac.GET(ERASMUS_PAGE % id, False)), extract)
    if not res.students: 
        print("No result for %s (%s)" % (course, id))
        continue

    # dir and file names
    directory = "archive/%s/%s" % (course, YEAR)
    filename = directory + "/%s.json" % "_".join(res.page_time.replace(":", " ").replace("-", " ").split())
    # check if no override is happening
    if isfile(filename) and input("file '%s' already exists, proceed? (y/n)" % filename) != "y": continue
    # create dir if not present
    if not exists(directory): makedirs(directory)
    # write result to file
    with open(filename, "w", encoding="utf-8") as out: out.write(str(res))

    print("OUPUT: complete to ", filename)

print("DONE courses: ", ERASMUS_IDS)

#TODO: anonymize
