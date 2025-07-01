from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Inițializarea bazei de date
def init_db():
    with sqlite3.connect('database.db') as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS articles (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        content TEXT NOT NULL)''')
        c.execute('''CREATE TABLE IF NOT EXISTS messages (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        email TEXT NOT NULL,
                        message TEXT NOT NULL)''')
        conn.commit()

# Exemplu dummy pentru tipuri de date primitive
exemplu_int = 10  # int - număr întreg
dummy_float = 3.14  # float - număr zecimal
dummy_bool = True  # bool - valoare logică
dummy_str = "Exemplu"  # str - șir de caractere

# Exemplu dummy pentru structuri de date
lista_dummy = [1, 2, 3]  # listă
set_dummy = {"rosu", "verde", "albastru"}  # set
tuplu_dummy = (45.76, 23.45)  # tuplu
dict_dummy = {"cheie": "valoare"}  # dicționar

@app.route("/")
def index():
    return render_template("index.html", title="Acasă")

@app.route("/cv")
def cv():
    return render_template("cv.html", title="CV")

@app.route("/projects")
def projects():
    return render_template("projects.html", title="Proiecte")

@app.route("/articles")
def articles():
    with sqlite3.connect('database.db') as conn:
        c = conn.cursor()
        c.execute("SELECT title, content FROM articles")
        articles = [{"title": row[0], "content": row[1]} for row in c.fetchall()]
    return render_template("articles.html", title="Articole", articles=articles)

@app.route("/articles/new", methods=["GET", "POST"])
def new_article():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        with sqlite3.connect('database.db') as conn:
            c = conn.cursor()
            c.execute("INSERT INTO articles (title, content) VALUES (?, ?)", (title, content))
            conn.commit()
        return redirect(url_for("articles"))
    return render_template("new_article.html", title="Adaugă articol")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        with sqlite3.connect('database.db') as conn:
            c = conn.cursor()
            c.execute("INSERT INTO messages (name, email, message) VALUES (?, ?, ?)", (name, email, message))
            conn.commit()
        return redirect(url_for("index"))
    return render_template("contact.html", title="Contact")

# Exemplu dummy de clasă, obiect și constructor
class Masina:
    def __init__(self, marca):  # constructor
        self.marca = marca

masina1 = Masina("Dacia")  # obiect

# Exemplu dummy complet pentru cei 4 piloni OOP

# Încapsulare
class Cont:
    def __init__(self, parola):
        self.__parola = parola  # atribut protejat

# Moștenire
class Animal:
    def sunet(self):
        return "Face un sunet"

class Caine(Animal):
    def sunet(self):  # polimorfism
        return "Ham ham"

# Abstracție
class Vehicul:
    def porneste(self):
        raise NotImplementedError("Aceasta este o metoda abstracta")

class Bicicleta(Vehicul):
    def porneste(self):
        return "Bicicleta a pornit"

# Polimorfism

def afiseaza_sunet(animal):
    print(animal.sunet())

# Exemplu dummy pentru structura conditionala if-elif-else
nota = 8.5  # exemplu de variabilă numerică

if nota >= 9:
    print("Ai obținut calificativul: Excelent")
elif nota >= 7:
    print("Ai obținut calificativul: Bun")
else:
    print("Ai obținut calificativul: Suficient")


# Exemplu apel
caine = Caine()
afiseaza_sunet(caine)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
