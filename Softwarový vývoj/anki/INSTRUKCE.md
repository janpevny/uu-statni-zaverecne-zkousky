# Instrukce pro generování ANKI kartiček

Zpracovavam temata na statni zaverecne zkousky bakalarskeho programu v Ceske republice (Unicorn Univerzity), a potrebuji vytvorit ANKI karticky ke kazdemu tematu. Obor je "Softwarový vývoj".

Ke kazdemu podbodu vytvor jednu karticku.

## Struktura souboru s kartičkami

Každý soubor obsahuje kartičky pro jedno téma státních závěrečných zkoušek ve formátu:

```
[Číslo]. [Název tématu] - [Název kartičky]	"[HTML obsah kartičky]"
```

## Formátování kartiček

### HTML struktura
- Použij `<div><strong>Hlavní nadpis</strong></div>`
- Oddělení sekcí: `<div><br></div>`
- Seznamy: `<ul><li><strong>Název</strong> - popis</li></ul>`
- Číslované seznamy: `<ol><li><strong>Název</strong> - popis</li></ol>`

### Obsah kartičky
Každá kartička by měla obsahovat:
1. **Hlavní koncept** - stručná definice
2. **Klíčové body** - 3-5 hlavních bodů
3. **Výhody/Nevýhody** (pokud je relevantní)
4. **Praktické příklady** - konkrétní technologie/nástroje

## Požadavky na obsah

### Délka kartiček
- **Maximálně 8 kartiček na téma**
- Každá kartička pokrývá jeden hlavní podbod
- Obsah kompaktní ale úplný pro zkoušku

### Pokrytí podbodů
Vždy zachovej všechny podbody uvedené v zadání tématu:
- První podbod → 2-3 kartičky
- Druhý podbod → 2-3 kartičky  
- Třetí podbod → 2-3 kartičky

### Styl psaní
- **Technická přesnost** - používej správnou terminologii
- **Stručnost** - pouze klíčové informace
- **Strukturovanost** - jasné rozdělení do sekcí
- **Praktičnost** - konkrétní příklady a technologie

## Příklad struktury tématu

```
3. Uživatelské rozhraní - Základní struktura UI
3. Uživatelské rozhraní - Komponentový přístup  
3. Uživatelské rozhraní - Webové technologie
3. Uživatelské rozhraní - Frontend frameworky
3. Uživatelské rozhraní - CSS frameworky a knihovny
3. Uživatelské rozhraní - Mobilní a cross-platform
3. Uživatelské rozhraní - Nástroje a trendy
3. Uživatelské rozhraní - Performance a přístupnost
```

## Checklist před dokončením

- [ ] 6-8 kartiček
- [ ] Všechny podbody pokryty
- [ ] HTML formátování správné
- [ ] Technické termíny přesné
- [ ] Praktické příklady zahrnuty
- [ ] Obsah vhodný pro státní zkoušky
- [ ] Konzistentní styl s předchozími kartičkami (porovnej s Softwarový vývoj/anki/Architektura cloudových aplikací/1.txt, vice souboru nenacitej)

## Proces vytváření

1. **Vyhledej materiály** k tématu
2. **Identifikuj hlavní podbody** podle zadání
3. **Rozděl obsah** do 8 nebo méně kartiček
4. **Vytvoř kartičky** podle formátu
5. **Zkontroluj úplnost** podle checklistu