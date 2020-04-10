# Correct-windows-live-mail-folders
## English version
This script is used to correct the name of the Windows Live Mail folders, as I found myself having to export the emails to another email software and all the folder names were wrong. This is because, I discovered, folder names are generated almost randomly if they exceed a certain number of letters. The actual name of the folder is contained in a file called `wlmail.fol`
### Code usage
**Attention**; The code eliminates all empty folders that do not contain email, if a folder name contains the characters `/` or `.`, they will be replaced with` -` and `' '` (space) respectively.
How to use:
```sh
$ python3 renameFolder.py --folder folderName/
```
## Versione italiana
Questo script serve a correggere il nome delle cartelle di Windows Live Mail, in quanto mi sono trovato a dover esportare le email su un altro software di posta elettronica e tutti i nomi delle cartelle erano sbagliati. Questo perché, ho scoperto, i nomi delle cartelle vengono generati in modo quasi casuale se superano un certo numero di lettere. Il nome vero e proprio della cartella è contenuto in un file chiamato `wlmail.fol`
### Il codice
**Attenzione**; Il codice elimina tutte le catelle vuote che non contengono email, se un nome di una cartella contiene i caratteri `/` o `.`, verranno rispettivamente rimpiazzati con `-` e `' '` (spazio).
Come si usa:
```sh
$ python3 renameFolder.py --folder folderName/
```