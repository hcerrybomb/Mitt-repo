# prj-trafikksystem-simulator
System som simulerer og tracker data fra et registreringspunkt langs en vei

Ting som trengs:

    Man trenger bare 1 python bibliotek for å kjøre systemet, dette er path

    For å installere biblioteket:

    > Åpne cmd (kommandolinje)

    > kjør følgende kommando:

        pip install path

    > ferdig.


Forklaring:

    main.py er hovedskriptet i systemet, når du kjører skripter får du prompter for om du vil
    se hjelp for resten av filene i systemet og deres klasser, og du blir promptet om du vil
    kjøre skriptet som fyller registeret og skriptet som simulerer passeringene til bilene. 

    Å fylle registeret og å kjøre simuleringen er valgfritt, siden denne dataen er allerede
    generert og main.py fungerer uten å generere dem på nytt, men om du ønsker kan du kjøre
    begge for å sjekke at det funker og for å få nye dater å teste på.

    fillregister.py fyller .json registeret med (by default) 100'000 bil objekter med tilfeldige
    realistiske navn, tilfeldige realistiske bilskilt, og tildeldige ekte bilmoddeller. 

    simulator.py bruker registeret og simulerer (by default) ett år med passeringer av bilene
    fra registeret, (by default) blir det cirka 400'000 passeringer, mellom 10 og 100 
    passeringer per time, med parametere som simulerer realistisk rush tid mellom 
    kl 7 og 9 og mellom kl 15 og 17. Dataen fra passeringene samles i en .json fil (data.json)

    main.py bruker dataen fra data.json fra simulatoren og finner dagen(e) med flest passeringer
    og de respektive timene på de dagene med flest passeringer

    Man kan kjøre fillregister.py og simulator.py på egen hånd eller via main.py som en import.
        