# Projekt---Basics-SQL-Python-in-practice

Opis Projektu

Automatyzacja procesu raportowania wyników sprzedaży dla fikcyjnej firmy handlowej Northwind. Skrypt integruje dane z relacyjnej bazy danych SQL, wykonuje przekształcenia analityczne w bibliotece Pandas i generuje gotowy raport biznesowy w formacie Excel.


Główne cele projektu:

Efektywne pobieranie danych z wielu tabel przy użyciu zaawansowanych zapytań SQL.

Obliczenie rzeczywistego przychodu (Revenue) z uwzględnieniem rabatów.

Automatyzacja tworzenia wieloarkuszowych raportów Excel dla kadry zarządzającej.


🛠️ Technologie

Python 

Pandas (Analiza i transformacja danych)

SQL / SQLite (Zarządzanie relacyjną bazą danych)

Openpyxl (Silnik zapisu plików Excel)


🚀 Funkcje Skryptu

Ekstrakcja (Extract): Połączenie z bazą danych i wykonanie zapytania JOIN łączącego tabele Orders, Order Details oraz Employees.

Transformacja (Transform): - Wyliczenie wartości netto każdego zamówienia: Quantity * UnitPrice * (1 - Discount).

Agregacja danych (Group By) w celu stworzenia rankingu wydajności pracowników.

Ładowanie (Load): Eksport danych do pliku .xlsx z podziałem na:

Ranking_Sprzedawców (podsumowanie dla zarządu).

Dane_Szczegółowe (pełna lista transakcji do weryfikacji).


📂 Struktura Projektu

main.py – główny skrypt Python.

northwind2000-simplified.sqlite – źródłowa baza danych.

Excel_raport.xlsx – przykładowy raport wygenerowany przez skrypt.


📈 Przykładowy Wynik (Preview)

Ranking Sprzedawców (Top 3):

Peacock	  232890,846

Leverling	  202812,843

Davolio	  192107,6045


💡 Czego się nauczyłem?

Budowania relacyjnych zapytań SQL w środowisku Python.

Zarządzania pamięcią podręczną poprzez operacje na DataFrame.

Wykorzystania Context Managerów (with) do bezpiecznej obsługi plików.

Praktycznego zastosowania architektury ETL w analizie biznesowej.
