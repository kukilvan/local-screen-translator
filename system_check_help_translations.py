HELP_TRANSLATIONS_EXTRA = {
    "de": {
        "LST-SYS-001": ("Nicht unterstützte Windows-Konfiguration", [
            "Verwenden Sie eine 64-Bit-Version von Windows 10 oder Windows 11.",
            "Installieren Sie alle verfügbaren Windows-Updates.",
            "Starten Sie Windows neu und führen Sie die Systemprüfung erneut aus.",
        ]),
        "LST-GPU-001": ("NVIDIA-GPU oder Treiber wurde nicht erkannt", [
            "Prüfen Sie im Geräte-Manager, ob die NVIDIA-GPU ohne Fehler angezeigt wird.",
            "Installieren oder reinstallieren Sie den offiziellen NVIDIA-Treiber.",
            "Starten Sie Windows neu und führen Sie die Systemprüfung erneut aus.",
        ]),
        "LST-GPU-002": ("Der NVIDIA-Treiber ist zu alt", [
            "Installieren Sie den neuesten NVIDIA-Treiber für Ihre Grafikkarte.",
            "Starten Sie Windows danach neu.",
            "Führen Sie die Systemprüfung erneut aus.",
        ]),
        "LST-GPU-003": ("Die NVIDIA-GPU ist nicht kompatibel", [
            "Diese GPU unterstützt die erforderliche CUDA/Paddle-Umgebung nicht.",
            "Verwenden Sie eine neuere kompatible NVIDIA-GPU.",
            "Installieren Sie CUDA Toolkit nicht manuell; die Anwendung enthält die benötigte Laufzeit.",
        ]),
        "LST-GPU-004": ("Zu wenig Grafikspeicher", [
            "Schließen Sie Spiele, Browser und andere GPU-intensive Programme.",
            "Führen Sie die Systemprüfung erneut aus und prüfen Sie den freien VRAM.",
            "Falls die Übersetzung weiterhin fehlschlägt, verwenden Sie eine GPU mit mehr VRAM.",
        ]),
        "LST-GPU-010": ("Mehrere NVIDIA-GPUs wurden erkannt", [
            "Die aktuelle Version verwendet NVIDIA GPU 0.",
            "Prüfen Sie in den technischen Details, welche Grafikkarte als gpu:0 angezeigt wird.",
            "Falls die falsche GPU verwendet wird, ändern Sie die GPU-Konfiguration in Windows/NVIDIA.",
        ]),
        "LST-CAP-001": ("Der Bildschirm konnte nicht korrekt erfasst werden", [
            "Stellen Sie sicher, dass der gewünschte Monitor mit der NVIDIA-GPU verbunden ist.",
            "Versuchen Sie den Modus Randloses Fenster / Borderless Windowed.",
            "Starten Sie Local Screen Translator danach neu und führen Sie die Prüfung erneut aus.",
        ]),
        "LST-NET-001": ("Der lokale Port 11435 wird bereits verwendet", [
            "Schließen Sie andere lokale KI-Anwendungen und Ollama-Instanzen.",
            "Starten Sie Local Screen Translator neu.",
            "Falls das Problem bleibt, starten Sie Windows neu und öffnen Sie zuerst Local Screen Translator.",
        ]),
        "LST-TTS-001": ("Keine geeignete englische Microsoft-Stimme gefunden", [
            "Öffnen Sie die Einstellungen von Local Screen Translator.",
            "Wählen Sie ein englisches Microsoft-Sprachpaket und installieren Sie es.",
            "Starten Sie Windows neu, falls dies verlangt wird.",
        ]),
        "LST-CUDA-001": ("GPU-OCR konnte nicht gestartet werden", [
            "Aktualisieren oder reinstallieren Sie den NVIDIA-Treiber.",
            "Starten Sie Windows neu und schließen Sie GPU-intensive Programme.",
            "Installieren Sie Python, PaddlePaddle oder CUDA Toolkit nicht manuell.",
        ]),
        "LST-FILE-001": ("Eine erforderliche Anwendungsdatei fehlt", [
            "Laden Sie einzelne Modelle oder DLL-Dateien nicht manuell herunter.",
            "Prüfen Sie den Schutzverlauf von Windows-Sicherheit auf quarantänisierte Dateien.",
            "Installieren Sie die vollständige Anwendung erneut; Setup.exe und alle .bin-Dateien müssen nebeneinander liegen.",
        ]),
        "LST-ALIGN-001": ("Die Textausrichtung konnte nicht gestartet werden", [
            "Prüfen Sie Windows-Sicherheit auf eine blockierte LSTAlignWorker.exe.",
            "Falls die Datei entfernt wurde, installieren Sie die Anwendung vollständig neu.",
            "Starten Sie Windows neu und führen Sie die Prüfung erneut aus.",
        ]),
        "LST-DATA-001": ("Die Anwendung kann Einstellungen nicht speichern", [
            "Prüfen Sie, ob Ihr Windows-Konto in den AppData-Ordner schreiben darf.",
            "Prüfen Sie Controlled Folder Access und andere Sicherheitssoftware.",
            "Führen Sie die Systemprüfung erneut aus.",
        ]),
        "LST-AI-001": ("Die lokalen Übersetzungsmodelle konnten nicht gestartet werden", [
            "Aktualisieren Sie den NVIDIA-Treiber und starten Sie Windows neu.",
            "Schließen Sie andere KI-Programme und GPU-intensive Anwendungen.",
            "Falls Modelle fehlen, installieren Sie die Anwendung vollständig neu.",
        ]),
        "LST-GEN-001": ("Die Systemprüfung hat ein Problem gefunden", [
            "Starten Sie Windows neu und führen Sie die Systemprüfung erneut aus.",
            "Suchen Sie im Internet nach dem genauen Fehlertext aus den technischen Details.",
            "Falls Dateien fehlen, installieren Sie die Anwendung vollständig neu.",
        ]),
    },

    "fr": {
        "LST-SYS-001": ("Configuration Windows non prise en charge", [
            "Utilisez une version 64 bits de Windows 10 ou Windows 11.",
            "Installez toutes les mises à jour Windows disponibles.",
            "Redémarrez Windows puis relancez la vérification du système.",
        ]),
        "LST-GPU-001": ("GPU NVIDIA ou pilote non détecté", [
            "Vérifiez dans le Gestionnaire de périphériques que le GPU NVIDIA est détecté sans erreur.",
            "Installez ou réinstallez le pilote NVIDIA officiel.",
            "Redémarrez Windows puis relancez la vérification.",
        ]),
        "LST-GPU-002": ("Le pilote NVIDIA est trop ancien", [
            "Installez le dernier pilote NVIDIA disponible pour votre carte graphique.",
            "Redémarrez Windows après l’installation.",
            "Relancez la vérification du système.",
        ]),
        "LST-GPU-003": ("Le GPU NVIDIA n’est pas compatible", [
            "Ce GPU ne peut pas utiliser l’environnement CUDA/Paddle requis.",
            "Utilisez un GPU NVIDIA compatible plus récent.",
            "N’installez pas CUDA Toolkit manuellement ; l’application fournit son propre environnement.",
        ]),
        "LST-GPU-004": ("Mémoire vidéo insuffisante", [
            "Fermez les jeux, navigateurs et autres applications utilisant fortement le GPU.",
            "Relancez la vérification et consultez la quantité de VRAM libre.",
            "Si la traduction échoue encore, utilisez un GPU disposant de plus de VRAM.",
        ]),
        "LST-GPU-010": ("Plusieurs GPU NVIDIA ont été détectés", [
            "La version actuelle utilise le GPU NVIDIA 0.",
            "Consultez les détails techniques pour savoir quelle carte correspond à gpu:0.",
            "Si le mauvais GPU est utilisé, modifiez la configuration GPU dans Windows/NVIDIA.",
        ]),
        "LST-CAP-001": ("La capture d’écran n’a pas fonctionné correctement", [
            "Vérifiez que l’écran concerné est connecté au GPU NVIDIA.",
            "Essayez le mode Fenêtré sans bordure / Borderless Windowed.",
            "Redémarrez Local Screen Translator puis relancez la vérification.",
        ]),
        "LST-NET-001": ("Le port local 11435 est déjà utilisé", [
            "Fermez les autres applications d’IA locales et les instances d’Ollama.",
            "Redémarrez Local Screen Translator.",
            "Si le problème persiste, redémarrez Windows et lancez d’abord Local Screen Translator.",
        ]),
        "LST-TTS-001": ("Aucune voix anglaise Microsoft utilisable n’a été trouvée", [
            "Ouvrez les paramètres de Local Screen Translator.",
            "Choisissez et installez un pack vocal anglais Microsoft.",
            "Redémarrez Windows si nécessaire.",
        ]),
        "LST-CUDA-001": ("Impossible de démarrer l’OCR GPU", [
            "Mettez à jour ou réinstallez le pilote NVIDIA.",
            "Redémarrez Windows et fermez les applications utilisant fortement le GPU.",
            "N’installez pas Python, PaddlePaddle ou CUDA Toolkit manuellement.",
        ]),
        "LST-FILE-001": ("Un fichier requis de l’application est manquant", [
            "Ne téléchargez pas manuellement des modèles ou DLL individuels.",
            "Consultez l’historique de protection de Sécurité Windows.",
            "Réinstallez l’application complète avec Setup.exe et tous les fichiers .bin placés ensemble.",
        ]),
        "LST-ALIGN-001": ("Le composant d’alignement du texte n’a pas pu démarrer", [
            "Vérifiez si Windows Sécurité a bloqué LSTAlignWorker.exe.",
            "Si le fichier a été supprimé, réinstallez complètement l’application.",
            "Redémarrez Windows puis relancez la vérification.",
        ]),
        "LST-DATA-001": ("L’application ne peut pas enregistrer ses paramètres", [
            "Vérifiez que votre compte Windows peut écrire dans le dossier AppData.",
            "Vérifiez Controlled Folder Access et les autres logiciels de sécurité.",
            "Relancez la vérification du système.",
        ]),
        "LST-AI-001": ("Les modèles de traduction locaux n’ont pas pu démarrer", [
            "Mettez à jour le pilote NVIDIA puis redémarrez Windows.",
            "Fermez les autres applications d’IA et les programmes utilisant fortement le GPU.",
            "Si des modèles sont manquants, réinstallez complètement l’application.",
        ]),
        "LST-GEN-001": ("La vérification du système a détecté un problème", [
            "Redémarrez Windows puis relancez la vérification.",
            "Recherchez sur Internet le texte exact de l’erreur affichée dans les détails techniques.",
            "Si des fichiers manquent, réinstallez complètement l’application.",
        ]),
    },

    "it": {
        "LST-SYS-001": ("Configurazione Windows non supportata", [
            "Usa una versione a 64 bit di Windows 10 o Windows 11.",
            "Installa tutti gli aggiornamenti Windows disponibili.",
            "Riavvia Windows ed esegui nuovamente il controllo del sistema.",
        ]),
        "LST-GPU-001": ("GPU NVIDIA o driver non rilevato", [
            "Controlla in Gestione dispositivi che la GPU NVIDIA sia rilevata senza errori.",
            "Installa o reinstalla il driver NVIDIA ufficiale.",
            "Riavvia Windows ed esegui nuovamente il controllo.",
        ]),
        "LST-GPU-002": ("Il driver NVIDIA è troppo vecchio", [
            "Installa il driver NVIDIA più recente disponibile per la tua GPU.",
            "Riavvia Windows dopo l’installazione.",
            "Esegui nuovamente il controllo del sistema.",
        ]),
        "LST-GPU-003": ("La GPU NVIDIA non è compatibile", [
            "Questa GPU non supporta l’ambiente CUDA/Paddle richiesto.",
            "Usa una GPU NVIDIA compatibile più recente.",
            "Non installare CUDA Toolkit manualmente; l’applicazione include il proprio runtime.",
        ]),
        "LST-GPU-004": ("Memoria video insufficiente", [
            "Chiudi giochi, browser e altre applicazioni che utilizzano intensamente la GPU.",
            "Esegui nuovamente il controllo e verifica la VRAM libera.",
            "Se la traduzione continua a non funzionare, usa una GPU con più VRAM.",
        ]),
        "LST-GPU-010": ("Sono state rilevate più GPU NVIDIA", [
            "La versione attuale utilizza NVIDIA GPU 0.",
            "Controlla nei dettagli tecnici quale scheda è indicata come gpu:0.",
            "Se viene usata la GPU sbagliata, modifica la configurazione GPU in Windows/NVIDIA.",
        ]),
        "LST-CAP-001": ("Impossibile acquisire correttamente lo schermo", [
            "Assicurati che il monitor desiderato sia collegato alla GPU NVIDIA.",
            "Prova la modalità Finestra senza bordi / Borderless Windowed.",
            "Riavvia Local Screen Translator ed esegui nuovamente il controllo.",
        ]),
        "LST-NET-001": ("La porta locale 11435 è già utilizzata", [
            "Chiudi altre applicazioni IA locali e istanze di Ollama.",
            "Riavvia Local Screen Translator.",
            "Se il problema continua, riavvia Windows e avvia prima Local Screen Translator.",
        ]),
        "LST-TTS-001": ("Nessuna voce inglese Microsoft utilizzabile trovata", [
            "Apri le impostazioni di Local Screen Translator.",
            "Scegli e installa un pacchetto vocale inglese Microsoft.",
            "Riavvia Windows se richiesto.",
        ]),
        "LST-CUDA-001": ("Impossibile avviare l’OCR GPU", [
            "Aggiorna o reinstalla il driver NVIDIA.",
            "Riavvia Windows e chiudi le applicazioni che usano intensamente la GPU.",
            "Non installare manualmente Python, PaddlePaddle o CUDA Toolkit.",
        ]),
        "LST-FILE-001": ("Manca un file necessario dell’applicazione", [
            "Non scaricare manualmente singoli modelli o DLL.",
            "Controlla la cronologia protezione di Sicurezza di Windows.",
            "Reinstalla l’applicazione completa con Setup.exe e tutti i file .bin nella stessa cartella.",
        ]),
        "LST-ALIGN-001": ("Impossibile avviare il componente di allineamento del testo", [
            "Controlla se Sicurezza di Windows ha bloccato LSTAlignWorker.exe.",
            "Se il file è stato rimosso, reinstalla completamente l’applicazione.",
            "Riavvia Windows ed esegui nuovamente il controllo.",
        ]),
        "LST-DATA-001": ("L’applicazione non può salvare le impostazioni", [
            "Controlla che il tuo account Windows possa scrivere nella cartella AppData.",
            "Controlla Controlled Folder Access e altri software di sicurezza.",
            "Esegui nuovamente il controllo del sistema.",
        ]),
        "LST-AI-001": ("Impossibile avviare i modelli di traduzione locali", [
            "Aggiorna il driver NVIDIA e riavvia Windows.",
            "Chiudi altre applicazioni IA e programmi che utilizzano intensamente la GPU.",
            "Se mancano dei modelli, reinstalla completamente l’applicazione.",
        ]),
        "LST-GEN-001": ("Il controllo del sistema ha rilevato un problema", [
            "Riavvia Windows ed esegui nuovamente il controllo.",
            "Cerca sul Web il testo esatto dell’errore presente nei dettagli tecnici.",
            "Se mancano file, reinstalla completamente l’applicazione.",
        ]),
    },

    "es-ES": {
        "LST-SYS-001": ("Configuración de Windows no compatible", [
            "Utiliza una versión de 64 bits de Windows 10 o Windows 11.",
            "Instala todas las actualizaciones disponibles de Windows.",
            "Reinicia Windows y vuelve a ejecutar la comprobación del sistema.",
        ]),
        "LST-GPU-001": ("No se detectó la GPU NVIDIA o su controlador", [
            "Comprueba en el Administrador de dispositivos que la GPU NVIDIA aparezca sin errores.",
            "Instala o reinstala el controlador oficial de NVIDIA.",
            "Reinicia Windows y vuelve a ejecutar la comprobación.",
        ]),
        "LST-GPU-002": ("El controlador NVIDIA es demasiado antiguo", [
            "Instala el controlador NVIDIA más reciente para tu tarjeta gráfica.",
            "Reinicia Windows después de instalarlo.",
            "Vuelve a ejecutar la comprobación del sistema.",
        ]),
        "LST-GPU-003": ("La GPU NVIDIA no es compatible", [
            "Esta GPU no puede ejecutar el entorno CUDA/Paddle necesario.",
            "Utiliza una GPU NVIDIA compatible más reciente.",
            "No instales CUDA Toolkit manualmente; la aplicación incluye su propio entorno.",
        ]),
        "LST-GPU-004": ("Memoria de vídeo insuficiente", [
            "Cierra juegos, navegadores y otros programas que utilicen mucho la GPU.",
            "Vuelve a ejecutar la comprobación y revisa la VRAM libre.",
            "Si la traducción sigue fallando, utiliza una GPU con más VRAM.",
        ]),
        "LST-GPU-010": ("Se detectaron varias GPU NVIDIA", [
            "La versión actual utiliza NVIDIA GPU 0.",
            "Consulta los detalles técnicos para ver qué tarjeta aparece como gpu:0.",
            "Si se utiliza la GPU incorrecta, cambia la configuración de GPU en Windows/NVIDIA.",
        ]),
        "LST-CAP-001": ("No se pudo capturar correctamente la pantalla", [
            "Asegúrate de que el monitor deseado esté conectado a la GPU NVIDIA.",
            "Prueba el modo Ventana sin bordes / Borderless Windowed.",
            "Reinicia Local Screen Translator y vuelve a ejecutar la comprobación.",
        ]),
        "LST-NET-001": ("El puerto local 11435 ya está siendo utilizado", [
            "Cierra otras aplicaciones de IA locales e instancias de Ollama.",
            "Reinicia Local Screen Translator.",
            "Si continúa, reinicia Windows y abre primero Local Screen Translator.",
        ]),
        "LST-TTS-001": ("No se encontró una voz inglesa de Microsoft utilizable", [
            "Abre los ajustes de Local Screen Translator.",
            "Selecciona e instala un paquete de voz inglesa de Microsoft.",
            "Reinicia Windows si es necesario.",
        ]),
        "LST-CUDA-001": ("No se pudo iniciar el OCR mediante GPU", [
            "Actualiza o reinstala el controlador NVIDIA.",
            "Reinicia Windows y cierra los programas que utilicen intensamente la GPU.",
            "No instales Python, PaddlePaddle ni CUDA Toolkit manualmente.",
        ]),
        "LST-FILE-001": ("Falta un archivo necesario de la aplicación", [
            "No descargues modelos o DLL individuales manualmente.",
            "Comprueba el Historial de protección de Seguridad de Windows.",
            "Reinstala la aplicación completa con Setup.exe y todos los archivos .bin juntos.",
        ]),
        "LST-ALIGN-001": ("No se pudo iniciar el componente de alineación de texto", [
            "Comprueba si Seguridad de Windows ha bloqueado LSTAlignWorker.exe.",
            "Si se eliminó el archivo, reinstala completamente la aplicación.",
            "Reinicia Windows y vuelve a ejecutar la comprobación.",
        ]),
        "LST-DATA-001": ("La aplicación no puede guardar su configuración", [
            "Comprueba que tu cuenta de Windows pueda escribir en la carpeta AppData.",
            "Comprueba Controlled Folder Access y otros programas de seguridad.",
            "Vuelve a ejecutar la comprobación del sistema.",
        ]),
        "LST-AI-001": ("No se pudieron iniciar los modelos locales de traducción", [
            "Actualiza el controlador NVIDIA y reinicia Windows.",
            "Cierra otras aplicaciones de IA y programas que utilicen intensamente la GPU.",
            "Si faltan modelos, reinstala completamente la aplicación.",
        ]),
        "LST-GEN-001": ("La comprobación del sistema encontró un problema", [
            "Reinicia Windows y vuelve a ejecutar la comprobación.",
            "Busca en Internet el texto exacto del error mostrado en los detalles técnicos.",
            "Si faltan archivos, reinstala completamente la aplicación.",
        ]),
    },
}

# es-US uses the same troubleshooting instructions.
HELP_TRANSLATIONS_EXTRA["es-US"] = HELP_TRANSLATIONS_EXTRA["es-ES"]


# Portuguese variants share the same technical troubleshooting flow.
_pt = {
    "LST-SYS-001": ("Configuração do Windows não suportada", [
        "Use uma versão de 64 bits do Windows 10 ou Windows 11.",
        "Instale todas as atualizações disponíveis do Windows.",
        "Reinicie o Windows e execute novamente a Verificação do sistema.",
    ]),
    "LST-GPU-001": ("A GPU NVIDIA ou o driver não foi detectado", [
        "Verifique no Gestor/Gerenciador de Dispositivos se a GPU NVIDIA aparece sem erros.",
        "Instale ou reinstale o driver oficial da NVIDIA.",
        "Reinicie o Windows e execute novamente a verificação.",
    ]),
    "LST-GPU-002": ("O driver NVIDIA é demasiado antigo", [
        "Instale o driver NVIDIA mais recente para a sua GPU.",
        "Reinicie o Windows depois da instalação.",
        "Execute novamente a Verificação do sistema.",
    ]),
    "LST-GPU-003": ("A GPU NVIDIA não é compatível", [
        "Esta GPU não consegue executar o ambiente CUDA/Paddle necessário.",
        "Use uma GPU NVIDIA compatível mais recente.",
        "Não instale o CUDA Toolkit manualmente; a aplicação inclui o runtime necessário.",
    ]),
    "LST-GPU-004": ("Memória de vídeo insuficiente", [
        "Feche jogos, navegadores e outros programas que utilizem intensamente a GPU.",
        "Execute novamente a verificação e consulte a VRAM livre.",
        "Se a tradução continuar a falhar, use uma GPU com mais VRAM.",
    ]),
    "LST-GPU-010": ("Foram detetadas várias GPUs NVIDIA", [
        "A versão atual utiliza a NVIDIA GPU 0.",
        "Consulte os detalhes técnicos para ver qual placa aparece como gpu:0.",
        "Se estiver a ser usada a GPU errada, altere a configuração de GPU no Windows/NVIDIA.",
    ]),
    "LST-CAP-001": ("Não foi possível capturar corretamente o ecrã/tela", [
        "Certifique-se de que o monitor pretendido está ligado à GPU NVIDIA.",
        "Experimente o modo Borderless Windowed / Janela sem bordas.",
        "Reinicie o Local Screen Translator e execute novamente a verificação.",
    ]),
    "LST-NET-001": ("A porta local 11435 já está a ser utilizada", [
        "Feche outras aplicações locais de IA e instâncias do Ollama.",
        "Reinicie o Local Screen Translator.",
        "Se continuar, reinicie o Windows e abra primeiro o Local Screen Translator.",
    ]),
    "LST-TTS-001": ("Não foi encontrada uma voz inglesa Microsoft utilizável", [
        "Abra as configurações do Local Screen Translator.",
        "Selecione e instale um pacote de voz inglesa Microsoft.",
        "Reinicie o Windows se necessário.",
    ]),
    "LST-CUDA-001": ("Não foi possível iniciar o OCR por GPU", [
        "Atualize ou reinstale o driver NVIDIA.",
        "Reinicie o Windows e feche aplicações que utilizem intensamente a GPU.",
        "Não instale Python, PaddlePaddle ou CUDA Toolkit manualmente.",
    ]),
    "LST-FILE-001": ("Falta um ficheiro/arquivo necessário da aplicação", [
        "Não descarregue modelos ou DLLs individuais manualmente.",
        "Verifique o histórico de proteção do Windows Security.",
        "Reinstale a aplicação completa com Setup.exe e todos os ficheiros .bin juntos.",
    ]),
    "LST-ALIGN-001": ("Não foi possível iniciar o componente de alinhamento de texto", [
        "Verifique se o Windows Security bloqueou LSTAlignWorker.exe.",
        "Se o ficheiro foi removido, reinstale completamente a aplicação.",
        "Reinicie o Windows e execute novamente a verificação.",
    ]),
    "LST-DATA-001": ("A aplicação não consegue guardar as configurações", [
        "Verifique se a sua conta Windows pode escrever na pasta AppData.",
        "Verifique Controlled Folder Access e outros programas de segurança.",
        "Execute novamente a Verificação do sistema.",
    ]),
    "LST-AI-001": ("Não foi possível iniciar os modelos locais de tradução", [
        "Atualize o driver NVIDIA e reinicie o Windows.",
        "Feche outras aplicações de IA e programas que utilizem intensamente a GPU.",
        "Se faltarem modelos, reinstale completamente a aplicação.",
    ]),
    "LST-GEN-001": ("A Verificação do sistema encontrou um problema", [
        "Reinicie o Windows e execute novamente a verificação.",
        "Pesquise na Internet o texto exato do erro apresentado nos detalhes técnicos.",
        "Se faltarem ficheiros, reinstale completamente a aplicação.",
    ]),
}

HELP_TRANSLATIONS_EXTRA["pt-PT"] = _pt
HELP_TRANSLATIONS_EXTRA["pt-BR"] = _pt


HELP_TRANSLATIONS_EXTRA["pl"] = {
    "LST-SYS-001": ("Nieobsługiwana konfiguracja Windows", [
        "Użyj 64-bitowej wersji Windows 10 lub Windows 11.",
        "Zainstaluj wszystkie dostępne aktualizacje Windows.",
        "Uruchom ponownie Windows i ponownie wykonaj sprawdzanie systemu.",
    ]),
    "LST-GPU-001": ("Nie wykryto GPU NVIDIA lub sterownika", [
        "Sprawdź w Menedżerze urządzeń, czy GPU NVIDIA jest wykrywane bez błędów.",
        "Zainstaluj lub przeinstaluj oficjalny sterownik NVIDIA.",
        "Uruchom ponownie Windows i ponownie wykonaj sprawdzanie.",
    ]),
    "LST-GPU-002": ("Sterownik NVIDIA jest zbyt stary", [
        "Zainstaluj najnowszy sterownik NVIDIA dla swojej karty graficznej.",
        "Po instalacji uruchom ponownie Windows.",
        "Ponownie wykonaj sprawdzanie systemu.",
    ]),
    "LST-GPU-003": ("GPU NVIDIA nie jest zgodne", [
        "Ta karta nie obsługuje wymaganego środowiska CUDA/Paddle.",
        "Użyj nowszego zgodnego GPU NVIDIA.",
        "Nie instaluj CUDA Toolkit ręcznie; aplikacja zawiera wymagane środowisko.",
    ]),
    "LST-GPU-004": ("Za mało pamięci VRAM", [
        "Zamknij gry, przeglądarki i inne programy intensywnie korzystające z GPU.",
        "Ponownie wykonaj sprawdzanie i sprawdź wolną pamięć VRAM.",
        "Jeśli tłumaczenie nadal nie działa, użyj GPU z większą ilością VRAM.",
    ]),
    "LST-GPU-010": ("Wykryto wiele GPU NVIDIA", [
        "Bieżąca wersja używa NVIDIA GPU 0.",
        "Sprawdź w szczegółach technicznych, która karta jest oznaczona jako gpu:0.",
        "Jeśli używane jest niewłaściwe GPU, zmień konfigurację GPU w Windows/NVIDIA.",
    ]),
    "LST-CAP-001": ("Nie udało się poprawnie przechwycić ekranu", [
        "Upewnij się, że właściwy monitor jest podłączony do GPU NVIDIA.",
        "Spróbuj trybu Borderless Windowed / okna bez ramek.",
        "Uruchom ponownie Local Screen Translator i ponownie wykonaj sprawdzanie.",
    ]),
    "LST-NET-001": ("Lokalny port 11435 jest już używany", [
        "Zamknij inne lokalne aplikacje AI i instancje Ollama.",
        "Uruchom ponownie Local Screen Translator.",
        "Jeśli problem pozostaje, uruchom ponownie Windows i najpierw otwórz Local Screen Translator.",
    ]),
    "LST-TTS-001": ("Nie znaleziono odpowiedniego angielskiego głosu Microsoft", [
        "Otwórz ustawienia Local Screen Translator.",
        "Wybierz i zainstaluj angielski pakiet głosowy Microsoft.",
        "Jeśli będzie to wymagane, uruchom ponownie Windows.",
    ]),
    "LST-CUDA-001": ("Nie udało się uruchomić OCR na GPU", [
        "Zaktualizuj lub przeinstaluj sterownik NVIDIA.",
        "Uruchom ponownie Windows i zamknij programy intensywnie używające GPU.",
        "Nie instaluj ręcznie Python, PaddlePaddle ani CUDA Toolkit.",
    ]),
    "LST-FILE-001": ("Brakuje wymaganego pliku aplikacji", [
        "Nie pobieraj ręcznie pojedynczych modeli ani bibliotek DLL.",
        "Sprawdź Historię ochrony w Zabezpieczeniach Windows.",
        "Zainstaluj ponownie pełną aplikację z Setup.exe i wszystkimi plikami .bin w tym samym folderze.",
    ]),
    "LST-ALIGN-001": ("Nie udało się uruchomić komponentu wyrównywania tekstu", [
        "Sprawdź, czy Zabezpieczenia Windows nie zablokowały LSTAlignWorker.exe.",
        "Jeśli plik został usunięty, zainstaluj ponownie całą aplikację.",
        "Uruchom ponownie Windows i ponownie wykonaj sprawdzanie.",
    ]),
    "LST-DATA-001": ("Aplikacja nie może zapisać ustawień", [
        "Sprawdź, czy konto Windows może zapisywać dane w folderze AppData.",
        "Sprawdź Controlled Folder Access i inne oprogramowanie zabezpieczające.",
        "Ponownie wykonaj sprawdzanie systemu.",
    ]),
    "LST-AI-001": ("Nie udało się uruchomić lokalnych modeli tłumaczenia", [
        "Zaktualizuj sterownik NVIDIA i uruchom ponownie Windows.",
        "Zamknij inne aplikacje AI i programy intensywnie używające GPU.",
        "Jeśli brakuje modeli, zainstaluj ponownie całą aplikację.",
    ]),
    "LST-GEN-001": ("Sprawdzanie systemu wykryło problem", [
        "Uruchom ponownie Windows i ponownie wykonaj sprawdzanie.",
        "Wyszukaj w Internecie dokładny tekst błędu ze szczegółów technicznych.",
        "Jeśli brakuje plików, zainstaluj ponownie całą aplikację.",
    ]),
}



# SELF HELP LANGUAGE BATCH 2A

HELP_TRANSLATIONS_EXTRA["uk"] = {
    "LST-SYS-001": ("Непідтримувана конфігурація Windows", [
        "Використовуйте 64-бітну версію Windows 10 або Windows 11.",
        "Установіть усі доступні оновлення Windows.",
        "Перезавантажте Windows і знову запустіть Перевірку системи.",
    ]),
    "LST-GPU-001": ("Не вдалося виявити NVIDIA GPU або драйвер", [
        "Відкрийте Диспетчер пристроїв і переконайтеся, що відеокарта NVIDIA визначається без помилок.",
        "Установіть або перевстановіть офіційний драйвер NVIDIA.",
        "Перезавантажте Windows і знову запустіть перевірку.",
    ]),
    "LST-GPU-002": ("Драйвер NVIDIA занадто старий", [
        "Установіть найновіший драйвер NVIDIA для вашої відеокарти.",
        "Після встановлення перезавантажте Windows.",
        "Знову запустіть Перевірку системи.",
    ]),
    "LST-GPU-003": ("Відеокарта NVIDIA несумісна", [
        "Ця відеокарта не підтримує необхідне середовище CUDA/Paddle.",
        "Використовуйте новішу сумісну відеокарту NVIDIA.",
        "Не встановлюйте CUDA Toolkit вручну — програма містить необхідне середовище.",
    ]),
    "LST-GPU-004": ("Недостатньо відеопам’яті", [
        "Закрийте ігри, браузери та інші програми, які активно використовують GPU.",
        "Знову запустіть перевірку та перевірте обсяг вільної VRAM.",
        "Якщо переклад усе ще не працює, використовуйте GPU з більшим обсягом VRAM.",
    ]),
    "LST-GPU-010": ("Виявлено кілька відеокарт NVIDIA", [
        "Поточна версія використовує NVIDIA GPU 0.",
        "У технічних даних перевірте, яка відеокарта вказана як gpu:0.",
        "Якщо використовується неправильний GPU, змініть конфігурацію GPU у Windows/NVIDIA.",
    ]),
    "LST-CAP-001": ("Не вдалося правильно захопити екран", [
        "Переконайтеся, що потрібний монітор підключений до відеокарти NVIDIA.",
        "Спробуйте режим Borderless Windowed / Безрамкове вікно.",
        "Перезапустіть Local Screen Translator і знову виконайте перевірку.",
    ]),
    "LST-NET-001": ("Локальний порт 11435 уже використовується", [
        "Закрийте інші локальні AI-програми та запущені екземпляри Ollama.",
        "Перезапустіть Local Screen Translator.",
        "Якщо проблема залишається, перезавантажте Windows і спочатку запустіть Local Screen Translator.",
    ]),
    "LST-TTS-001": ("Не знайдено придатного англійського голосу Microsoft", [
        "Відкрийте налаштування Local Screen Translator.",
        "Виберіть і встановіть англійський голосовий пакет Microsoft.",
        "Якщо буде потрібно, перезавантажте Windows.",
    ]),
    "LST-CUDA-001": ("Не вдалося запустити GPU OCR", [
        "Оновіть або перевстановіть драйвер NVIDIA.",
        "Перезавантажте Windows і закрийте програми, які активно використовують GPU.",
        "Не встановлюйте Python, PaddlePaddle або CUDA Toolkit вручну.",
    ]),
    "LST-FILE-001": ("Відсутній необхідний файл програми", [
        "Не завантажуйте окремі моделі або DLL вручну.",
        "Перевірте журнал захисту Windows Security — файл міг потрапити в карантин.",
        "Повністю перевстановіть програму, розмістивши Setup.exe та всі файли .bin поруч.",
    ]),
    "LST-ALIGN-001": ("Не вдалося запустити компонент вирівнювання тексту", [
        "Перевірте, чи Windows Security не заблокував LSTAlignWorker.exe.",
        "Якщо файл було видалено, повністю перевстановіть програму.",
        "Перезавантажте Windows і знову виконайте перевірку.",
    ]),
    "LST-DATA-001": ("Програма не може зберегти налаштування", [
        "Переконайтеся, що ваш обліковий запис Windows має право запису до папки AppData.",
        "Перевірте Controlled Folder Access та інше захисне ПЗ.",
        "Знову запустіть Перевірку системи.",
    ]),
    "LST-AI-001": ("Не вдалося запустити локальні моделі перекладу", [
        "Оновіть драйвер NVIDIA та перезавантажте Windows.",
        "Закрийте інші AI-програми та програми, які активно використовують GPU.",
        "Якщо моделі відсутні, повністю перевстановіть програму.",
    ]),
    "LST-GEN-001": ("Перевірка системи виявила проблему", [
        "Перезавантажте Windows і знову виконайте перевірку.",
        "Шукайте в Інтернеті точний текст помилки з технічних даних.",
        "Якщо файли відсутні, повністю перевстановіть програму.",
    ]),
}


HELP_TRANSLATIONS_EXTRA["cs"] = {
    "LST-SYS-001": ("Nepodporovaná konfigurace Windows", [
        "Používejte 64bitovou verzi Windows 10 nebo Windows 11.",
        "Nainstalujte všechny dostupné aktualizace Windows.",
        "Restartujte Windows a znovu spusťte kontrolu systému.",
    ]),
    "LST-GPU-001": ("GPU NVIDIA nebo ovladač nebyl nalezen", [
        "Ve Správci zařízení ověřte, že je GPU NVIDIA rozpoznáno bez chyb.",
        "Nainstalujte nebo přeinstalujte oficiální ovladač NVIDIA.",
        "Restartujte Windows a znovu spusťte kontrolu.",
    ]),
    "LST-GPU-002": ("Ovladač NVIDIA je příliš starý", [
        "Nainstalujte nejnovější ovladač NVIDIA pro svou grafickou kartu.",
        "Po instalaci restartujte Windows.",
        "Znovu spusťte kontrolu systému.",
    ]),
    "LST-GPU-003": ("GPU NVIDIA není kompatibilní", [
        "Toto GPU nepodporuje požadované prostředí CUDA/Paddle.",
        "Použijte novější kompatibilní GPU NVIDIA.",
        "Neinstalujte CUDA Toolkit ručně; aplikace obsahuje potřebné prostředí.",
    ]),
    "LST-GPU-004": ("Nedostatek grafické paměti", [
        "Ukončete hry, prohlížeče a další programy intenzivně využívající GPU.",
        "Znovu spusťte kontrolu a zkontrolujte volnou VRAM.",
        "Pokud překlad stále nefunguje, použijte GPU s větší VRAM.",
    ]),
    "LST-GPU-010": ("Bylo zjištěno více GPU NVIDIA", [
        "Aktuální verze používá NVIDIA GPU 0.",
        "V technických podrobnostech zjistěte, která karta je označena jako gpu:0.",
        "Pokud se používá nesprávné GPU, změňte konfiguraci GPU ve Windows/NVIDIA.",
    ]),
    "LST-CAP-001": ("Obrazovku se nepodařilo správně zachytit", [
        "Ujistěte se, že požadovaný monitor je připojen k GPU NVIDIA.",
        "Vyzkoušejte režim Borderless Windowed / okno bez okrajů.",
        "Restartujte Local Screen Translator a znovu spusťte kontrolu.",
    ]),
    "LST-NET-001": ("Místní port 11435 je již používán", [
        "Ukončete ostatní místní AI aplikace a instance Ollama.",
        "Restartujte Local Screen Translator.",
        "Pokud problém přetrvává, restartujte Windows a spusťte nejprve Local Screen Translator.",
    ]),
    "LST-TTS-001": ("Nebyl nalezen použitelný anglický hlas Microsoft", [
        "Otevřete nastavení Local Screen Translator.",
        "Vyberte a nainstalujte anglický hlasový balíček Microsoft.",
        "Pokud je to vyžadováno, restartujte Windows.",
    ]),
    "LST-CUDA-001": ("GPU OCR se nepodařilo spustit", [
        "Aktualizujte nebo přeinstalujte ovladač NVIDIA.",
        "Restartujte Windows a ukončete programy intenzivně využívající GPU.",
        "Neinstalujte ručně Python, PaddlePaddle ani CUDA Toolkit.",
    ]),
    "LST-FILE-001": ("Chybí požadovaný soubor aplikace", [
        "Nestahujte ručně jednotlivé modely ani DLL.",
        "Zkontrolujte historii ochrany Zabezpečení Windows.",
        "Přeinstalujte celou aplikaci s Setup.exe a všemi soubory .bin ve stejné složce.",
    ]),
    "LST-ALIGN-001": ("Komponentu zarovnání textu se nepodařilo spustit", [
        "Ověřte, zda Zabezpečení Windows nezablokovalo LSTAlignWorker.exe.",
        "Pokud byl soubor odstraněn, aplikaci kompletně přeinstalujte.",
        "Restartujte Windows a spusťte kontrolu znovu.",
    ]),
    "LST-DATA-001": ("Aplikace nemůže uložit nastavení", [
        "Ověřte, že váš účet Windows může zapisovat do složky AppData.",
        "Zkontrolujte Controlled Folder Access a další bezpečnostní software.",
        "Spusťte kontrolu systému znovu.",
    ]),
    "LST-AI-001": ("Místní překladové modely se nepodařilo spustit", [
        "Aktualizujte ovladač NVIDIA a restartujte Windows.",
        "Ukončete ostatní AI aplikace a programy intenzivně využívající GPU.",
        "Pokud modely chybí, kompletně přeinstalujte aplikaci.",
    ]),
    "LST-GEN-001": ("Kontrola systému zjistila problém", [
        "Restartujte Windows a spusťte kontrolu znovu.",
        "Vyhledejte na Internetu přesný text chyby z technických podrobností.",
        "Pokud chybí soubory, aplikaci kompletně přeinstalujte.",
    ]),
}


HELP_TRANSLATIONS_EXTRA["sk"] = {
    "LST-SYS-001": ("Nepodporovaná konfigurácia Windows", [
        "Používajte 64-bitovú verziu Windows 10 alebo Windows 11.",
        "Nainštalujte všetky dostupné aktualizácie Windows.",
        "Reštartujte Windows a znova spustite kontrolu systému.",
    ]),
    "LST-GPU-001": ("GPU NVIDIA alebo ovládač nebol nájdený", [
        "V Správcovi zariadení overte, že GPU NVIDIA je rozpoznané bez chýb.",
        "Nainštalujte alebo preinštalujte oficiálny ovládač NVIDIA.",
        "Reštartujte Windows a znova spustite kontrolu.",
    ]),
    "LST-GPU-002": ("Ovládač NVIDIA je príliš starý", [
        "Nainštalujte najnovší ovládač NVIDIA pre svoju grafickú kartu.",
        "Po inštalácii reštartujte Windows.",
        "Znova spustite kontrolu systému.",
    ]),
    "LST-GPU-003": ("GPU NVIDIA nie je kompatibilné", [
        "Toto GPU nepodporuje požadované prostredie CUDA/Paddle.",
        "Použite novšie kompatibilné GPU NVIDIA.",
        "Neinštalujte CUDA Toolkit ručne; aplikácia obsahuje potrebné prostredie.",
    ]),
    "LST-GPU-004": ("Nedostatok grafickej pamäte", [
        "Zatvorte hry, prehliadače a ďalšie programy intenzívne využívajúce GPU.",
        "Znova spustite kontrolu a skontrolujte voľnú VRAM.",
        "Ak preklad stále nefunguje, použite GPU s väčšou VRAM.",
    ]),
    "LST-GPU-010": ("Bolo zistených viac GPU NVIDIA", [
        "Aktuálna verzia používa NVIDIA GPU 0.",
        "V technických podrobnostiach zistite, ktorá karta je označená ako gpu:0.",
        "Ak sa používa nesprávne GPU, zmeňte konfiguráciu GPU vo Windows/NVIDIA.",
    ]),
    "LST-CAP-001": ("Obrazovku sa nepodarilo správne zachytiť", [
        "Uistite sa, že požadovaný monitor je pripojený ku GPU NVIDIA.",
        "Vyskúšajte režim Borderless Windowed / okno bez okrajov.",
        "Reštartujte Local Screen Translator a znova spustite kontrolu.",
    ]),
    "LST-NET-001": ("Lokálny port 11435 sa už používa", [
        "Zatvorte ostatné lokálne AI aplikácie a inštancie Ollama.",
        "Reštartujte Local Screen Translator.",
        "Ak problém pretrváva, reštartujte Windows a najprv spustite Local Screen Translator.",
    ]),
    "LST-TTS-001": ("Nenašiel sa použiteľný anglický hlas Microsoft", [
        "Otvorte nastavenia Local Screen Translator.",
        "Vyberte a nainštalujte anglický hlasový balík Microsoft.",
        "Ak je to potrebné, reštartujte Windows.",
    ]),
    "LST-CUDA-001": ("GPU OCR sa nepodarilo spustiť", [
        "Aktualizujte alebo preinštalujte ovládač NVIDIA.",
        "Reštartujte Windows a zatvorte programy intenzívne využívajúce GPU.",
        "Neinštalujte ručne Python, PaddlePaddle ani CUDA Toolkit.",
    ]),
    "LST-FILE-001": ("Chýba požadovaný súbor aplikácie", [
        "Nesťahujte ručne jednotlivé modely ani DLL.",
        "Skontrolujte históriu ochrany Zabezpečenia Windows.",
        "Preinštalujte celú aplikáciu so Setup.exe a všetkými súbormi .bin v rovnakom priečinku.",
    ]),
    "LST-ALIGN-001": ("Komponent zarovnania textu sa nepodarilo spustiť", [
        "Overte, či Zabezpečenie Windows nezablokovalo LSTAlignWorker.exe.",
        "Ak bol súbor odstránený, aplikáciu kompletne preinštalujte.",
        "Reštartujte Windows a spustite kontrolu znova.",
    ]),
    "LST-DATA-001": ("Aplikácia nemôže uložiť nastavenia", [
        "Overte, že váš účet Windows môže zapisovať do priečinka AppData.",
        "Skontrolujte Controlled Folder Access a ďalší bezpečnostný softvér.",
        "Spustite kontrolu systému znova.",
    ]),
    "LST-AI-001": ("Lokálne prekladové modely sa nepodarilo spustiť", [
        "Aktualizujte ovládač NVIDIA a reštartujte Windows.",
        "Zatvorte ostatné AI aplikácie a programy intenzívne využívajúce GPU.",
        "Ak modely chýbajú, kompletne preinštalujte aplikáciu.",
    ]),
    "LST-GEN-001": ("Kontrola systému zistila problém", [
        "Reštartujte Windows a spustite kontrolu znova.",
        "Vyhľadajte na internete presný text chyby z technických podrobností.",
        "Ak chýbajú súbory, aplikáciu kompletne preinštalujte.",
    ]),
}


HELP_TRANSLATIONS_EXTRA["nl"] = {
    "LST-SYS-001": ("Niet-ondersteunde Windows-configuratie", [
        "Gebruik een 64-bits versie van Windows 10 of Windows 11.",
        "Installeer alle beschikbare Windows-updates.",
        "Start Windows opnieuw en voer de systeemcontrole opnieuw uit.",
    ]),
    "LST-GPU-001": ("NVIDIA-GPU of stuurprogramma niet gevonden", [
        "Controleer in Apparaatbeheer of de NVIDIA-GPU zonder fouten wordt weergegeven.",
        "Installeer of herinstalleer het officiële NVIDIA-stuurprogramma.",
        "Start Windows opnieuw en voer de controle opnieuw uit.",
    ]),
    "LST-GPU-002": ("Het NVIDIA-stuurprogramma is te oud", [
        "Installeer het nieuwste NVIDIA-stuurprogramma voor uw grafische kaart.",
        "Start Windows daarna opnieuw.",
        "Voer de systeemcontrole opnieuw uit.",
    ]),
    "LST-GPU-003": ("De NVIDIA-GPU is niet compatibel", [
        "Deze GPU ondersteunt de vereiste CUDA/Paddle-omgeving niet.",
        "Gebruik een nieuwere compatibele NVIDIA-GPU.",
        "Installeer CUDA Toolkit niet handmatig; de toepassing bevat de benodigde runtime.",
    ]),
    "LST-GPU-004": ("Onvoldoende videogeheugen", [
        "Sluit games, browsers en andere programma's die de GPU zwaar belasten.",
        "Voer de controle opnieuw uit en controleer de vrije VRAM.",
        "Gebruik een GPU met meer VRAM als vertalen nog steeds niet werkt.",
    ]),
    "LST-GPU-010": ("Meerdere NVIDIA-GPU's gedetecteerd", [
        "De huidige versie gebruikt NVIDIA GPU 0.",
        "Controleer in de technische details welke kaart als gpu:0 wordt weergegeven.",
        "Wijzig de GPU-configuratie in Windows/NVIDIA als de verkeerde GPU wordt gebruikt.",
    ]),
    "LST-CAP-001": ("Het scherm kon niet correct worden vastgelegd", [
        "Controleer of de gewenste monitor op de NVIDIA-GPU is aangesloten.",
        "Probeer de modus Borderless Windowed / venster zonder randen.",
        "Start Local Screen Translator opnieuw en voer de controle opnieuw uit.",
    ]),
    "LST-NET-001": ("Lokale poort 11435 is al in gebruik", [
        "Sluit andere lokale AI-programma's en Ollama-instanties.",
        "Start Local Screen Translator opnieuw.",
        "Als het probleem blijft bestaan, start Windows opnieuw en open Local Screen Translator als eerste.",
    ]),
    "LST-TTS-001": ("Geen bruikbare Engelse Microsoft-stem gevonden", [
        "Open de instellingen van Local Screen Translator.",
        "Selecteer en installeer een Engels Microsoft-spraakpakket.",
        "Start Windows opnieuw als dit wordt gevraagd.",
    ]),
    "LST-CUDA-001": ("GPU-OCR kon niet worden gestart", [
        "Werk het NVIDIA-stuurprogramma bij of installeer het opnieuw.",
        "Start Windows opnieuw en sluit programma's die de GPU zwaar belasten.",
        "Installeer Python, PaddlePaddle of CUDA Toolkit niet handmatig.",
    ]),
    "LST-FILE-001": ("Een vereist toepassingsbestand ontbreekt", [
        "Download afzonderlijke modellen of DLL-bestanden niet handmatig.",
        "Controleer de beveiligingsgeschiedenis van Windows-beveiliging.",
        "Installeer de volledige toepassing opnieuw met Setup.exe en alle .bin-bestanden in dezelfde map.",
    ]),
    "LST-ALIGN-001": ("De tekstuitlijningscomponent kon niet worden gestart", [
        "Controleer of Windows-beveiliging LSTAlignWorker.exe heeft geblokkeerd.",
        "Installeer de toepassing volledig opnieuw als het bestand is verwijderd.",
        "Start Windows opnieuw en voer de controle opnieuw uit.",
    ]),
    "LST-DATA-001": ("De toepassing kan instellingen niet opslaan", [
        "Controleer of uw Windows-account naar de map AppData kan schrijven.",
        "Controleer Controlled Folder Access en andere beveiligingssoftware.",
        "Voer de systeemcontrole opnieuw uit.",
    ]),
    "LST-AI-001": ("De lokale vertaalmodellen konden niet worden gestart", [
        "Werk het NVIDIA-stuurprogramma bij en start Windows opnieuw.",
        "Sluit andere AI-programma's en toepassingen die de GPU zwaar belasten.",
        "Installeer de toepassing volledig opnieuw als modellen ontbreken.",
    ]),
    "LST-GEN-001": ("De systeemcontrole heeft een probleem gevonden", [
        "Start Windows opnieuw en voer de controle opnieuw uit.",
        "Zoek op Internet naar de exacte fouttekst uit de technische details.",
        "Installeer de toepassing volledig opnieuw als bestanden ontbreken.",
    ]),
}



# SELF HELP LANGUAGE BATCH 2B

HELP_TRANSLATIONS_EXTRA["da"] = {
    "LST-SYS-001": ("Ikke-understøttet Windows-konfiguration", [
        "Brug en 64-bit version af Windows 10 eller Windows 11.",
        "Installer alle tilgængelige Windows-opdateringer.",
        "Genstart Windows, og kør systemkontrollen igen.",
    ]),
    "LST-GPU-001": ("NVIDIA-GPU eller driver blev ikke fundet", [
        "Kontroller i Enhedshåndtering, at NVIDIA-GPU'en vises uden fejl.",
        "Installer eller geninstaller den officielle NVIDIA-driver.",
        "Genstart Windows, og kør kontrollen igen.",
    ]),
    "LST-GPU-002": ("NVIDIA-driveren er for gammel", [
        "Installer den nyeste NVIDIA-driver til dit grafikkort.",
        "Genstart Windows efter installationen.",
        "Kør systemkontrollen igen.",
    ]),
    "LST-GPU-003": ("NVIDIA-GPU'en er ikke kompatibel", [
        "Denne GPU understøtter ikke det krævede CUDA/Paddle-miljø.",
        "Brug en nyere kompatibel NVIDIA-GPU.",
        "Installer ikke CUDA Toolkit manuelt; programmet indeholder den nødvendige runtime.",
    ]),
    "LST-GPU-004": ("Utilstrækkelig grafikhukommelse", [
        "Luk spil, browsere og andre programmer, der bruger GPU'en meget.",
        "Kør kontrollen igen, og kontroller den ledige VRAM.",
        "Brug en GPU med mere VRAM, hvis oversættelsen stadig ikke virker.",
    ]),
    "LST-GPU-010": ("Flere NVIDIA-GPU'er blev fundet", [
        "Den aktuelle version bruger NVIDIA GPU 0.",
        "Se i de tekniske detaljer, hvilket kort der vises som gpu:0.",
        "Skift GPU-konfigurationen i Windows/NVIDIA, hvis den forkerte GPU bruges.",
    ]),
    "LST-CAP-001": ("Skærmen kunne ikke optages korrekt", [
        "Kontroller, at den ønskede skærm er tilsluttet NVIDIA-GPU'en.",
        "Prøv Borderless Windowed / vindue uden ramme.",
        "Genstart Local Screen Translator, og kør kontrollen igen.",
    ]),
    "LST-NET-001": ("Den lokale port 11435 er allerede i brug", [
        "Luk andre lokale AI-programmer og Ollama-instanser.",
        "Genstart Local Screen Translator.",
        "Hvis problemet fortsætter, genstart Windows og åbn Local Screen Translator først.",
    ]),
    "LST-TTS-001": ("Ingen brugbar engelsk Microsoft-stemme blev fundet", [
        "Åbn indstillingerne i Local Screen Translator.",
        "Vælg og installer en engelsk Microsoft-stemmepakke.",
        "Genstart Windows, hvis det er nødvendigt.",
    ]),
    "LST-CUDA-001": ("GPU-OCR kunne ikke startes", [
        "Opdater eller geninstaller NVIDIA-driveren.",
        "Genstart Windows, og luk programmer, der bruger GPU'en meget.",
        "Installer ikke Python, PaddlePaddle eller CUDA Toolkit manuelt.",
    ]),
    "LST-FILE-001": ("En nødvendig programfil mangler", [
        "Download ikke enkelte modeller eller DLL-filer manuelt.",
        "Kontroller beskyttelseshistorikken i Windows Sikkerhed.",
        "Geninstaller hele programmet med Setup.exe og alle .bin-filer i samme mappe.",
    ]),
    "LST-ALIGN-001": ("Tekstjusteringskomponenten kunne ikke startes", [
        "Kontroller, om Windows Sikkerhed har blokeret LSTAlignWorker.exe.",
        "Geninstaller hele programmet, hvis filen blev fjernet.",
        "Genstart Windows, og kør kontrollen igen.",
    ]),
    "LST-DATA-001": ("Programmet kan ikke gemme indstillinger", [
        "Kontroller, at din Windows-konto kan skrive til AppData-mappen.",
        "Kontroller Controlled Folder Access og anden sikkerhedssoftware.",
        "Kør systemkontrollen igen.",
    ]),
    "LST-AI-001": ("De lokale oversættelsesmodeller kunne ikke startes", [
        "Opdater NVIDIA-driveren, og genstart Windows.",
        "Luk andre AI-programmer og programmer, der bruger GPU'en meget.",
        "Geninstaller hele programmet, hvis modeller mangler.",
    ]),
    "LST-GEN-001": ("Systemkontrollen fandt et problem", [
        "Genstart Windows, og kør kontrollen igen.",
        "Søg på internettet efter den nøjagtige fejltekst fra de tekniske detaljer.",
        "Geninstaller hele programmet, hvis filer mangler.",
    ]),
}


HELP_TRANSLATIONS_EXTRA["fi"] = {
    "LST-SYS-001": ("Windows-kokoonpanoa ei tueta", [
        "Käytä Windows 10:n tai Windows 11:n 64-bittistä versiota.",
        "Asenna kaikki saatavilla olevat Windows-päivitykset.",
        "Käynnistä Windows uudelleen ja suorita järjestelmän tarkistus uudelleen.",
    ]),
    "LST-GPU-001": ("NVIDIA-GPU:ta tai ohjainta ei havaittu", [
        "Tarkista Laitehallinnasta, että NVIDIA-GPU näkyy ilman virheitä.",
        "Asenna tai asenna uudelleen virallinen NVIDIA-ohjain.",
        "Käynnistä Windows uudelleen ja suorita tarkistus uudelleen.",
    ]),
    "LST-GPU-002": ("NVIDIA-ohjain on liian vanha", [
        "Asenna näytönohjaimellesi uusin NVIDIA-ohjain.",
        "Käynnistä Windows uudelleen asennuksen jälkeen.",
        "Suorita järjestelmän tarkistus uudelleen.",
    ]),
    "LST-GPU-003": ("NVIDIA-GPU ei ole yhteensopiva", [
        "Tämä GPU ei tue vaadittua CUDA/Paddle-ympäristöä.",
        "Käytä uudempaa yhteensopivaa NVIDIA-GPU:ta.",
        "Älä asenna CUDA Toolkitia käsin; sovellus sisältää tarvittavan runtimen.",
    ]),
    "LST-GPU-004": ("Näytönohjaimen muistia ei ole riittävästi", [
        "Sulje pelit, selaimet ja muut GPU:ta voimakkaasti käyttävät ohjelmat.",
        "Suorita tarkistus uudelleen ja tarkista vapaan VRAM-muistin määrä.",
        "Jos käännös ei vieläkään toimi, käytä GPU:ta, jossa on enemmän VRAM-muistia.",
    ]),
    "LST-GPU-010": ("Useita NVIDIA-GPU:ita havaittiin", [
        "Nykyinen versio käyttää NVIDIA GPU 0:aa.",
        "Tarkista teknisistä tiedoista, mikä kortti näkyy nimellä gpu:0.",
        "Muuta Windowsin/NVIDIAn GPU-asetuksia, jos käytössä on väärä GPU.",
    ]),
    "LST-CAP-001": ("Näyttöä ei voitu kaapata oikein", [
        "Varmista, että haluttu näyttö on liitetty NVIDIA-GPU:hun.",
        "Kokeile Borderless Windowed / reunatonta ikkunatilaa.",
        "Käynnistä Local Screen Translator uudelleen ja suorita tarkistus uudelleen.",
    ]),
    "LST-NET-001": ("Paikallinen portti 11435 on jo käytössä", [
        "Sulje muut paikalliset AI-ohjelmat ja Ollama-instanssit.",
        "Käynnistä Local Screen Translator uudelleen.",
        "Jos ongelma jatkuu, käynnistä Windows uudelleen ja avaa Local Screen Translator ensimmäisenä.",
    ]),
    "LST-TTS-001": ("Sopivaa englanninkielistä Microsoft-ääntä ei löytynyt", [
        "Avaa Local Screen Translatorin asetukset.",
        "Valitse ja asenna englanninkielinen Microsoft-äänipaketti.",
        "Käynnistä Windows uudelleen tarvittaessa.",
    ]),
    "LST-CUDA-001": ("GPU-OCR:ää ei voitu käynnistää", [
        "Päivitä tai asenna NVIDIA-ohjain uudelleen.",
        "Käynnistä Windows uudelleen ja sulje GPU:ta voimakkaasti käyttävät ohjelmat.",
        "Älä asenna Pythonia, PaddlePaddlea tai CUDA Toolkitia käsin.",
    ]),
    "LST-FILE-001": ("Tarvittava sovellustiedosto puuttuu", [
        "Älä lataa yksittäisiä malleja tai DLL-tiedostoja käsin.",
        "Tarkista Windowsin suojauksen suojaushistoria.",
        "Asenna koko sovellus uudelleen niin, että Setup.exe ja kaikki .bin-tiedostot ovat samassa kansiossa.",
    ]),
    "LST-ALIGN-001": ("Tekstin kohdistuskomponenttia ei voitu käynnistää", [
        "Tarkista, onko Windowsin suojaus estänyt LSTAlignWorker.exe-tiedoston.",
        "Jos tiedosto poistettiin, asenna koko sovellus uudelleen.",
        "Käynnistä Windows uudelleen ja suorita tarkistus uudelleen.",
    ]),
    "LST-DATA-001": ("Sovellus ei voi tallentaa asetuksia", [
        "Varmista, että Windows-tililläsi on kirjoitusoikeus AppData-kansioon.",
        "Tarkista Controlled Folder Access ja muut suojausohjelmat.",
        "Suorita järjestelmän tarkistus uudelleen.",
    ]),
    "LST-AI-001": ("Paikallisia käännösmalleja ei voitu käynnistää", [
        "Päivitä NVIDIA-ohjain ja käynnistä Windows uudelleen.",
        "Sulje muut AI-ohjelmat ja GPU:ta voimakkaasti käyttävät sovellukset.",
        "Jos malleja puuttuu, asenna koko sovellus uudelleen.",
    ]),
    "LST-GEN-001": ("Järjestelmän tarkistus löysi ongelman", [
        "Käynnistä Windows uudelleen ja suorita tarkistus uudelleen.",
        "Hae Internetistä teknisissä tiedoissa näkyvää tarkkaa virhetekstiä.",
        "Jos tiedostoja puuttuu, asenna koko sovellus uudelleen.",
    ]),
}


HELP_TRANSLATIONS_EXTRA["sv"] = {
    "LST-SYS-001": ("Windows-konfigurationen stöds inte", [
        "Använd en 64-bitarsversion av Windows 10 eller Windows 11.",
        "Installera alla tillgängliga Windows-uppdateringar.",
        "Starta om Windows och kör systemkontrollen igen.",
    ]),
    "LST-GPU-001": ("NVIDIA-GPU eller drivrutin kunde inte hittas", [
        "Kontrollera i Enhetshanteraren att NVIDIA-GPU:n visas utan fel.",
        "Installera eller installera om den officiella NVIDIA-drivrutinen.",
        "Starta om Windows och kör kontrollen igen.",
    ]),
    "LST-GPU-002": ("NVIDIA-drivrutinen är för gammal", [
        "Installera den senaste NVIDIA-drivrutinen för ditt grafikkort.",
        "Starta om Windows efter installationen.",
        "Kör systemkontrollen igen.",
    ]),
    "LST-GPU-003": ("NVIDIA-GPU:n är inte kompatibel", [
        "Den här GPU:n stöder inte den CUDA/Paddle-miljö som krävs.",
        "Använd en nyare kompatibel NVIDIA-GPU.",
        "Installera inte CUDA Toolkit manuellt; programmet innehåller den runtime som behövs.",
    ]),
    "LST-GPU-004": ("Otillräckligt grafikminne", [
        "Stäng spel, webbläsare och andra program som använder GPU:n mycket.",
        "Kör kontrollen igen och kontrollera mängden ledigt VRAM.",
        "Använd en GPU med mer VRAM om översättningen fortfarande inte fungerar.",
    ]),
    "LST-GPU-010": ("Flera NVIDIA-GPU:er upptäcktes", [
        "Den aktuella versionen använder NVIDIA GPU 0.",
        "Kontrollera i de tekniska detaljerna vilket kort som visas som gpu:0.",
        "Ändra GPU-konfigurationen i Windows/NVIDIA om fel GPU används.",
    ]),
    "LST-CAP-001": ("Skärmen kunde inte fångas korrekt", [
        "Kontrollera att rätt bildskärm är ansluten till NVIDIA-GPU:n.",
        "Prova Borderless Windowed / kantlöst fönster.",
        "Starta om Local Screen Translator och kör kontrollen igen.",
    ]),
    "LST-NET-001": ("Den lokala porten 11435 används redan", [
        "Stäng andra lokala AI-program och Ollama-instanser.",
        "Starta om Local Screen Translator.",
        "Om problemet kvarstår, starta om Windows och öppna Local Screen Translator först.",
    ]),
    "LST-TTS-001": ("Ingen användbar engelsk Microsoft-röst hittades", [
        "Öppna inställningarna i Local Screen Translator.",
        "Välj och installera ett engelskt Microsoft-röstpaket.",
        "Starta om Windows om det behövs.",
    ]),
    "LST-CUDA-001": ("GPU-OCR kunde inte startas", [
        "Uppdatera eller installera om NVIDIA-drivrutinen.",
        "Starta om Windows och stäng program som använder GPU:n mycket.",
        "Installera inte Python, PaddlePaddle eller CUDA Toolkit manuellt.",
    ]),
    "LST-FILE-001": ("En nödvändig programfil saknas", [
        "Ladda inte ned enskilda modeller eller DLL-filer manuellt.",
        "Kontrollera skyddshistoriken i Windows-säkerhet.",
        "Installera om hela programmet med Setup.exe och alla .bin-filer i samma mapp.",
    ]),
    "LST-ALIGN-001": ("Textjusteringskomponenten kunde inte startas", [
        "Kontrollera om Windows-säkerhet har blockerat LSTAlignWorker.exe.",
        "Installera om hela programmet om filen togs bort.",
        "Starta om Windows och kör kontrollen igen.",
    ]),
    "LST-DATA-001": ("Programmet kan inte spara inställningar", [
        "Kontrollera att ditt Windows-konto kan skriva till AppData-mappen.",
        "Kontrollera Controlled Folder Access och annan säkerhetsprogramvara.",
        "Kör systemkontrollen igen.",
    ]),
    "LST-AI-001": ("De lokala översättningsmodellerna kunde inte startas", [
        "Uppdatera NVIDIA-drivrutinen och starta om Windows.",
        "Stäng andra AI-program och program som använder GPU:n mycket.",
        "Installera om hela programmet om modeller saknas.",
    ]),
    "LST-GEN-001": ("Systemkontrollen hittade ett problem", [
        "Starta om Windows och kör kontrollen igen.",
        "Sök på Internet efter den exakta feltexten i de tekniska detaljerna.",
        "Installera om hela programmet om filer saknas.",
    ]),
}


HELP_TRANSLATIONS_EXTRA["no"] = {
    "LST-SYS-001": ("Windows-konfigurasjonen støttes ikke", [
        "Bruk en 64-biters versjon av Windows 10 eller Windows 11.",
        "Installer alle tilgjengelige Windows-oppdateringer.",
        "Start Windows på nytt og kjør systemkontrollen igjen.",
    ]),
    "LST-GPU-001": ("NVIDIA-GPU eller driver ble ikke funnet", [
        "Kontroller i Enhetsbehandling at NVIDIA-GPU-en vises uten feil.",
        "Installer eller installer den offisielle NVIDIA-driveren på nytt.",
        "Start Windows på nytt og kjør kontrollen igjen.",
    ]),
    "LST-GPU-002": ("NVIDIA-driveren er for gammel", [
        "Installer den nyeste NVIDIA-driveren for grafikkortet ditt.",
        "Start Windows på nytt etter installasjonen.",
        "Kjør systemkontrollen igjen.",
    ]),
    "LST-GPU-003": ("NVIDIA-GPU-en er ikke kompatibel", [
        "Denne GPU-en støtter ikke det nødvendige CUDA/Paddle-miljøet.",
        "Bruk en nyere kompatibel NVIDIA-GPU.",
        "Ikke installer CUDA Toolkit manuelt; programmet inneholder nødvendig runtime.",
    ]),
    "LST-GPU-004": ("For lite grafikkminne", [
        "Lukk spill, nettlesere og andre programmer som bruker GPU-en mye.",
        "Kjør kontrollen igjen og kontroller hvor mye VRAM som er ledig.",
        "Bruk en GPU med mer VRAM hvis oversettelsen fortsatt ikke fungerer.",
    ]),
    "LST-GPU-010": ("Flere NVIDIA-GPU-er ble funnet", [
        "Den gjeldende versjonen bruker NVIDIA GPU 0.",
        "Se i de tekniske detaljene hvilket kort som vises som gpu:0.",
        "Endre GPU-konfigurasjonen i Windows/NVIDIA hvis feil GPU brukes.",
    ]),
    "LST-CAP-001": ("Skjermen kunne ikke fanges riktig", [
        "Kontroller at ønsket skjerm er koblet til NVIDIA-GPU-en.",
        "Prøv Borderless Windowed / vindu uten ramme.",
        "Start Local Screen Translator på nytt og kjør kontrollen igjen.",
    ]),
    "LST-NET-001": ("Den lokale porten 11435 er allerede i bruk", [
        "Lukk andre lokale AI-programmer og Ollama-instanser.",
        "Start Local Screen Translator på nytt.",
        "Hvis problemet fortsetter, start Windows på nytt og åpne Local Screen Translator først.",
    ]),
    "LST-TTS-001": ("Ingen brukbar engelsk Microsoft-stemme ble funnet", [
        "Åpne innstillingene i Local Screen Translator.",
        "Velg og installer en engelsk Microsoft-talepakke.",
        "Start Windows på nytt hvis det er nødvendig.",
    ]),
    "LST-CUDA-001": ("GPU-OCR kunne ikke startes", [
        "Oppdater eller installer NVIDIA-driveren på nytt.",
        "Start Windows på nytt og lukk programmer som bruker GPU-en mye.",
        "Ikke installer Python, PaddlePaddle eller CUDA Toolkit manuelt.",
    ]),
    "LST-FILE-001": ("En nødvendig programfil mangler", [
        "Ikke last ned enkeltmodeller eller DLL-filer manuelt.",
        "Kontroller beskyttelsesloggen i Windows Sikkerhet.",
        "Installer hele programmet på nytt med Setup.exe og alle .bin-filene i samme mappe.",
    ]),
    "LST-ALIGN-001": ("Tekstjusteringskomponenten kunne ikke startes", [
        "Kontroller om Windows Sikkerhet har blokkert LSTAlignWorker.exe.",
        "Installer hele programmet på nytt hvis filen ble fjernet.",
        "Start Windows på nytt og kjør kontrollen igjen.",
    ]),
    "LST-DATA-001": ("Programmet kan ikke lagre innstillinger", [
        "Kontroller at Windows-kontoen din kan skrive til AppData-mappen.",
        "Kontroller Controlled Folder Access og annen sikkerhetsprogramvare.",
        "Kjør systemkontrollen igjen.",
    ]),
    "LST-AI-001": ("De lokale oversettelsesmodellene kunne ikke startes", [
        "Oppdater NVIDIA-driveren og start Windows på nytt.",
        "Lukk andre AI-programmer og programmer som bruker GPU-en mye.",
        "Installer hele programmet på nytt hvis modeller mangler.",
    ]),
    "LST-GEN-001": ("Systemkontrollen fant et problem", [
        "Start Windows på nytt og kjør kontrollen igjen.",
        "Søk på Internett etter den nøyaktige feilteksten fra de tekniske detaljene.",
        "Installer hele programmet på nytt hvis filer mangler.",
    ]),
}



# SELF HELP LANGUAGE BATCH 3A

HELP_TRANSLATIONS_EXTRA["el"] = {
    "LST-SYS-001": ("Μη υποστηριζόμενη διαμόρφωση Windows", [
        "Χρησιμοποιήστε έκδοση 64-bit των Windows 10 ή Windows 11.",
        "Εγκαταστήστε όλες τις διαθέσιμες ενημερώσεις των Windows.",
        "Επανεκκινήστε τα Windows και εκτελέστε ξανά τον έλεγχο συστήματος.",
    ]),
    "LST-GPU-001": ("Δεν εντοπίστηκε GPU NVIDIA ή πρόγραμμα οδήγησης", [
        "Ελέγξτε στη Διαχείριση Συσκευών ότι η GPU NVIDIA εμφανίζεται χωρίς σφάλματα.",
        "Εγκαταστήστε ή επανεγκαταστήστε το επίσημο πρόγραμμα οδήγησης NVIDIA.",
        "Επανεκκινήστε τα Windows και εκτελέστε ξανά τον έλεγχο.",
    ]),
    "LST-GPU-002": ("Το πρόγραμμα οδήγησης NVIDIA είναι πολύ παλιό", [
        "Εγκαταστήστε το νεότερο πρόγραμμα οδήγησης NVIDIA για την κάρτα γραφικών σας.",
        "Επανεκκινήστε τα Windows μετά την εγκατάσταση.",
        "Εκτελέστε ξανά τον έλεγχο συστήματος.",
    ]),
    "LST-GPU-003": ("Η GPU NVIDIA δεν είναι συμβατή", [
        "Αυτή η GPU δεν υποστηρίζει το απαιτούμενο περιβάλλον CUDA/Paddle.",
        "Χρησιμοποιήστε νεότερη συμβατή GPU NVIDIA.",
        "Μην εγκαταστήσετε χειροκίνητα το CUDA Toolkit· η εφαρμογή περιλαμβάνει το απαραίτητο runtime.",
    ]),
    "LST-GPU-004": ("Ανεπαρκής μνήμη γραφικών", [
        "Κλείστε παιχνίδια, προγράμματα περιήγησης και άλλες εφαρμογές που χρησιμοποιούν έντονα τη GPU.",
        "Εκτελέστε ξανά τον έλεγχο και ελέγξτε την ελεύθερη VRAM.",
        "Αν η μετάφραση εξακολουθεί να αποτυγχάνει, χρησιμοποιήστε GPU με περισσότερη VRAM.",
    ]),
    "LST-GPU-010": ("Εντοπίστηκαν πολλές GPU NVIDIA", [
        "Η τρέχουσα έκδοση χρησιμοποιεί την NVIDIA GPU 0.",
        "Ελέγξτε στις τεχνικές λεπτομέρειες ποια κάρτα εμφανίζεται ως gpu:0.",
        "Αν χρησιμοποιείται λάθος GPU, αλλάξτε τη διαμόρφωση GPU στα Windows/NVIDIA.",
    ]),
    "LST-CAP-001": ("Δεν ήταν δυνατή η σωστή καταγραφή της οθόνης", [
        "Βεβαιωθείτε ότι η επιθυμητή οθόνη είναι συνδεδεμένη στην GPU NVIDIA.",
        "Δοκιμάστε λειτουργία Borderless Windowed / παράθυρο χωρίς περιγράμματα.",
        "Επανεκκινήστε το Local Screen Translator και εκτελέστε ξανά τον έλεγχο.",
    ]),
    "LST-NET-001": ("Η τοπική θύρα 11435 χρησιμοποιείται ήδη", [
        "Κλείστε άλλες τοπικές εφαρμογές AI και διεργασίες Ollama.",
        "Επανεκκινήστε το Local Screen Translator.",
        "Αν το πρόβλημα παραμένει, επανεκκινήστε τα Windows και ανοίξτε πρώτα το Local Screen Translator.",
    ]),
    "LST-TTS-001": ("Δεν βρέθηκε κατάλληλη αγγλική φωνή Microsoft", [
        "Ανοίξτε τις ρυθμίσεις του Local Screen Translator.",
        "Επιλέξτε και εγκαταστήστε αγγλικό πακέτο φωνής Microsoft.",
        "Επανεκκινήστε τα Windows αν απαιτείται.",
    ]),
    "LST-CUDA-001": ("Δεν ήταν δυνατή η εκκίνηση του GPU OCR", [
        "Ενημερώστε ή επανεγκαταστήστε το πρόγραμμα οδήγησης NVIDIA.",
        "Επανεκκινήστε τα Windows και κλείστε εφαρμογές που χρησιμοποιούν έντονα τη GPU.",
        "Μην εγκαταστήσετε χειροκίνητα Python, PaddlePaddle ή CUDA Toolkit.",
    ]),
    "LST-FILE-001": ("Λείπει απαιτούμενο αρχείο της εφαρμογής", [
        "Μην κατεβάζετε μεμονωμένα μοντέλα ή αρχεία DLL χειροκίνητα.",
        "Ελέγξτε το ιστορικό προστασίας του Windows Security.",
        "Επανεγκαταστήστε ολόκληρη την εφαρμογή με το Setup.exe και όλα τα αρχεία .bin στον ίδιο φάκελο.",
    ]),
    "LST-ALIGN-001": ("Δεν ήταν δυνατή η εκκίνηση της στοίχισης κειμένου", [
        "Ελέγξτε αν το Windows Security απέκλεισε το LSTAlignWorker.exe.",
        "Αν το αρχείο αφαιρέθηκε, επανεγκαταστήστε πλήρως την εφαρμογή.",
        "Επανεκκινήστε τα Windows και εκτελέστε ξανά τον έλεγχο.",
    ]),
    "LST-DATA-001": ("Η εφαρμογή δεν μπορεί να αποθηκεύσει ρυθμίσεις", [
        "Ελέγξτε ότι ο λογαριασμός Windows έχει δικαίωμα εγγραφής στον φάκελο AppData.",
        "Ελέγξτε το Controlled Folder Access και άλλο λογισμικό ασφαλείας.",
        "Εκτελέστε ξανά τον έλεγχο συστήματος.",
    ]),
    "LST-AI-001": ("Δεν ήταν δυνατή η εκκίνηση των τοπικών μοντέλων μετάφρασης", [
        "Ενημερώστε το πρόγραμμα οδήγησης NVIDIA και επανεκκινήστε τα Windows.",
        "Κλείστε άλλες εφαρμογές AI και εφαρμογές που χρησιμοποιούν έντονα τη GPU.",
        "Αν λείπουν μοντέλα, επανεγκαταστήστε πλήρως την εφαρμογή.",
    ]),
    "LST-GEN-001": ("Ο έλεγχος συστήματος εντόπισε πρόβλημα", [
        "Επανεκκινήστε τα Windows και εκτελέστε ξανά τον έλεγχο.",
        "Αναζητήστε στο Internet το ακριβές κείμενο σφάλματος από τις τεχνικές λεπτομέρειες.",
        "Αν λείπουν αρχεία, επανεγκαταστήστε πλήρως την εφαρμογή.",
    ]),
}


HELP_TRANSLATIONS_EXTRA["hu"] = {
    "LST-SYS-001": ("Nem támogatott Windows-konfiguráció", [
        "Használja a Windows 10 vagy Windows 11 64 bites verzióját.",
        "Telepítse az összes elérhető Windows-frissítést.",
        "Indítsa újra a Windowst, majd futtassa újra a rendszerellenőrzést.",
    ]),
    "LST-GPU-001": ("Az NVIDIA GPU vagy illesztőprogram nem található", [
        "Az Eszközkezelőben ellenőrizze, hogy az NVIDIA GPU hibamentesen jelenik-e meg.",
        "Telepítse vagy telepítse újra a hivatalos NVIDIA-illesztőprogramot.",
        "Indítsa újra a Windowst, majd futtassa újra az ellenőrzést.",
    ]),
    "LST-GPU-002": ("Az NVIDIA-illesztőprogram túl régi", [
        "Telepítse a videokártyájához elérhető legújabb NVIDIA-illesztőprogramot.",
        "A telepítés után indítsa újra a Windowst.",
        "Futtassa újra a rendszerellenőrzést.",
    ]),
    "LST-GPU-003": ("Az NVIDIA GPU nem kompatibilis", [
        "Ez a GPU nem támogatja a szükséges CUDA/Paddle környezetet.",
        "Használjon újabb, kompatibilis NVIDIA GPU-t.",
        "Ne telepítse kézzel a CUDA Toolkit csomagot; az alkalmazás tartalmazza a szükséges futtatókörnyezetet.",
    ]),
    "LST-GPU-004": ("Nincs elegendő videomemória", [
        "Zárja be a játékokat, böngészőket és más GPU-igényes programokat.",
        "Futtassa újra az ellenőrzést, és ellenőrizze a szabad VRAM mennyiségét.",
        "Ha a fordítás továbbra sem működik, használjon több VRAM-mal rendelkező GPU-t.",
    ]),
    "LST-GPU-010": ("Több NVIDIA GPU található", [
        "A jelenlegi verzió az NVIDIA GPU 0 eszközt használja.",
        "A technikai részletekben ellenőrizze, melyik kártya szerepel gpu:0 néven.",
        "Ha nem a megfelelő GPU van használatban, módosítsa a GPU-konfigurációt a Windows/NVIDIA beállításaiban.",
    ]),
    "LST-CAP-001": ("A képernyő rögzítése nem sikerült megfelelően", [
        "Győződjön meg arról, hogy a kívánt monitor az NVIDIA GPU-hoz van csatlakoztatva.",
        "Próbálja ki a Borderless Windowed / keret nélküli ablak módot.",
        "Indítsa újra a Local Screen Translator alkalmazást, majd futtassa újra az ellenőrzést.",
    ]),
    "LST-NET-001": ("A helyi 11435-ös port már használatban van", [
        "Zárja be a többi helyi AI-alkalmazást és Ollama-példányt.",
        "Indítsa újra a Local Screen Translator alkalmazást.",
        "Ha a probléma megmarad, indítsa újra a Windowst, és először a Local Screen Translator alkalmazást indítsa el.",
    ]),
    "LST-TTS-001": ("Nem található használható angol Microsoft-hang", [
        "Nyissa meg a Local Screen Translator beállításait.",
        "Válasszon ki és telepítsen egy angol Microsoft-hangcsomagot.",
        "Szükség esetén indítsa újra a Windowst.",
    ]),
    "LST-CUDA-001": ("A GPU OCR nem indítható el", [
        "Frissítse vagy telepítse újra az NVIDIA-illesztőprogramot.",
        "Indítsa újra a Windowst, és zárja be a GPU-t erősen használó programokat.",
        "Ne telepítse kézzel a Pythont, a PaddlePaddle-t vagy a CUDA Toolkitet.",
    ]),
    "LST-FILE-001": ("Hiányzik egy szükséges alkalmazásfájl", [
        "Ne töltsön le különálló modelleket vagy DLL-fájlokat kézzel.",
        "Ellenőrizze a Windows Security védelmi előzményeit.",
        "Telepítse újra a teljes alkalmazást úgy, hogy a Setup.exe és minden .bin fájl ugyanabban a mappában legyen.",
    ]),
    "LST-ALIGN-001": ("A szövegillesztési komponens nem indítható el", [
        "Ellenőrizze, hogy a Windows Security nem blokkolta-e az LSTAlignWorker.exe fájlt.",
        "Ha a fájlt eltávolították, telepítse újra a teljes alkalmazást.",
        "Indítsa újra a Windowst, majd futtassa újra az ellenőrzést.",
    ]),
    "LST-DATA-001": ("Az alkalmazás nem tudja menteni a beállításokat", [
        "Ellenőrizze, hogy Windows-fiókja írhat-e az AppData mappába.",
        "Ellenőrizze a Controlled Folder Access és más biztonsági szoftverek beállításait.",
        "Futtassa újra a rendszerellenőrzést.",
    ]),
    "LST-AI-001": ("A helyi fordítási modellek nem indíthatók el", [
        "Frissítse az NVIDIA-illesztőprogramot, majd indítsa újra a Windowst.",
        "Zárja be a többi AI-programot és GPU-igényes alkalmazást.",
        "Ha modellek hiányoznak, telepítse újra a teljes alkalmazást.",
    ]),
    "LST-GEN-001": ("A rendszerellenőrzés problémát talált", [
        "Indítsa újra a Windowst, majd futtassa újra az ellenőrzést.",
        "Keressen rá az interneten a technikai részletekben található pontos hibaüzenetre.",
        "Ha fájlok hiányoznak, telepítse újra a teljes alkalmazást.",
    ]),
}


HELP_TRANSLATIONS_EXTRA["ro"] = {
    "LST-SYS-001": ("Configurație Windows neacceptată", [
        "Utilizați o versiune pe 64 de biți de Windows 10 sau Windows 11.",
        "Instalați toate actualizările Windows disponibile.",
        "Reporniți Windows și rulați din nou verificarea sistemului.",
    ]),
    "LST-GPU-001": ("GPU-ul NVIDIA sau driverul nu a fost detectat", [
        "Verificați în Device Manager dacă GPU-ul NVIDIA apare fără erori.",
        "Instalați sau reinstalați driverul NVIDIA oficial.",
        "Reporniți Windows și rulați din nou verificarea.",
    ]),
    "LST-GPU-002": ("Driverul NVIDIA este prea vechi", [
        "Instalați cel mai nou driver NVIDIA pentru placa dvs. video.",
        "Reporniți Windows după instalare.",
        "Rulați din nou verificarea sistemului.",
    ]),
    "LST-GPU-003": ("GPU-ul NVIDIA nu este compatibil", [
        "Acest GPU nu acceptă mediul CUDA/Paddle necesar.",
        "Utilizați un GPU NVIDIA compatibil mai nou.",
        "Nu instalați manual CUDA Toolkit; aplicația include mediul necesar.",
    ]),
    "LST-GPU-004": ("Memorie video insuficientă", [
        "Închideți jocurile, browserele și alte programe care folosesc intens GPU-ul.",
        "Rulați din nou verificarea și consultați memoria VRAM liberă.",
        "Dacă traducerea continuă să nu funcționeze, utilizați un GPU cu mai multă VRAM.",
    ]),
    "LST-GPU-010": ("Au fost detectate mai multe GPU-uri NVIDIA", [
        "Versiunea curentă utilizează NVIDIA GPU 0.",
        "Consultați detaliile tehnice pentru a vedea ce placă este afișată ca gpu:0.",
        "Dacă este utilizat GPU-ul greșit, modificați configurația GPU în Windows/NVIDIA.",
    ]),
    "LST-CAP-001": ("Ecranul nu a putut fi capturat corect", [
        "Asigurați-vă că monitorul dorit este conectat la GPU-ul NVIDIA.",
        "Încercați modul Borderless Windowed / fereastră fără margini.",
        "Reporniți Local Screen Translator și rulați din nou verificarea.",
    ]),
    "LST-NET-001": ("Portul local 11435 este deja utilizat", [
        "Închideți alte aplicații AI locale și instanțe Ollama.",
        "Reporniți Local Screen Translator.",
        "Dacă problema persistă, reporniți Windows și deschideți mai întâi Local Screen Translator.",
    ]),
    "LST-TTS-001": ("Nu a fost găsită o voce engleză Microsoft utilizabilă", [
        "Deschideți setările Local Screen Translator.",
        "Selectați și instalați un pachet vocal Microsoft în limba engleză.",
        "Reporniți Windows dacă este necesar.",
    ]),
    "LST-CUDA-001": ("OCR-ul pe GPU nu a putut fi pornit", [
        "Actualizați sau reinstalați driverul NVIDIA.",
        "Reporniți Windows și închideți programele care folosesc intens GPU-ul.",
        "Nu instalați manual Python, PaddlePaddle sau CUDA Toolkit.",
    ]),
    "LST-FILE-001": ("Lipsește un fișier necesar al aplicației", [
        "Nu descărcați manual modele individuale sau fișiere DLL.",
        "Verificați istoricul de protecție din Windows Security.",
        "Reinstalați aplicația completă cu Setup.exe și toate fișierele .bin în același folder.",
    ]),
    "LST-ALIGN-001": ("Componenta de aliniere a textului nu a putut fi pornită", [
        "Verificați dacă Windows Security a blocat LSTAlignWorker.exe.",
        "Dacă fișierul a fost eliminat, reinstalați complet aplicația.",
        "Reporniți Windows și rulați din nou verificarea.",
    ]),
    "LST-DATA-001": ("Aplicația nu poate salva setările", [
        "Verificați dacă utilizatorul Windows poate scrie în folderul AppData.",
        "Verificați Controlled Folder Access și alte programe de securitate.",
        "Rulați din nou verificarea sistemului.",
    ]),
    "LST-AI-001": ("Modelele locale de traducere nu au putut fi pornite", [
        "Actualizați driverul NVIDIA și reporniți Windows.",
        "Închideți alte aplicații AI și programe care utilizează intens GPU-ul.",
        "Dacă lipsesc modele, reinstalați complet aplicația.",
    ]),
    "LST-GEN-001": ("Verificarea sistemului a detectat o problemă", [
        "Reporniți Windows și rulați din nou verificarea.",
        "Căutați pe Internet textul exact al erorii din detaliile tehnice.",
        "Dacă lipsesc fișiere, reinstalați complet aplicația.",
    ]),
}


HELP_TRANSLATIONS_EXTRA["lt"] = {
    "LST-SYS-001": ("Nepalaikoma Windows konfigūracija", [
        "Naudokite 64 bitų Windows 10 arba Windows 11 versiją.",
        "Įdiekite visus galimus Windows naujinimus.",
        "Paleiskite Windows iš naujo ir dar kartą vykdykite sistemos patikrą.",
    ]),
    "LST-GPU-001": ("NVIDIA GPU arba tvarkyklė neaptikta", [
        "Įrenginių tvarkytuvėje patikrinkite, ar NVIDIA GPU rodomas be klaidų.",
        "Įdiekite arba iš naujo įdiekite oficialią NVIDIA tvarkyklę.",
        "Paleiskite Windows iš naujo ir dar kartą vykdykite patikrą.",
    ]),
    "LST-GPU-002": ("NVIDIA tvarkyklė per sena", [
        "Įdiekite naujausią NVIDIA tvarkyklę savo vaizdo plokštei.",
        "Po diegimo paleiskite Windows iš naujo.",
        "Dar kartą vykdykite sistemos patikrą.",
    ]),
    "LST-GPU-003": ("NVIDIA GPU nesuderinamas", [
        "Šis GPU nepalaiko reikiamos CUDA/Paddle aplinkos.",
        "Naudokite naujesnį suderinamą NVIDIA GPU.",
        "Neįdiekite CUDA Toolkit rankiniu būdu; programa turi reikiamą vykdymo aplinką.",
    ]),
    "LST-GPU-004": ("Nepakanka vaizdo atminties", [
        "Uždarykite žaidimus, naršykles ir kitas GPU intensyviai naudojančias programas.",
        "Dar kartą vykdykite patikrą ir patikrinkite laisvą VRAM.",
        "Jei vertimas vis tiek neveikia, naudokite GPU su daugiau VRAM.",
    ]),
    "LST-GPU-010": ("Aptikti keli NVIDIA GPU", [
        "Dabartinė versija naudoja NVIDIA GPU 0.",
        "Techninėje informacijoje patikrinkite, kuri plokštė rodoma kaip gpu:0.",
        "Jei naudojamas netinkamas GPU, pakeiskite GPU konfigūraciją Windows/NVIDIA nustatymuose.",
    ]),
    "LST-CAP-001": ("Nepavyko tinkamai užfiksuoti ekrano", [
        "Įsitikinkite, kad norimas monitorius prijungtas prie NVIDIA GPU.",
        "Išbandykite Borderless Windowed / lango be rėmelių režimą.",
        "Paleiskite Local Screen Translator iš naujo ir dar kartą vykdykite patikrą.",
    ]),
    "LST-NET-001": ("Vietinis 11435 prievadas jau naudojamas", [
        "Uždarykite kitas vietines AI programas ir Ollama procesus.",
        "Paleiskite Local Screen Translator iš naujo.",
        "Jei problema išlieka, paleiskite Windows iš naujo ir pirmiausia atidarykite Local Screen Translator.",
    ]),
    "LST-TTS-001": ("Nerastas tinkamas angliškas Microsoft balsas", [
        "Atidarykite Local Screen Translator nustatymus.",
        "Pasirinkite ir įdiekite anglišką Microsoft balso paketą.",
        "Jei reikia, paleiskite Windows iš naujo.",
    ]),
    "LST-CUDA-001": ("Nepavyko paleisti GPU OCR", [
        "Atnaujinkite arba iš naujo įdiekite NVIDIA tvarkyklę.",
        "Paleiskite Windows iš naujo ir uždarykite GPU intensyviai naudojančias programas.",
        "Neįdiekite Python, PaddlePaddle ar CUDA Toolkit rankiniu būdu.",
    ]),
    "LST-FILE-001": ("Trūksta būtino programos failo", [
        "Neatsisiųskite atskirų modelių ar DLL failų rankiniu būdu.",
        "Patikrinkite Windows Security apsaugos istoriją.",
        "Iš naujo įdiekite visą programą, laikydami Setup.exe ir visus .bin failus tame pačiame aplanke.",
    ]),
    "LST-ALIGN-001": ("Nepavyko paleisti teksto lygiavimo komponento", [
        "Patikrinkite, ar Windows Security neužblokavo LSTAlignWorker.exe.",
        "Jei failas pašalintas, visiškai iš naujo įdiekite programą.",
        "Paleiskite Windows iš naujo ir dar kartą vykdykite patikrą.",
    ]),
    "LST-DATA-001": ("Programa negali išsaugoti nustatymų", [
        "Patikrinkite, ar Windows naudotojas gali rašyti į AppData aplanką.",
        "Patikrinkite Controlled Folder Access ir kitą saugos programinę įrangą.",
        "Dar kartą vykdykite sistemos patikrą.",
    ]),
    "LST-AI-001": ("Nepavyko paleisti vietinių vertimo modelių", [
        "Atnaujinkite NVIDIA tvarkyklę ir paleiskite Windows iš naujo.",
        "Uždarykite kitas AI programas ir GPU intensyviai naudojančias programas.",
        "Jei trūksta modelių, visiškai iš naujo įdiekite programą.",
    ]),
    "LST-GEN-001": ("Sistemos patikra aptiko problemą", [
        "Paleiskite Windows iš naujo ir dar kartą vykdykite patikrą.",
        "Internete ieškokite tikslaus klaidos teksto iš techninės informacijos.",
        "Jei trūksta failų, visiškai iš naujo įdiekite programą.",
    ]),
}



# SELF HELP LANGUAGE BATCH 3B

HELP_TRANSLATIONS_EXTRA["lv"] = {
    "LST-SYS-001": ("Neatbalstīta Windows konfigurācija", [
        "Izmantojiet Windows 10 vai Windows 11 64 bitu versiju.",
        "Instalējiet visus pieejamos Windows atjauninājumus.",
        "Restartējiet Windows un vēlreiz palaidiet sistēmas pārbaudi.",
    ]),
    "LST-GPU-001": ("NVIDIA GPU vai draiveris netika atrasts", [
        "Ierīču pārvaldniekā pārbaudiet, vai NVIDIA GPU tiek rādīts bez kļūdām.",
        "Instalējiet vai pārinstalējiet oficiālo NVIDIA draiveri.",
        "Restartējiet Windows un vēlreiz palaidiet pārbaudi.",
    ]),
    "LST-GPU-002": ("NVIDIA draiveris ir pārāk vecs", [
        "Instalējiet jaunāko NVIDIA draiveri savai videokartei.",
        "Pēc instalēšanas restartējiet Windows.",
        "Vēlreiz palaidiet sistēmas pārbaudi.",
    ]),
    "LST-GPU-003": ("NVIDIA GPU nav saderīgs", [
        "Šis GPU neatbalsta nepieciešamo CUDA/Paddle vidi.",
        "Izmantojiet jaunāku saderīgu NVIDIA GPU.",
        "Neinstalējiet CUDA Toolkit manuāli; lietotnē ir nepieciešamā izpildvide.",
    ]),
    "LST-GPU-004": ("Nepietiek videomemoriņas", [
        "Aizveriet spēles, pārlūkprogrammas un citas programmas, kas intensīvi izmanto GPU.",
        "Vēlreiz palaidiet pārbaudi un pārbaudiet brīvo VRAM.",
        "Ja tulkošana joprojām nedarbojas, izmantojiet GPU ar lielāku VRAM.",
    ]),
    "LST-GPU-010": ("Atrasti vairāki NVIDIA GPU", [
        "Pašreizējā versija izmanto NVIDIA GPU 0.",
        "Tehniskajā informācijā pārbaudiet, kura videokarte norādīta kā gpu:0.",
        "Ja tiek izmantots nepareizais GPU, mainiet GPU konfigurāciju Windows/NVIDIA iestatījumos.",
    ]),
    "LST-CAP-001": ("Ekrānu neizdevās pareizi uztvert", [
        "Pārliecinieties, ka vajadzīgais monitors ir pievienots NVIDIA GPU.",
        "Izmēģiniet Borderless Windowed / bezmalu loga režīmu.",
        "Restartējiet Local Screen Translator un vēlreiz palaidiet pārbaudi.",
    ]),
    "LST-NET-001": ("Lokālais ports 11435 jau tiek izmantots", [
        "Aizveriet citas lokālās AI programmas un Ollama procesus.",
        "Restartējiet Local Screen Translator.",
        "Ja problēma saglabājas, restartējiet Windows un vispirms palaidiet Local Screen Translator.",
    ]),
    "LST-TTS-001": ("Nav atrasta piemērota Microsoft angļu balss", [
        "Atveriet Local Screen Translator iestatījumus.",
        "Izvēlieties un instalējiet Microsoft angļu balss pakotni.",
        "Ja nepieciešams, restartējiet Windows.",
    ]),
    "LST-CUDA-001": ("GPU OCR neizdevās palaist", [
        "Atjauniniet vai pārinstalējiet NVIDIA draiveri.",
        "Restartējiet Windows un aizveriet programmas, kas intensīvi izmanto GPU.",
        "Neinstalējiet Python, PaddlePaddle vai CUDA Toolkit manuāli.",
    ]),
    "LST-FILE-001": ("Trūkst nepieciešama lietotnes faila", [
        "Nelejupielādējiet atsevišķus modeļus vai DLL failus manuāli.",
        "Pārbaudiet Windows Security aizsardzības vēsturi.",
        "Pilnībā pārinstalējiet lietotni, novietojot Setup.exe un visus .bin failus vienā mapē.",
    ]),
    "LST-ALIGN-001": ("Teksta izlīdzināšanas komponentu neizdevās palaist", [
        "Pārbaudiet, vai Windows Security nav bloķējis LSTAlignWorker.exe.",
        "Ja fails tika noņemts, pilnībā pārinstalējiet lietotni.",
        "Restartējiet Windows un vēlreiz palaidiet pārbaudi.",
    ]),
    "LST-DATA-001": ("Lietotne nevar saglabāt iestatījumus", [
        "Pārbaudiet, vai jūsu Windows konts drīkst rakstīt AppData mapē.",
        "Pārbaudiet Controlled Folder Access un citu drošības programmatūru.",
        "Vēlreiz palaidiet sistēmas pārbaudi.",
    ]),
    "LST-AI-001": ("Lokālos tulkošanas modeļus neizdevās palaist", [
        "Atjauniniet NVIDIA draiveri un restartējiet Windows.",
        "Aizveriet citas AI programmas un GPU intensīvi izmantojošas lietotnes.",
        "Ja trūkst modeļu, pilnībā pārinstalējiet lietotni.",
    ]),
    "LST-GEN-001": ("Sistēmas pārbaude atrada problēmu", [
        "Restartējiet Windows un vēlreiz palaidiet pārbaudi.",
        "Internetā meklējiet precīzu kļūdas tekstu no tehniskās informācijas.",
        "Ja trūkst failu, pilnībā pārinstalējiet lietotni.",
    ]),
}


HELP_TRANSLATIONS_EXTRA["et"] = {
    "LST-SYS-001": ("Windowsi konfiguratsiooni ei toetata", [
        "Kasutage Windows 10 või Windows 11 64-bitist versiooni.",
        "Installige kõik saadaolevad Windowsi värskendused.",
        "Taaskäivitage Windows ja käivitage süsteemikontroll uuesti.",
    ]),
    "LST-GPU-001": ("NVIDIA GPU-d või draiverit ei leitud", [
        "Kontrollige seadmehalduris, et NVIDIA GPU kuvatakse ilma vigadeta.",
        "Installige või installige uuesti ametlik NVIDIA draiver.",
        "Taaskäivitage Windows ja käivitage kontroll uuesti.",
    ]),
    "LST-GPU-002": ("NVIDIA draiver on liiga vana", [
        "Installige oma videokaardi uusim NVIDIA draiver.",
        "Pärast installimist taaskäivitage Windows.",
        "Käivitage süsteemikontroll uuesti.",
    ]),
    "LST-GPU-003": ("NVIDIA GPU ei ole ühilduv", [
        "See GPU ei toeta vajalikku CUDA/Paddle keskkonda.",
        "Kasutage uuemat ühilduvat NVIDIA GPU-d.",
        "Ärge installige CUDA Toolkiti käsitsi; rakendus sisaldab vajalikku käituskeskkonda.",
    ]),
    "LST-GPU-004": ("Videomälu pole piisavalt", [
        "Sulgege mängud, brauserid ja muud GPU-d intensiivselt kasutavad programmid.",
        "Käivitage kontroll uuesti ja vaadake vaba VRAM-i hulka.",
        "Kui tõlkimine endiselt ei tööta, kasutage suurema VRAM-iga GPU-d.",
    ]),
    "LST-GPU-010": ("Tuvastati mitu NVIDIA GPU-d", [
        "Praegune versioon kasutab NVIDIA GPU 0.",
        "Kontrollige tehnilistest andmetest, milline kaart kuvatakse kui gpu:0.",
        "Kui kasutatakse valet GPU-d, muutke GPU konfiguratsiooni Windowsi/NVIDIA seadetes.",
    ]),
    "LST-CAP-001": ("Ekraani ei õnnestunud õigesti jäädvustada", [
        "Veenduge, et soovitud monitor oleks ühendatud NVIDIA GPU-ga.",
        "Proovige Borderless Windowed / ääristeta akna režiimi.",
        "Taaskäivitage Local Screen Translator ja käivitage kontroll uuesti.",
    ]),
    "LST-NET-001": ("Kohalik port 11435 on juba kasutusel", [
        "Sulgege muud kohalikud AI-programmid ja Ollama protsessid.",
        "Taaskäivitage Local Screen Translator.",
        "Kui probleem püsib, taaskäivitage Windows ja avage esmalt Local Screen Translator.",
    ]),
    "LST-TTS-001": ("Sobivat Microsofti ingliskeelset häält ei leitud", [
        "Avage Local Screen Translator seadistused.",
        "Valige ja installige Microsofti ingliskeelne häälepakett.",
        "Vajadusel taaskäivitage Windows.",
    ]),
    "LST-CUDA-001": ("GPU OCR-i ei õnnestunud käivitada", [
        "Uuendage või installige uuesti NVIDIA draiver.",
        "Taaskäivitage Windows ja sulgege GPU-d intensiivselt kasutavad programmid.",
        "Ärge installige Pythonit, PaddlePaddle'i ega CUDA Toolkiti käsitsi.",
    ]),
    "LST-FILE-001": ("Vajalik rakenduse fail puudub", [
        "Ärge laadige üksikuid mudeleid ega DLL-faile käsitsi alla.",
        "Kontrollige Windows Security kaitseajalugu.",
        "Installige kogu rakendus uuesti, hoides Setup.exe ja kõik .bin-failid samas kaustas.",
    ]),
    "LST-ALIGN-001": ("Teksti joondamise komponenti ei õnnestunud käivitada", [
        "Kontrollige, kas Windows Security blokeeris faili LSTAlignWorker.exe.",
        "Kui fail eemaldati, installige rakendus täielikult uuesti.",
        "Taaskäivitage Windows ja käivitage kontroll uuesti.",
    ]),
    "LST-DATA-001": ("Rakendus ei saa seadistusi salvestada", [
        "Kontrollige, kas teie Windowsi konto saab AppData kausta kirjutada.",
        "Kontrollige Controlled Folder Accessi ja muud turvatarkvara.",
        "Käivitage süsteemikontroll uuesti.",
    ]),
    "LST-AI-001": ("Kohalikke tõlkemudeleid ei õnnestunud käivitada", [
        "Uuendage NVIDIA draiverit ja taaskäivitage Windows.",
        "Sulgege muud AI-programmid ja GPU-d intensiivselt kasutavad rakendused.",
        "Kui mudelid puuduvad, installige rakendus täielikult uuesti.",
    ]),
    "LST-GEN-001": ("Süsteemikontroll leidis probleemi", [
        "Taaskäivitage Windows ja käivitage kontroll uuesti.",
        "Otsige Internetist tehnilistes andmetes kuvatavat täpset veateksti.",
        "Kui failid puuduvad, installige rakendus täielikult uuesti.",
    ]),
}


HELP_TRANSLATIONS_EXTRA["sl"] = {
    "LST-SYS-001": ("Nepodprta konfiguracija Windows", [
        "Uporabite 64-bitno različico Windows 10 ali Windows 11.",
        "Namestite vse razpoložljive posodobitve Windows.",
        "Znova zaženite Windows in ponovno izvedite preverjanje sistema.",
    ]),
    "LST-GPU-001": ("GPU NVIDIA ali gonilnik ni bil zaznan", [
        "V Upravitelju naprav preverite, ali je GPU NVIDIA prikazan brez napak.",
        "Namestite ali znova namestite uradni gonilnik NVIDIA.",
        "Znova zaženite Windows in ponovno izvedite preverjanje.",
    ]),
    "LST-GPU-002": ("Gonilnik NVIDIA je prestar", [
        "Namestite najnovejši gonilnik NVIDIA za svojo grafično kartico.",
        "Po namestitvi znova zaženite Windows.",
        "Ponovno izvedite preverjanje sistema.",
    ]),
    "LST-GPU-003": ("GPU NVIDIA ni združljiv", [
        "Ta GPU ne podpira zahtevanega okolja CUDA/Paddle.",
        "Uporabite novejši združljiv GPU NVIDIA.",
        "CUDA Toolkita ne nameščajte ročno; aplikacija vsebuje potrebno izvajalno okolje.",
    ]),
    "LST-GPU-004": ("Premalo grafičnega pomnilnika", [
        "Zaprite igre, brskalnike in druge programe, ki močno uporabljajo GPU.",
        "Ponovno izvedite preverjanje in preverite količino prostega VRAM.",
        "Če prevajanje še vedno ne deluje, uporabite GPU z več VRAM.",
    ]),
    "LST-GPU-010": ("Zaznanih je več GPU-jev NVIDIA", [
        "Trenutna različica uporablja NVIDIA GPU 0.",
        "V tehničnih podrobnostih preverite, katera kartica je prikazana kot gpu:0.",
        "Če se uporablja napačen GPU, spremenite konfiguracijo GPU v Windows/NVIDIA.",
    ]),
    "LST-CAP-001": ("Zaslona ni bilo mogoče pravilno zajeti", [
        "Prepričajte se, da je želeni monitor priključen na GPU NVIDIA.",
        "Poskusite način Borderless Windowed / okno brez robov.",
        "Znova zaženite Local Screen Translator in ponovno izvedite preverjanje.",
    ]),
    "LST-NET-001": ("Lokalna vrata 11435 so že v uporabi", [
        "Zaprite druge lokalne programe AI in primerke Ollama.",
        "Znova zaženite Local Screen Translator.",
        "Če težava ostane, znova zaženite Windows in najprej odprite Local Screen Translator.",
    ]),
    "LST-TTS-001": ("Ustrezen angleški glas Microsoft ni bil najden", [
        "Odprite nastavitve Local Screen Translator.",
        "Izberite in namestite angleški glasovni paket Microsoft.",
        "Če je potrebno, znova zaženite Windows.",
    ]),
    "LST-CUDA-001": ("GPU OCR ni bilo mogoče zagnati", [
        "Posodobite ali znova namestite gonilnik NVIDIA.",
        "Znova zaženite Windows in zaprite programe, ki močno uporabljajo GPU.",
        "Ne nameščajte Python, PaddlePaddle ali CUDA Toolkit ročno.",
    ]),
    "LST-FILE-001": ("Manjka zahtevana datoteka aplikacije", [
        "Posameznih modelov ali DLL-datotek ne prenašajte ročno.",
        "Preverite zgodovino zaščite Windows Security.",
        "Ponovno namestite celotno aplikacijo z Setup.exe in vsemi .bin-datotekami v isti mapi.",
    ]),
    "LST-ALIGN-001": ("Komponente za poravnavo besedila ni bilo mogoče zagnati", [
        "Preverite, ali je Windows Security blokiral LSTAlignWorker.exe.",
        "Če je bila datoteka odstranjena, ponovno namestite celotno aplikacijo.",
        "Znova zaženite Windows in ponovno izvedite preverjanje.",
    ]),
    "LST-DATA-001": ("Aplikacija ne more shraniti nastavitev", [
        "Preverite, ali lahko vaš račun Windows zapisuje v mapo AppData.",
        "Preverite Controlled Folder Access in drugo varnostno programsko opremo.",
        "Ponovno izvedite preverjanje sistema.",
    ]),
    "LST-AI-001": ("Lokalnih modelov za prevajanje ni bilo mogoče zagnati", [
        "Posodobite gonilnik NVIDIA in znova zaženite Windows.",
        "Zaprite druge programe AI in aplikacije, ki močno uporabljajo GPU.",
        "Če modeli manjkajo, ponovno namestite celotno aplikacijo.",
    ]),
    "LST-GEN-001": ("Preverjanje sistema je našlo težavo", [
        "Znova zaženite Windows in ponovno izvedite preverjanje.",
        "Na internetu poiščite natančno besedilo napake iz tehničnih podrobnosti.",
        "Če manjkajo datoteke, ponovno namestite celotno aplikacijo.",
    ]),
}


HELP_TRANSLATIONS_EXTRA["bg"] = {
    "LST-SYS-001": ("Неподдържана конфигурация на Windows", [
        "Използвайте 64-битова версия на Windows 10 или Windows 11.",
        "Инсталирайте всички налични актуализации на Windows.",
        "Рестартирайте Windows и стартирайте проверката на системата отново.",
    ]),
    "LST-GPU-001": ("NVIDIA GPU или драйверът не е открит", [
        "Проверете в Device Manager дали NVIDIA GPU се показва без грешки.",
        "Инсталирайте или преинсталирайте официалния NVIDIA драйвер.",
        "Рестартирайте Windows и стартирайте проверката отново.",
    ]),
    "LST-GPU-002": ("NVIDIA драйверът е твърде стар", [
        "Инсталирайте най-новия NVIDIA драйвер за вашата видеокарта.",
        "След инсталацията рестартирайте Windows.",
        "Стартирайте проверката на системата отново.",
    ]),
    "LST-GPU-003": ("NVIDIA GPU не е съвместим", [
        "Този GPU не поддържа необходимата CUDA/Paddle среда.",
        "Използвайте по-нов съвместим NVIDIA GPU.",
        "Не инсталирайте CUDA Toolkit ръчно; приложението съдържа необходимата среда.",
    ]),
    "LST-GPU-004": ("Недостатъчна видеопамет", [
        "Затворете игри, браузъри и други програми, които използват интензивно GPU.",
        "Стартирайте проверката отново и проверете свободната VRAM.",
        "Ако преводът все още не работи, използвайте GPU с повече VRAM.",
    ]),
    "LST-GPU-010": ("Открити са няколко NVIDIA GPU", [
        "Текущата версия използва NVIDIA GPU 0.",
        "В техническите данни проверете коя видеокарта е показана като gpu:0.",
        "Ако се използва грешният GPU, променете GPU конфигурацията в Windows/NVIDIA.",
    ]),
    "LST-CAP-001": ("Екранът не може да бъде заснет правилно", [
        "Уверете се, че желаният монитор е свързан към NVIDIA GPU.",
        "Опитайте режим Borderless Windowed / прозорец без рамки.",
        "Рестартирайте Local Screen Translator и стартирайте проверката отново.",
    ]),
    "LST-NET-001": ("Локалният порт 11435 вече се използва", [
        "Затворете други локални AI приложения и процеси на Ollama.",
        "Рестартирайте Local Screen Translator.",
        "Ако проблемът остане, рестартирайте Windows и първо стартирайте Local Screen Translator.",
    ]),
    "LST-TTS-001": ("Не е намерен подходящ английски глас на Microsoft", [
        "Отворете настройките на Local Screen Translator.",
        "Изберете и инсталирайте английски гласов пакет на Microsoft.",
        "Ако е необходимо, рестартирайте Windows.",
    ]),
    "LST-CUDA-001": ("GPU OCR не може да бъде стартиран", [
        "Актуализирайте или преинсталирайте NVIDIA драйвера.",
        "Рестартирайте Windows и затворете програми, които използват интензивно GPU.",
        "Не инсталирайте Python, PaddlePaddle или CUDA Toolkit ръчно.",
    ]),
    "LST-FILE-001": ("Липсва необходим файл на приложението", [
        "Не изтегляйте отделни модели или DLL файлове ръчно.",
        "Проверете историята на защитата в Windows Security.",
        "Преинсталирайте цялото приложение с Setup.exe и всички .bin файлове в една и съща папка.",
    ]),
    "LST-ALIGN-001": ("Компонентът за подравняване на текст не може да бъде стартиран", [
        "Проверете дали Windows Security не е блокирал LSTAlignWorker.exe.",
        "Ако файлът е премахнат, преинсталирайте напълно приложението.",
        "Рестартирайте Windows и стартирайте проверката отново.",
    ]),
    "LST-DATA-001": ("Приложението не може да запази настройките", [
        "Проверете дали вашият Windows акаунт може да записва в папката AppData.",
        "Проверете Controlled Folder Access и друг софтуер за сигурност.",
        "Стартирайте проверката на системата отново.",
    ]),
    "LST-AI-001": ("Локалните модели за превод не могат да бъдат стартирани", [
        "Актуализирайте NVIDIA драйвера и рестартирайте Windows.",
        "Затворете други AI приложения и програми, които използват интензивно GPU.",
        "Ако липсват модели, преинсталирайте напълно приложението.",
    ]),
    "LST-GEN-001": ("Проверката на системата откри проблем", [
        "Рестартирайте Windows и стартирайте проверката отново.",
        "Потърсете в интернет точния текст на грешката от техническите данни.",
        "Ако липсват файлове, преинсталирайте напълно приложението.",
    ]),
}


# Convert compact tuples to the structure used by system_check_help.py.
for _language, _entries in list(HELP_TRANSLATIONS_EXTRA.items()):
    HELP_TRANSLATIONS_EXTRA[_language] = {
        _code: {
            "title": _value[0],
            "actions": _value[1],
        }
        for _code, _value in _entries.items()
    }
