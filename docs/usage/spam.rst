*************
Obsługa spamu
*************

W okresie funkcjonowania systemu mogą wystąpić niepożądąne sytuacje związane z dostarczaniem przez systemy informatyczne
urzędu, albo – ze względu na publikacje adresów e-mail – inne podmioty niezamawianych informacji
takich jak informacje handlowe, kartki świąteczne, których wartość informacyjna w konkretnej sprawie jest znikoma.

W celu obsługi tego rodzaju korespondencji został wprowadzony mechanizm zgłaszania spamu i oznaczania wiadomości jako
spam.

Uprawnienia
-----------

System - w celu efektywnego rozłożenia zadań – wyposażony jest w mechanizm uprawnień. Osoba, która utworzyła monitoring
ma możliwość zarządzania nim i dysponuje wszelkimi uprawnieniami do tego. Może nadawać i odbierać uprawnienia
użytkownikom w danym monitoringu, a także nadawać im uprawnienia do takiego samego zarządzania.

Istnieją następujące uprawnienia związane z obsługą spamu:

Może widzieć dzienniki – ``can_view_log``
    uprawnia do zapoznania się z dziennikiem zgłoszeń w monitoringu

Może oznaczyć spam – ``spam_mark``
    uprawnia zapewniające dostęp do przycisku "Zgłoś spam" poprzez natychmiastowe ukrycie wiadomości

Proces obsługi
--------------

Na ekranie dowolnej wiadomości dostępny jest przycisk "Zgłoś spam". Po jego wybraniu przez użytkownika niezalogowanego
wiadomości trafiają do dziennika zgłoszeń.

Użytkownik, który posiada uprawnienie ``can_view_log`` otrzymuje powiadomienie o nowym wpisie w dzienniku
zgłoszeń.

Użytkownik zalogowany, który posiada uprawnienie ``mark_spam`` po wybraniu przycisku "Oznacz spam" może ukryć
wiadomość oznaczoną jako spam. Ewentualnie wiadomość zostanie oznaczona jako prawidłowa, a wówczas nie będzie możliwe
ponowne zgłoszenie wiadomości jako spam. W obu przypadkach wpisy w dzienniku dotyczące danej wiadomości zostaną oznaczone
jako załatwione.

Wiadomość oznaczona jako spam – ze względów dowodowych i potencjalnego przyszłego wykorzystania np. uczenie maszynowego
automatycznego oznaczania podejrzanych wiadomości – nie jest całkowicie z systemu usunięta. Jest ona wyłącznie
wycofywana z publikacji. Z tego też względu nie należy wprowadzać niezgodne z stanem faktycznym oznaczenia wiadomości
jako spam, gdyż może to w przyszłości zakłócić maszynowe wnioskowanie.

Analiza bezpieczeństwa
----------------------

Wiadomości, które są publikowane w systemie mogą zawierać złośliwe oprogramowanie, albowiem pochodzą od niezaufanych,
zewnętrznych dostawców. Na dzień 10 lutego 2017 roku wiadomości są publikowane bez żadnej analizy antywirusowej.

Nawet w przypadku wprowadzenia takich mechanizmów - ze względu na niedoskonałość oprogramowania antywirusowego - będziemy
w stanie wykryć wyłącznie wirusy poznane przez konkretny silnik antywirusowy.

W przypadku wiadomości zawierającej podejrzany załącznik:

#. **nie pobieraj, ani nie otwieraj pliku na komputerze**,
#. skopiuj adres URL pliku,
#. przejdź na VirusTotal_ do zakładki "URL"
#. wprowadź adres pliku i zatwierdź, aby uzyskać raport z badania adresu URL, który odnosi się do historii wiarygodności strony, ale  nie treści,
#. w sekcji "Downloaded file" wybierz odnośnik, aby uzyskać raport z skanowania pliku przez wiele, niezależnych silników antywirusowych:

    #. w przypadku wyniku negatywnego - plik prawdopodobnie nie jest wirusem lub nie jest jeszcze znany oprogramowaniu antywirusowemu,
    #. w przypadku wyniku pozytywnego - niezwłocznie poinformuj Administratora Bezpieczeństwa Informacji oraz Administratora Systemu.

Administrator powinien:

#. zweryfikować nadesłane zgłoszenie,
#. zachować adres załączników i adres wiadomości,
#. podjąć działania, które uniemożliwią zapoznanie się z treścią i ochronią systemy informatyczne:

    #. przeanalizować nagłówki wiadomości w celu oceny celowości zgłoszenia do źródła przypadku nadużycia,
    #. usunąć wiadomość w ramach modułu ``django_mailbox.Messages`` wraz z załącznikiem ``.eml`` i załącznikami binarnymi,
    #. usunąć wiadomość w ramach modułu ``letters.Letter`` wraz z plikiem ``.eml`` i załącznikami binarnymi,
    #. zweryfikować np. programem ``curl`` czy pierwotny adres z załącznikami został skutecznie usunięty.

Należy zaznaczyć, że zagrażającym wiarygodności Stowarzyszenia jest sytuacja, gdy rozpowszechnia ono złośliwe
oprogramowanie. W takim przypadku przeglądarki internetowe i firmy antywirusowe mogą oznaczyć wszystkie strony danego
podmiotu jako niebezpieczne i uniemożliwić dostęp użytkownikom, co poważnie zakłóci realizacje podstawowych celów
Stowarzyszenia.

.. _VirusTotal: https://www.virustotal.com/
