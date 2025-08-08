import csv

# Datei lesen
with open("personen.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    personen = list(reader)

ok = 0
fehler = 0
aktiv = 0

def ist_gueltig(p):
    # Name und Email müssen vorhanden sein
    if not p["name"] or not p["email"]:
        return False
    # Email muss ein @ enthalten
    if "@" not in p["email"]:
        return False
    return True

for p in personen:
    if not ist_gueltig(p):
        fehler += 1
        continue
    if p["aktiv"].lower() == "true":
        aktiv += 1
    ok += 1

gesamt = ok + fehler
anteil_aktiv = aktiv / gesamt * 100 if gesamt else 0

print(f"Gültig: {ok}")
print(f"Fehler: {fehler}")
print(f"Aktiv: {aktiv} ({anteil_aktiv:.1f}%)")