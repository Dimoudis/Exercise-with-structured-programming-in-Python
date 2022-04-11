employees = """Γιώργος Γεωργίου,m,eng,project1 project3 
 Μαρία Ρήγα,f,eng,project2 
 Κατερίνα Σελή,f,secr,project1 project2 
 Νίκος Πάλης,m,tech,project2 
 Λίνα Πενταγιά,f,eng,project1 
 Ρένα Ντορ,f,secr,project3 project2 
 Τζον Κλης,m,tech,project1 project2 
 Λάκης Λαζός,m,eng,project2 
 Μαρίνα Μαρή,f,eng,project3 
 Ζήσης Χελάς,m,tech,project1 project2"""

# αρχικοποίηση των συνόλων (κενα συνολα)
m = set();f = set();eng = set();tech = set()
secr = set();p1 = set();p2 = set();p3 = set()
def load_sets():
    # φόρτωμα των στοιχείων του πίνακα εργαζομένων στα σύνολα
    erg = employees.split("\n")
    
    for string in erg:
        N = string.split(",")
        Name = N[0]
        if "m" in string:
            m.add(Name)
        if "f" in string:
            f.add(Name)
        if "eng" in string:
            eng.add(Name)
        if "tech" in string:
            tech.add(Name)
        if "secr" in string:
            secr.add(Name)
        if "project1" in string:
            p1.add(Name)
        if "project2" in string:
            p2.add(Name)
        if "project3" in string:
            p3.add(Name)

# εκτύπωση set
def show_set(hint, s):
    # βοηθητική συνάρτηση εκτύπωσης συνόλου s με εξήγηση hint
    print(hint,":", s)


# ΑΠΑΝΤΗΣΕΙΣ ΣΤΑ ΕΡΩΤΗΜΑΤΑ
# οι άνδρες που δουλεύουν στο project1
def men_project1():
    show_set("Ανδρες που δουλεύουν στο project1", m&p1)

# όλοι όσοι δουλεύουν στο project1 αλλά όχι στο project2 ή project3
def project1_not_project2_not_project3():
    A = p1 - p2
    B = A - p3
    show_set("Όσοι δουλεύουν στο project1 αλλά όχι στο project2 ή project3", B)

# οι γυναίκες μηχανικοί
def f_eng():
    show_set("Μηχανικοί γυναίκες",f&eng)

# όλοι οι τεχνικοί που δουλεύουν είτε στο project1 ή στο project2
def tech_p1_p2():
    C = p1&tech
    D = p2&tech
    show_set("Τεχνικοί που δουλεύουν είτε στο project1 ή στο project2",C|D)

# οι άνδρες μηχανικοί που δεν δουλεύουν στο project2
def m_eng_not_p2():
    E = m&eng
    K = E - p2
    show_set("Άνδρες μηχανικοί που δεν δουλεύουν στο project2", K)

#### κυρίως πρόγραμμα ####
# αρχικά σύνολα
load_sets()
show_set("Άνδρες", m)
show_set("Γυναίκες", f)
show_set("Μηχανικοί", eng)
show_set("Τεχνικοί", tech)
show_set("Διοικητικοί υπάλληλοι", secr)
show_set("Εργαζόμενοι στο project 1", p1)
show_set("Εργαζόμενοι στο project 2", p2)
show_set("Εργαζόμενοι στο project 3", p3)

### κλήση συναρτήσεων
print("ΑΠΑΝΤΗΣΕΙΣ ΣΤΑ ΕΡΩΤΗΜΑΤΑ:")
men_project1()
project1_not_project2_not_project3()
f_eng()
tech_p1_p2()
m_eng_not_p2()

