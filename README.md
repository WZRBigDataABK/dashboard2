# Wymagania
| Kod |  Funkcjonalność    | Wymagania      | Kategoria         |
|---------|--------------------|----------------|-------------------|
|FD-001 |Połączenie z API zawierającym dane z NASDAQ    | Wymagane       | funkcjonalne      |
|FD-002 |Wyszukiwarka firm NASDAQ    | Wymagane       | funkcjonalne      |
|FD-003 |Statystyki opisowe i pozycyjne (mediana, średnia,      | Wymagane       | funkcjonalne      |
|FD-004 |Wykres Boxplot    | Wymagane       | funkcjonalne      |
|FD-005 |Wykresy Violin    | Przydatne     | funkcjonalne      |
|FD-006 |Wykres linii dla stopy zwrotu z wolumenu    | Wymagane       | funkcjonalne      |
|FD-007 |Histogram stopy zwrotu dla ceny zamknięcia    | Przydatne       | funkcjonalne      |
|FD-008 |Histogram stopy zwrotu dla wolumenu   | Wymagane       | funkcjonalne      |
|FD-009 |Podsumowanie statystyk stóp zwrotu    | Wymagane       | funkcjonalne      |
|FD-010 |Interaktywność wykresów    | Przydatne       | funkcjonalne      |
|FD-011 |Wykresy linii trendu    | Wymagane       | funkcjonalne      |
|FD-012 |GUI    | Wymagane       | funkcjonalne      |
|FD-013 |System obśługuje jednego użytkownika jednocześnie    | Wymagane       | pozafunkcjonalne      |
|FD-014 |Obsługa w środowisku windows                         | Wymagane       | pozafunkcjonalne      |
|FD-015 |System posługuje się danymi od dnia poprzedniego     | Wymagane       | pozafunkcjonalne      |
|FD-016 |Prognozy   | opcjonalne       | funkcjonalne      |
|FD-017 |zapisywanie portfela użytkownika | opcjonalne       | funkcjonalne      |
|FD-018 |obliczanie ryzyka dla portfela użytkownika | opcjonalne       | funkcjonalne      | 


# Scenariusze Testowe
| Kod Testu | Scenariusz Testowy| Wynik |Tester| Data Testu| Priorytet|
|-------|-------------------|--------|------------|---------------|-------|
|T01| Wyszukiwarka pozwala na wpisywanie stickerów firm | Test Udany | BH | 19/12/2024 | Kluczowy|
|T02| Aplikacja poprawnie pobiera dane o cenach akcji wybranej firmy: należy wybrać firmę i sprawdzić poprawność danych | Test Udany | BH | 19/12/2024 | Kluczowy|
|T03| Aplikacja poprawnie oblicza wskaźniki: należy sprawdzić wyświetlane miary | Test Udany | BH | 19/12/2024 | Kluczowy|
|T04| Aplikacja generuje wszystkie wykresy zawarte w wymaganiach | Test Udany | KP | 19/12/2024 | Kluczowy|
|T05| Aplikacja pozwala na przybliżenie widoku wykresów | Test Udany |AK | 28/12/2024 | Ważny |
|T06| Aplikacja pozwala na pobranie widoku wybranego wykresu jako plik PNG: należy przy każdym wykresie kliknąć ikonę aparatu | Test Udany |AK | 28/12/2024 | Umiarkowany |
|T07| Aplikacja pozwala na zaznaczanie dowolnego obszaru dla wygenerowanych wykresów: | Test Udany |AK | 28/12/2024 | Ważny |
|T08| Aplikacja pozwala na przemieszczanie przybliżenia po całym wykresie szeregu czasowego za pomocą suwaka: należy przybliżyć wykres szeregu czasowego i użyć suwaka umieszczonego pod wykresem | Test Udany |KP | 02/01/2025 | Umiarkowany |
|T09| Aplikacja pozwala na wybranie wartości minimalnych histogramu i poprawnie podświetla słupki histogramu mieszczące się w danym zakresie | Test Udany |KP | 02/01/2025 | Umiarkowany |
