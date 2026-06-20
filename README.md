# Python Calculator Project

Prosty projekt w Pythonie z CLI, testami, formatowaniem, lintowaniem i GitHub Actions.

## Quick Start

### Klonowanie repozytorium

```bash
git clone <adres_repozytorium>
cd python-calculator-ci
```

### Instalacja zależności

```bash
bash scripts/create_venv.sh
```

## Uruchomienie programu

Dodawanie:

```bash
python cli.py add 2 3
```

Odejmowanie:

```bash
python cli.py subtract 5 3
```

## Testy

```bash
bash scripts/test.sh
```

## Formatowanie kodu

```bash
bash scripts/format.sh
```

## Sprawdzenie formatowania

```bash
bash scripts/format_check.sh
```

## Lint

```bash
bash scripts/lint.sh
```

## CI/CD

Workflow GitHub Actions uruchamia się po:

- push na branch main, master lub develop
- pull request do main lub master

Pipeline wykonuje:

1. instalację zależności
2. sprawdzenie formatowania
3. lintowanie
4. testy