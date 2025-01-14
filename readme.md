# LB 324

WICHTIG: Dieses Projekt verwendet pre-commit hooks, um die Codequalität zu gewährleisten. Die Hooks sind so konfiguriert, das bei jedem push der Code getested und formatiert wird.

## Aufgabe 2
Setup pre-commit:
(Erklären Sie hier, wie man `pre-commit` installiert.)

- Als erstes klonnt man das repo auf die Locale maschiene um daran arbeiten zu können.
- Fals installiert, deinstallieren sie die alte versione von flake8:

`pip uninstall flake8`

- Um pre-commit reibungslos laufen zu lassen installiert man nun die richtigen, compatible version:

`pip install flake8==7.1.1`

- Nun kann man im ROOT-Directory vom Projekt folgende Commands eingeben um pre-commit herunterzuladen:

`pip install pre-commit`

`pre-commit install`

- Füge folgenden command aus um sicherzugehen das alle hooks up to date sind:

`pre-commit autoupdate`


## Aufgabe 4
Erklären Sie hier, wie Sie das Passwort aus Ihrer lokalen `.env` auf Azure übertragen.
