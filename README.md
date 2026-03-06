🎯 Podsumowanie workflow
- Tworzysz branch feature
- Kod → commit → push
- PR → develop
- Testy
- Merge do develop
- Po stabilizacji → merge do main
- Usuwasz feature branch

Struktura branchy
main - stabilna wersja projektu, gotowa do prezentacji lub wdrożenia
develop - główna gałąź rozwojowa — tu trafiają ukończone funkcje
feature/ - gałęzie funkcjonalne — każda nowa funkcja ma własny branch
test_validation - środowisko do testów automatycznych



Jak pracować nad nową funkcją?
1️⃣ Utwórz nowy branch feature
git switch -c feature/nazwa_funkcji

2️⃣ Pracuj nad kodem i rób commity
git add .
git commit -m "Opis zmian"

3️⃣ Wypchnij branch na GitHub
git push -u origin feature/adding_locators_to_home_page

4️⃣ Zrób Pull Request → do develop
To jedyne miejsce, gdzie mergujesz feature.
W PR sprawdzasz:
• 	czy kod działa,
• 	czy testy przechodzą,
• 	czy nie ma konfliktów.


5️⃣ Po akceptacji mergujesz do develop
Develop to gałąź, gdzie łączą się wszystkie funkcje.

6️⃣ Gdy develop jest stabilny → merge do main
Main dostaje tylko:
• 	stabilny kod,
• 	przetestowane funkcje,
• 	wersje gotowe do prezentacji.

Branch test_validation (opcjonalny)
Jeśli potrzebujesz osobnego środowiska testowego:
• 	NIE mergujesz tam feature branchy,
• 	NIE mergujesz tam develop,
• 	używasz go tylko do testów automatycznych.



🧹 Usuwanie branchy po zakończeniu pracy
Po zmergowaniu feature do develop możesz go usunąć:

git branch -d feature/adding_locators_to_home_page
git push origin --delete feature/adding_locators_to_home_page




