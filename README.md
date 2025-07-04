Portofoliu Online - Python & Flask

Acest proiect reprezintă un portofoliu online personal, dezvoltat cu ajutorul limbajului Python și framework-ului Flask, destinat prezentării experienței profesionale, proiectelor și articolelor personale, precum și pentru facilitarea contactului direct printr-un formular funcțional.

Caracteristici și funcționalități
Pagini disponibile:
Acasă
Pagina principală care oferă o prezentare concisă și atractivă a profilului personal.

CV
O pagină dedicată afișării datelor profesionale, competențelor, educației și experienței relevante, în format clar și accesibil.

Proiecte
Listă cu proiectele personale realizate, fiecare cu descriere și link către codul sursă disponibil pe GitHub, facilitând astfel demonstrarea competențelor tehnice.

Articole
Secțiune de tip blog, unde pot fi publicate articole personale, reflecții sau materiale tehnice, gestionate dinamic prin intermediul bazei de date.

Contact
Formular funcțional care permite vizitatorilor să trimită mesaje direct către proprietar, cu salvarea acestora într-o bază de date SQLite, pentru o gestionare eficientă și organizată a comunicării.

Funcționalități tehnice:
Backend robust realizat cu Flask, care gestionează rutele, procesează datele și interacționează cu baza de date.

Baza de date SQLite folosită pentru stocarea articolelor și a mesajelor primite prin formularul de contact, asigurând persistența și securitatea datelor.

Template-uri HTML folosind Jinja2 pentru generarea dinamică a conținutului și o interfață prietenoasă utilizatorului.

Design responsive și intuitiv, care asigură o experiență consistentă atât pe desktop, cât și pe dispozitive mobile.

Validarea și gestionarea mesajelor trimise prin formular pentru o comunicare eficientă cu vizitatorii.

Instrucțiuni de instalare și utilizare
Cerințe preliminare
Python 3.x instalat

Pip (gestionarul de pachete Python)

Pași pentru rulare locală
Clonează sau descarcă acest repository.

Deschide un terminal în directorul proiectului.

Instalează Flask rulând:

bash
Copiază
Editează
pip install flask
Pornește serverul local cu comanda:

bash
Copiază
Editează
python app.py
Deschide un browser și accesează adresa:


http://127.0.0.1:5000
Structura directorului

|-- app.py              # Fișierul principal care rulează aplicația Flask
|-- database.db         # Baza de date SQLite pentru articole și mesaje
|-- /templates          # Șabloane HTML pentru paginile aplicației
|-- /static             # Resurse statice (CSS, imagini, JavaScript)
|-- README.md           # Documentația proiectului

Beneficii ale proiectului
Permite o prezentare profesională și modernă a profilului personal online.

Facilitează demonstrarea competențelor tehnice prin expunerea proiectelor și articolelor personale.

Oferă un canal de comunicare direct și organizat cu potențiali angajatori sau colaboratori prin formularul de contact.

Este un exemplu de proiect funcțional, ușor de extins și personalizat pentru diverse nevoi profesionale.

Posibile îmbunătățiri viitoare
Adăugarea autentificării pentru administrarea articolelor și mesajelor.

Implementarea paginilor suplimentare (ex: portofoliu foto, recomandări).

Integrarea cu servicii externe pentru trimiterea email-urilor din formularul de contact.

Optimizarea designului pentru accesibilitate și SEO.

