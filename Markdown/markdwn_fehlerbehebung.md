# Fehlerbehebung

### try und except
Mit den try und except Statements kann der Error-Output eines Programmes manipuliert werden. So kann an Stelle des automatisch generierten Error-Codes eine zuvor Bestimmte Nachricht ausgestellt werden.  
Der Code, der potenziell einen Error ausgibt wird in das *try* Statement gesetzt.  
Die Programmausführung springt dann automatisch zum *except* Statement, sobald ein Error auftritt.

```python
print("Durch was für eine Zahl möchtest du 420 teilen? ")
eingabe = int(input())

def beispiel(eingabe):
    try:
        return 420 / eingabe
    except ZeroDivisionError:
        print("Du kannst nicht durch 0 teilen!!!!")

print(beispiel(eingabe))

``````
Hier wird z.B. falls der *ZeroDivisionError* (der Error, der auftritt, wenn durch 0 geteilt wird) manipuliert, indem bei seinem Eintretten nicht der Fehlercode ausgegeben wird, sondern die Nachricht: "Du kannst nicht durch 0 teilen!!!!"

