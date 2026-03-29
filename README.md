# Peirce Continuum PoC — Relational Sheaf Algebra als operationales Modell für Spektroskopie und Überkritikalität

Kurzpitch  
Peirces Kontinuum interpretiert Messwerte als lokale Sektionen relationaler Garben. Dieses PoC zeigt reproduzierbare numerische Beispiele für K‑Schalenbindungsenergien in zwei Kernmodellen, liefert drei präzise, falsifizierbare Vorhersagen und stellt minimalen Code bereit, mit dem experimentelle Gruppen und Numeriker schnell prüfen können, ob die vorgeschlagenen Signaturen in realen Daten auftreten.

## Zielsetzung
Dieses Projekt zeigt, wie eine relationale, topologisch geprägte Sichtweise auf Spektroskopie und Überkritikalität konkret gerechnet und geprüft werden kann. Es dokumentiert erste numerische Befunde und liefert reproduzierbare Werkzeuge, um die vorgeschlagenen Signaturen experimentell zu testen.

## Inhalt des Repos
- src/dirac_radial_solver.py — Minimaler radialer Dirac‑Solver (1s, κ = −1) mit zwei Kernmodellen: punkt‑reguliert und homogene Kugel  
- notebooks/PoC.ipynb — Demo‑Notebook zur schnellen Visualisierung der Ergebnisse  
- data/ — Beispiel‑CSV‑Format für Ergebnisdaten  
- results/ — Beispielplots (E₁s vs Z)  
- predictions.md — Drei falsifizierbare Vorhersagen mit kurzen Messprotokollen  
- OUTREACH.md — Vorlagen für Kontaktaufnahme und kurze Beschreibungen  
- requirements.txt — Abhängigkeiten für lokale Reproduktion

## Schnellstart (kurz)
1. Repository klonen.  
2. Abhängigkeiten installieren mit: pip install -r requirements.txt  
3. Minimalen Sweep ausführen mit: python src/dirac_radial_solver.py --model sphere --R_fm 5.0 --Z_max 200  
4. Ergebnisse: CSVs in data/ und Plot in results/E1s_vs_Z.png. Öffne notebooks/PoC.ipynb für interaktive Auswertung.

## Kernergebnisse dieses PoC
- Punktkern (numerisch reguliert) reproduziert die formale Erscheinung bei Z ≈ 137.  
- Homogene Kugel mit R = 5 fm zeigt kein Eintauchen des 1s‑Zustands bis Z = 200; die kritische Ladung ist modellabhängig und liegt deutlich über 137.  
- Vakuumpolarisation (Uehling‑Term) wirkt stabilisierend und verschiebt die kritische Ladung weiter nach oben.

## Drei prägnante Vorhersagen (Kurzfassung)
1. K‑Schalen‑Residuum — Systematische Abweichung von Dirac‑Fock‑Werten für K‑Schalen bei Z ≳ 150; erwartete Größenordnung 10–200 eV.  
2. Positronen‑Zeitprofil — Bei temporär überkritischen Schwerionenkollisionen charakteristische Positronen‑Zeitprofile und Sum‑Energy‑Peaks.  
3. Skalenproportionale Residuen — Nicht‑eliminierbare, skalenproportionale Residuen in Präzisionsfits über verschiedene Z‑Skalen, korrelierbar mit numerisch berechneter Kohomologie.  
Details zu Messprotokollen und Signaturtests stehen in predictions.md.

## Reproduzierbarkeit und Erweiterungsmöglichkeiten
- Das Minimalskript ist bewusst einfach gehalten; Erweiterungen vorgesehen: Uehling‑Potential (Vakuumpolarisation), Dirac‑Fock‑Screening, feinere Z‑Auflösung, alternative Kernmodelle (z. B. Fermi‑Verteilung).  
- Konvergenztests und numerische Hinweise sind im Notebook dokumentiert; die Skripte sind so strukturiert, dass Anpassungen schnell möglich sind.

## Projektstruktur (Übersicht)
peirce-continuum-poc/  
├─ README.md  
├─ requirements.txt  
├─ src/  
│  └─ dirac_radial_solver.py  
├─ notebooks/  
│  └─ PoC.ipynb  
├─ data/  
│  └─ example_E1s_sphere.csv  
├─ results/  
│  └─ E1s_vs_Z.png  
├─ predictions.md  
└─ OUTREACH.md

## Lizenz
Dieses Projekt steht unter der MIT‑Lizenz. Siehe LICENSE für Details.

## Hinweise zur Nutzung
Die hier präsentierten Rechnungen sind ein Proof of Concept. Die numerischen Ergebnisse sind modellabhängig und dienen als Ausgangspunkt für weitergehende, präzisere Rechnungen und experimentelle Tests. Reproduktionsskripte und Notebooks sind so gestaltet, dass sie schnell angepasst und erweitert werden können.

## Nächste sinnvolle Schritte
- Systematische Einrechnung des Uehling‑Potentials für Z in [150, 210] mit feiner Auflösung.  
- Implementierung eines einfachen Dirac‑Fock‑Screenings zur Abschätzung von Mehrteilchen‑Effekten.  
- Kontaktaufnahme zu experimentellen Gruppen für kurze Datenchecks oder Testläufe.

## Mitmachen
Issues und Pull Requests sind willkommen. Für Reproduktionsfragen bitte relevante Logausgaben und die verwendeten Parameter anhängen.
