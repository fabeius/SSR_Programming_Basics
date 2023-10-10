# Fuktionen

Eine Funktion ist wie ein "Mini-Programm" innerhalb eines Programmes.
Also zum Beispiel:

```python
def hello():
    print("Howdy!")
    print("Howdy!!")
    print("Hello there!")

hello()
hello()
hello()
``````

Mit der *def* Aufrufung wird eine Funktion Namens *hello* definiert.  
Diese wird dann drei Mal ausgeführt. Die Funktion wird erst ausgeführt wenn sie aufgerufen wird. Nicht wenn sie definiert wird.  
  
  ### Parameter
Ein Parameter ist ähnlich wie eine Variable. In einem Parameter ist ein Argument gespeichert, welches beim Aufrufen der Funktion dann benutzt wird.  
Ein Parameter wird nach dem Ausführen der Funktion "vergessen". Er muss also bei einer weiteren Ausführung wieder neu eingespeist werden.

### Return

Das, was die geschriebene Funktion dann schlussendlich ausgibt, wird als *return value* bezeichnet.  
Achtung!! --> die lokalen Variablen werden nach dem Gebrauch der Funktion wieder gelöscht!

### Local und Global Scope
Alle Variablen, die in einer Funktion definiert werden, sind per default in diesem "lokalen Raum" gespeichert.  
Alle Variablen, welche ausserhalb von Funktionen definiert werden, werden im "globalen Raum" gespeichert. 

```python
def localScope()
    localVariable = 12  #dies ist die Variable im Local Scope
    Beispiel == 15

Beispiel = 18 #Dies ist die Variable im global Scope

localScope()
print(Beispiel)
```
Ausgabe:    18  
Notiz:
- die lokalen Variablen werden nach dem Gebrauch der Funktion wieder gelöscht.
- Lokale Variablen können nicht im global Scope verwendet werden.
- Local Scopes können nicht auf Variablen anderer Local Scopes zugreifen.
- Local Scopes können globale Variablen benutzen.
    - mit dem Statement *global* + VariablenNamen können globale Variablen auch innerhalb von Funktionen manipuliert werden.
