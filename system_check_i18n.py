from __future__ import annotations

from ui_i18n import (
    detect_system_language,
    resolve_ui_language,
)


SC_TRANSLATIONS = {
    "en": {
        "system_check": "System Check",
        "description": (
            "Checks GPU, OCR, screen capture, local AI models, "
            "alignment and Windows speech."
        ),
        "ready_to_check": "Ready to check.",
        "checking": (
            "Checking system compatibility. "
            "The AI model test can take a little while..."
        ),
        "placeholder": "System Check results will appear here.",
        "run_again": "Run again",
        "copy_report": "Copy report",
        "close": "Close",
        "copied": "Copied",
        "status_ready": (
            "System ready - all compatibility checks passed."
        ),
        "status_warnings": (
            "System Check completed with warnings."
        ),
        "status_problems": (
            "Problems were found. Follow the instructions below."
        ),
        "status_failed": (
            "System Check could not complete."
        ),
        "technical_details": "TECHNICAL DETAILS",
        "report_ready_title": "SYSTEM READY",
        "report_ready_line1": "All compatibility checks passed.",
        "report_ready_line2": "Local Screen Translator is ready to use.",
        "report_self_help_title": (
            "LOCAL SCREEN TRANSLATOR - SELF-HELP REPORT"
        ),
        "report_detected": "Detected:",
        "report_how_to_fix": "How to fix:",
        "report_search_web": "Search the web for:",
        "report_after_steps": (
            "After completing the suggested steps, "
            "run System Check again."
        ),
    },

    "ru": {
        "system_check": "Проверка системы",
        "description": (
            "Проверяет GPU, OCR, захват экрана, локальные ИИ-модели, "
            "выравнивание текста и синтез речи Windows."
        ),
        "ready_to_check": "Готово к проверке.",
        "checking": (
            "Проверка совместимости системы. "
            "Тест ИИ-моделей может занять некоторое время..."
        ),
        "placeholder": "Здесь появятся результаты проверки системы.",
        "run_again": "Проверить снова",
        "copy_report": "Копировать отчёт",
        "close": "Закрыть",
        "copied": "Скопировано",
        "status_ready": (
            "Система готова — все проверки совместимости пройдены."
        ),
        "status_warnings": (
            "Проверка системы завершена с предупреждениями."
        ),
        "status_problems": (
            "Обнаружены проблемы. Следуйте инструкциям ниже."
        ),
        "status_failed": (
            "Не удалось завершить проверку системы."
        ),
        "technical_details": "ТЕХНИЧЕСКИЕ ДАННЫЕ",
        "report_ready_title": "СИСТЕМА ГОТОВА",
        "report_ready_line1": (
            "Все проверки совместимости успешно пройдены."
        ),
        "report_ready_line2": (
            "Local Screen Translator готов к работе."
        ),
        "report_self_help_title": (
            "LOCAL SCREEN TRANSLATOR - "
            "САМОСТОЯТЕЛЬНАЯ ДИАГНОСТИКА"
        ),
        "report_detected": "Обнаружено:",
        "report_how_to_fix": "Как исправить:",
        "report_search_web": "Для поиска в интернете:",
        "report_after_steps": (
            "После выполнения указанных действий "
            "снова запустите Проверку системы."
        ),
    },
}


# SYSTEM CHECK LANGUAGE BATCH 1
SC_TRANSLATIONS.update({
    "de": {
        "system_check": "Systemprüfung",
        "description": (
            "Prüft GPU, OCR, Bildschirmaufnahme, lokale KI-Modelle, "
            "Textausrichtung und Windows-Sprachausgabe."
        ),
        "ready_to_check": "Bereit zur Prüfung.",
        "checking": (
            "Systemkompatibilität wird geprüft. "
            "Der Test der KI-Modelle kann etwas dauern..."
        ),
        "placeholder": "Die Ergebnisse der Systemprüfung erscheinen hier.",
        "run_again": "Erneut prüfen",
        "copy_report": "Bericht kopieren",
        "close": "Schließen",
        "copied": "Kopiert",
        "status_ready": "System bereit – alle Kompatibilitätsprüfungen bestanden.",
        "status_warnings": "Systemprüfung mit Warnungen abgeschlossen.",
        "status_problems": "Probleme wurden gefunden. Folgen Sie den Anweisungen unten.",
        "status_failed": "Die Systemprüfung konnte nicht abgeschlossen werden.",
        "technical_details": "TECHNISCHE DETAILS",
        "report_ready_title": "SYSTEM BEREIT",
        "report_ready_line1": "Alle Kompatibilitätsprüfungen wurden erfolgreich bestanden.",
        "report_ready_line2": "Local Screen Translator ist einsatzbereit.",
        "report_self_help_title": "LOCAL SCREEN TRANSLATOR - SELBSTHILFE-DIAGNOSE",
        "report_detected": "Erkannt:",
        "report_how_to_fix": "So beheben Sie das Problem:",
        "report_search_web": "Im Internet suchen nach:",
        "report_after_steps": "Führen Sie nach diesen Schritten die Systemprüfung erneut aus.",
    },

    "fr": {
        "system_check": "Vérification du système",
        "description": (
            "Vérifie le GPU, l’OCR, la capture d’écran, les modèles d’IA locaux, "
            "l’alignement du texte et la synthèse vocale Windows."
        ),
        "ready_to_check": "Prêt pour la vérification.",
        "checking": (
            "Vérification de la compatibilité du système. "
            "Le test des modèles d’IA peut prendre un peu de temps..."
        ),
        "placeholder": "Les résultats de la vérification apparaîtront ici.",
        "run_again": "Vérifier à nouveau",
        "copy_report": "Copier le rapport",
        "close": "Fermer",
        "copied": "Copié",
        "status_ready": "Système prêt — toutes les vérifications de compatibilité ont réussi.",
        "status_warnings": "Vérification terminée avec des avertissements.",
        "status_problems": "Des problèmes ont été détectés. Suivez les instructions ci-dessous.",
        "status_failed": "La vérification du système n’a pas pu être terminée.",
        "technical_details": "DÉTAILS TECHNIQUES",
        "report_ready_title": "SYSTÈME PRÊT",
        "report_ready_line1": "Toutes les vérifications de compatibilité ont réussi.",
        "report_ready_line2": "Local Screen Translator est prêt à être utilisé.",
        "report_self_help_title": "LOCAL SCREEN TRANSLATOR - DIAGNOSTIC AUTONOME",
        "report_detected": "Détecté :",
        "report_how_to_fix": "Comment résoudre le problème :",
        "report_search_web": "Rechercher sur Internet :",
        "report_after_steps": "Après avoir effectué ces étapes, relancez la vérification du système.",
    },

    "it": {
        "system_check": "Controllo del sistema",
        "description": (
            "Controlla GPU, OCR, acquisizione dello schermo, modelli IA locali, "
            "allineamento del testo e sintesi vocale di Windows."
        ),
        "ready_to_check": "Pronto per il controllo.",
        "checking": (
            "Controllo della compatibilità del sistema. "
            "Il test dei modelli IA può richiedere un po’ di tempo..."
        ),
        "placeholder": "I risultati del controllo del sistema appariranno qui.",
        "run_again": "Controlla di nuovo",
        "copy_report": "Copia rapporto",
        "close": "Chiudi",
        "copied": "Copiato",
        "status_ready": "Sistema pronto — tutti i controlli di compatibilità sono stati superati.",
        "status_warnings": "Controllo del sistema completato con avvisi.",
        "status_problems": "Sono stati rilevati problemi. Segui le istruzioni qui sotto.",
        "status_failed": "Impossibile completare il controllo del sistema.",
        "technical_details": "DETTAGLI TECNICI",
        "report_ready_title": "SISTEMA PRONTO",
        "report_ready_line1": "Tutti i controlli di compatibilità sono stati superati.",
        "report_ready_line2": "Local Screen Translator è pronto per l’uso.",
        "report_self_help_title": "LOCAL SCREEN TRANSLATOR - DIAGNOSTICA AUTONOMA",
        "report_detected": "Rilevato:",
        "report_how_to_fix": "Come risolvere:",
        "report_search_web": "Cerca sul Web:",
        "report_after_steps": "Dopo aver completato questi passaggi, esegui nuovamente il controllo del sistema.",
    },

    "es-ES": {
        "system_check": "Comprobación del sistema",
        "description": (
            "Comprueba la GPU, OCR, captura de pantalla, modelos de IA locales, "
            "alineación de texto y síntesis de voz de Windows."
        ),
        "ready_to_check": "Listo para comprobar.",
        "checking": (
            "Comprobando la compatibilidad del sistema. "
            "La prueba de los modelos de IA puede tardar un poco..."
        ),
        "placeholder": "Los resultados de la comprobación aparecerán aquí.",
        "run_again": "Comprobar de nuevo",
        "copy_report": "Copiar informe",
        "close": "Cerrar",
        "copied": "Copiado",
        "status_ready": "Sistema listo — se superaron todas las comprobaciones de compatibilidad.",
        "status_warnings": "Comprobación del sistema completada con advertencias.",
        "status_problems": "Se encontraron problemas. Sigue las instrucciones siguientes.",
        "status_failed": "No se pudo completar la comprobación del sistema.",
        "technical_details": "DETALLES TÉCNICOS",
        "report_ready_title": "SISTEMA LISTO",
        "report_ready_line1": "Se superaron todas las comprobaciones de compatibilidad.",
        "report_ready_line2": "Local Screen Translator está listo para usar.",
        "report_self_help_title": "LOCAL SCREEN TRANSLATOR - DIAGNÓSTICO AUTÓNOMO",
        "report_detected": "Detectado:",
        "report_how_to_fix": "Cómo solucionarlo:",
        "report_search_web": "Buscar en Internet:",
        "report_after_steps": "Después de completar estos pasos, vuelve a ejecutar la comprobación del sistema.",
    },

    "es-US": {
        "system_check": "Comprobación del sistema",
        "description": (
            "Comprueba la GPU, OCR, captura de pantalla, modelos de IA locales, "
            "alineación de texto y voz de Windows."
        ),
        "ready_to_check": "Listo para comprobar.",
        "checking": (
            "Comprobando la compatibilidad del sistema. "
            "La prueba de los modelos de IA puede tardar un poco..."
        ),
        "placeholder": "Los resultados de la comprobación aparecerán aquí.",
        "run_again": "Comprobar de nuevo",
        "copy_report": "Copiar informe",
        "close": "Cerrar",
        "copied": "Copiado",
        "status_ready": "Sistema listo — se aprobaron todas las comprobaciones de compatibilidad.",
        "status_warnings": "Comprobación del sistema completada con advertencias.",
        "status_problems": "Se encontraron problemas. Sigue las instrucciones a continuación.",
        "status_failed": "No se pudo completar la comprobación del sistema.",
        "technical_details": "DETALLES TÉCNICOS",
        "report_ready_title": "SISTEMA LISTO",
        "report_ready_line1": "Se aprobaron todas las comprobaciones de compatibilidad.",
        "report_ready_line2": "Local Screen Translator está listo para usarse.",
        "report_self_help_title": "LOCAL SCREEN TRANSLATOR - DIAGNÓSTICO AUTÓNOMO",
        "report_detected": "Detectado:",
        "report_how_to_fix": "Cómo solucionarlo:",
        "report_search_web": "Buscar en Internet:",
        "report_after_steps": "Después de completar estos pasos, ejecuta nuevamente la comprobación del sistema.",
    },

    "pt-PT": {
        "system_check": "Verificação do sistema",
        "description": (
            "Verifica a GPU, OCR, captura de ecrã, modelos de IA locais, "
            "alinhamento de texto e síntese de voz do Windows."
        ),
        "ready_to_check": "Pronto para verificar.",
        "checking": (
            "A verificar a compatibilidade do sistema. "
            "O teste dos modelos de IA pode demorar algum tempo..."
        ),
        "placeholder": "Os resultados da verificação aparecerão aqui.",
        "run_again": "Verificar novamente",
        "copy_report": "Copiar relatório",
        "close": "Fechar",
        "copied": "Copiado",
        "status_ready": "Sistema pronto — todas as verificações de compatibilidade foram concluídas.",
        "status_warnings": "Verificação do sistema concluída com avisos.",
        "status_problems": "Foram encontrados problemas. Siga as instruções abaixo.",
        "status_failed": "Não foi possível concluir a verificação do sistema.",
        "technical_details": "DETALHES TÉCNICOS",
        "report_ready_title": "SISTEMA PRONTO",
        "report_ready_line1": "Todas as verificações de compatibilidade foram concluídas com sucesso.",
        "report_ready_line2": "O Local Screen Translator está pronto a utilizar.",
        "report_self_help_title": "LOCAL SCREEN TRANSLATOR - DIAGNÓSTICO AUTÓNOMO",
        "report_detected": "Detetado:",
        "report_how_to_fix": "Como corrigir:",
        "report_search_web": "Pesquisar na Internet:",
        "report_after_steps": "Depois de concluir estes passos, execute novamente a verificação do sistema.",
    },

    "pt-BR": {
        "system_check": "Verificação do sistema",
        "description": (
            "Verifica a GPU, OCR, captura de tela, modelos de IA locais, "
            "alinhamento de texto e síntese de voz do Windows."
        ),
        "ready_to_check": "Pronto para verificar.",
        "checking": (
            "Verificando a compatibilidade do sistema. "
            "O teste dos modelos de IA pode levar algum tempo..."
        ),
        "placeholder": "Os resultados da verificação aparecerão aqui.",
        "run_again": "Verificar novamente",
        "copy_report": "Copiar relatório",
        "close": "Fechar",
        "copied": "Copiado",
        "status_ready": "Sistema pronto — todas as verificações de compatibilidade foram concluídas.",
        "status_warnings": "Verificação do sistema concluída com avisos.",
        "status_problems": "Foram encontrados problemas. Siga as instruções abaixo.",
        "status_failed": "Não foi possível concluir a verificação do sistema.",
        "technical_details": "DETALHES TÉCNICOS",
        "report_ready_title": "SISTEMA PRONTO",
        "report_ready_line1": "Todas as verificações de compatibilidade foram concluídas com sucesso.",
        "report_ready_line2": "O Local Screen Translator está pronto para uso.",
        "report_self_help_title": "LOCAL SCREEN TRANSLATOR - DIAGNÓSTICO AUTÔNOMO",
        "report_detected": "Detectado:",
        "report_how_to_fix": "Como corrigir:",
        "report_search_web": "Pesquisar na Internet:",
        "report_after_steps": "Depois de concluir estas etapas, execute novamente a verificação do sistema.",
    },

    "pl": {
        "system_check": "Sprawdzanie systemu",
        "description": (
            "Sprawdza GPU, OCR, przechwytywanie ekranu, lokalne modele AI, "
            "wyrównywanie tekstu i syntezę mowy Windows."
        ),
        "ready_to_check": "Gotowe do sprawdzenia.",
        "checking": (
            "Sprawdzanie zgodności systemu. "
            "Test modeli AI może chwilę potrwać..."
        ),
        "placeholder": "Tutaj pojawią się wyniki sprawdzania systemu.",
        "run_again": "Sprawdź ponownie",
        "copy_report": "Kopiuj raport",
        "close": "Zamknij",
        "copied": "Skopiowano",
        "status_ready": "System gotowy — wszystkie testy zgodności zakończyły się powodzeniem.",
        "status_warnings": "Sprawdzanie systemu zakończono z ostrzeżeniami.",
        "status_problems": "Wykryto problemy. Wykonaj poniższe instrukcje.",
        "status_failed": "Nie udało się zakończyć sprawdzania systemu.",
        "technical_details": "SZCZEGÓŁY TECHNICZNE",
        "report_ready_title": "SYSTEM GOTOWY",
        "report_ready_line1": "Wszystkie testy zgodności zakończyły się powodzeniem.",
        "report_ready_line2": "Local Screen Translator jest gotowy do użycia.",
        "report_self_help_title": "LOCAL SCREEN TRANSLATOR - SAMODZIELNA DIAGNOSTYKA",
        "report_detected": "Wykryto:",
        "report_how_to_fix": "Jak naprawić:",
        "report_search_web": "Wyszukaj w Internecie:",
        "report_after_steps": "Po wykonaniu tych kroków uruchom ponownie sprawdzanie systemu.",
    },
})


# SYSTEM CHECK LANGUAGE BATCH 2
SC_TRANSLATIONS.update({
    "uk": {
        "system_check": "Перевірка системи",
        "description": (
            "Перевіряє GPU, OCR, захоплення екрана, локальні ШІ-моделі, "
            "вирівнювання тексту та синтез мовлення Windows."
        ),
        "ready_to_check": "Готово до перевірки.",
        "checking": (
            "Перевірка сумісності системи. "
            "Тест ШІ-моделей може зайняти деякий час..."
        ),
        "placeholder": "Тут з’являться результати перевірки системи.",
        "run_again": "Перевірити знову",
        "copy_report": "Копіювати звіт",
        "close": "Закрити",
        "copied": "Скопійовано",
        "status_ready": "Система готова — усі перевірки сумісності пройдено.",
        "status_warnings": "Перевірку системи завершено з попередженнями.",
        "status_problems": "Виявлено проблеми. Виконайте наведені нижче інструкції.",
        "status_failed": "Не вдалося завершити перевірку системи.",
        "technical_details": "ТЕХНІЧНІ ДАНІ",
        "report_ready_title": "СИСТЕМА ГОТОВА",
        "report_ready_line1": "Усі перевірки сумісності успішно пройдено.",
        "report_ready_line2": "Local Screen Translator готовий до роботи.",
        "report_self_help_title": "LOCAL SCREEN TRANSLATOR - САМОСТІЙНА ДІАГНОСТИКА",
        "report_detected": "Виявлено:",
        "report_how_to_fix": "Як виправити:",
        "report_search_web": "Для пошуку в Інтернеті:",
        "report_after_steps": "Після виконання цих дій знову запустіть Перевірку системи.",
    },

    "cs": {
        "system_check": "Kontrola systému",
        "description": (
            "Kontroluje GPU, OCR, zachytávání obrazovky, místní modely AI, "
            "zarovnání textu a syntézu řeči Windows."
        ),
        "ready_to_check": "Připraveno ke kontrole.",
        "checking": (
            "Kontrola kompatibility systému. "
            "Test modelů AI může chvíli trvat..."
        ),
        "placeholder": "Zde se zobrazí výsledky kontroly systému.",
        "run_again": "Zkontrolovat znovu",
        "copy_report": "Kopírovat zprávu",
        "close": "Zavřít",
        "copied": "Zkopírováno",
        "status_ready": "Systém je připraven — všechny kontroly kompatibility byly úspěšné.",
        "status_warnings": "Kontrola systému byla dokončena s upozorněními.",
        "status_problems": "Byly nalezeny problémy. Postupujte podle pokynů níže.",
        "status_failed": "Kontrolu systému se nepodařilo dokončit.",
        "technical_details": "TECHNICKÉ PODROBNOSTI",
        "report_ready_title": "SYSTÉM JE PŘIPRAVEN",
        "report_ready_line1": "Všechny kontroly kompatibility byly úspěšné.",
        "report_ready_line2": "Local Screen Translator je připraven k použití.",
        "report_self_help_title": "LOCAL SCREEN TRANSLATOR - SAMOSTATNÁ DIAGNOSTIKA",
        "report_detected": "Zjištěno:",
        "report_how_to_fix": "Jak problém vyřešit:",
        "report_search_web": "Vyhledat na Internetu:",
        "report_after_steps": "Po provedení těchto kroků spusťte kontrolu systému znovu.",
    },

    "sk": {
        "system_check": "Kontrola systému",
        "description": (
            "Kontroluje GPU, OCR, snímanie obrazovky, lokálne modely AI, "
            "zarovnanie textu a syntézu reči Windows."
        ),
        "ready_to_check": "Pripravené na kontrolu.",
        "checking": (
            "Kontrola kompatibility systému. "
            "Test modelov AI môže chvíľu trvať..."
        ),
        "placeholder": "Tu sa zobrazia výsledky kontroly systému.",
        "run_again": "Skontrolovať znova",
        "copy_report": "Kopírovať správu",
        "close": "Zavrieť",
        "copied": "Skopírované",
        "status_ready": "Systém je pripravený — všetky kontroly kompatibility boli úspešné.",
        "status_warnings": "Kontrola systému bola dokončená s upozorneniami.",
        "status_problems": "Boli nájdené problémy. Postupujte podľa pokynov nižšie.",
        "status_failed": "Kontrolu systému sa nepodarilo dokončiť.",
        "technical_details": "TECHNICKÉ PODROBNOSTI",
        "report_ready_title": "SYSTÉM JE PRIPRAVENÝ",
        "report_ready_line1": "Všetky kontroly kompatibility boli úspešné.",
        "report_ready_line2": "Local Screen Translator je pripravený na použitie.",
        "report_self_help_title": "LOCAL SCREEN TRANSLATOR - SAMOSTATNÁ DIAGNOSTIKA",
        "report_detected": "Zistené:",
        "report_how_to_fix": "Ako problém vyriešiť:",
        "report_search_web": "Vyhľadať na internete:",
        "report_after_steps": "Po vykonaní týchto krokov spustite kontrolu systému znova.",
    },

    "da": {
        "system_check": "Systemkontrol",
        "description": (
            "Kontrollerer GPU, OCR, skærmoptagelse, lokale AI-modeller, "
            "tekstjustering og Windows-talesyntese."
        ),
        "ready_to_check": "Klar til kontrol.",
        "checking": (
            "Kontrollerer systemkompatibilitet. "
            "Testen af AI-modeller kan tage lidt tid..."
        ),
        "placeholder": "Resultaterne af systemkontrollen vises her.",
        "run_again": "Kontroller igen",
        "copy_report": "Kopiér rapport",
        "close": "Luk",
        "copied": "Kopieret",
        "status_ready": "Systemet er klar — alle kompatibilitetskontroller er bestået.",
        "status_warnings": "Systemkontrollen blev gennemført med advarsler.",
        "status_problems": "Der blev fundet problemer. Følg instruktionerne nedenfor.",
        "status_failed": "Systemkontrollen kunne ikke gennemføres.",
        "technical_details": "TEKNISKE DETALJER",
        "report_ready_title": "SYSTEMET ER KLAR",
        "report_ready_line1": "Alle kompatibilitetskontroller blev gennemført korrekt.",
        "report_ready_line2": "Local Screen Translator er klar til brug.",
        "report_self_help_title": "LOCAL SCREEN TRANSLATOR - SELVHJÆLPSDIAGNOSTIK",
        "report_detected": "Registreret:",
        "report_how_to_fix": "Sådan løses problemet:",
        "report_search_web": "Søg på internettet efter:",
        "report_after_steps": "Kør systemkontrollen igen, når disse trin er udført.",
    },

    "fi": {
        "system_check": "Järjestelmän tarkistus",
        "description": (
            "Tarkistaa GPU:n, OCR:n, näytönkaappauksen, paikalliset AI-mallit, "
            "tekstin kohdistuksen ja Windowsin puhesynteesin."
        ),
        "ready_to_check": "Valmis tarkistukseen.",
        "checking": (
            "Tarkistetaan järjestelmän yhteensopivuutta. "
            "AI-mallien testi voi kestää hetken..."
        ),
        "placeholder": "Järjestelmän tarkistuksen tulokset näkyvät tässä.",
        "run_again": "Tarkista uudelleen",
        "copy_report": "Kopioi raportti",
        "close": "Sulje",
        "copied": "Kopioitu",
        "status_ready": "Järjestelmä on valmis — kaikki yhteensopivuustarkistukset läpäistiin.",
        "status_warnings": "Järjestelmän tarkistus valmistui varoituksin.",
        "status_problems": "Ongelmia havaittiin. Noudata alla olevia ohjeita.",
        "status_failed": "Järjestelmän tarkistusta ei voitu suorittaa loppuun.",
        "technical_details": "TEKNISET TIEDOT",
        "report_ready_title": "JÄRJESTELMÄ ON VALMIS",
        "report_ready_line1": "Kaikki yhteensopivuustarkistukset läpäistiin onnistuneesti.",
        "report_ready_line2": "Local Screen Translator on käyttövalmis.",
        "report_self_help_title": "LOCAL SCREEN TRANSLATOR - OMATOIMINEN VIANMÄÄRITYS",
        "report_detected": "Havaittu:",
        "report_how_to_fix": "Korjausohje:",
        "report_search_web": "Hae Internetistä:",
        "report_after_steps": "Kun olet suorittanut nämä vaiheet, käynnistä järjestelmän tarkistus uudelleen.",
    },

    "sv": {
        "system_check": "Systemkontroll",
        "description": (
            "Kontrollerar GPU, OCR, skärminspelning, lokala AI-modeller, "
            "textjustering och Windows talsyntes."
        ),
        "ready_to_check": "Redo att kontrollera.",
        "checking": (
            "Kontrollerar systemkompatibiliteten. "
            "Testet av AI-modeller kan ta en stund..."
        ),
        "placeholder": "Resultaten från systemkontrollen visas här.",
        "run_again": "Kontrollera igen",
        "copy_report": "Kopiera rapport",
        "close": "Stäng",
        "copied": "Kopierat",
        "status_ready": "Systemet är klart — alla kompatibilitetskontroller godkändes.",
        "status_warnings": "Systemkontrollen slutfördes med varningar.",
        "status_problems": "Problem hittades. Följ instruktionerna nedan.",
        "status_failed": "Systemkontrollen kunde inte slutföras.",
        "technical_details": "TEKNISKA DETALJER",
        "report_ready_title": "SYSTEMET ÄR KLART",
        "report_ready_line1": "Alla kompatibilitetskontroller genomfördes utan fel.",
        "report_ready_line2": "Local Screen Translator är redo att användas.",
        "report_self_help_title": "LOCAL SCREEN TRANSLATOR - SJÄLVHJÄLPSDIAGNOSTIK",
        "report_detected": "Upptäckt:",
        "report_how_to_fix": "Så här löser du problemet:",
        "report_search_web": "Sök på Internet efter:",
        "report_after_steps": "Kör systemkontrollen igen efter att du har utfört dessa steg.",
    },

    "no": {
        "system_check": "Systemkontroll",
        "description": (
            "Kontrollerer GPU, OCR, skjermopptak, lokale AI-modeller, "
            "tekstjustering og Windows talesyntese."
        ),
        "ready_to_check": "Klar til kontroll.",
        "checking": (
            "Kontrollerer systemkompatibiliteten. "
            "Testen av AI-modeller kan ta litt tid..."
        ),
        "placeholder": "Resultatene fra systemkontrollen vises her.",
        "run_again": "Kontroller på nytt",
        "copy_report": "Kopier rapport",
        "close": "Lukk",
        "copied": "Kopiert",
        "status_ready": "Systemet er klart — alle kompatibilitetskontroller ble bestått.",
        "status_warnings": "Systemkontrollen ble fullført med advarsler.",
        "status_problems": "Det ble funnet problemer. Følg instruksjonene nedenfor.",
        "status_failed": "Systemkontrollen kunne ikke fullføres.",
        "technical_details": "TEKNISKE DETALJER",
        "report_ready_title": "SYSTEMET ER KLART",
        "report_ready_line1": "Alle kompatibilitetskontroller ble fullført uten feil.",
        "report_ready_line2": "Local Screen Translator er klar til bruk.",
        "report_self_help_title": "LOCAL SCREEN TRANSLATOR - SELVHJELPSDIAGNOSTIKK",
        "report_detected": "Oppdaget:",
        "report_how_to_fix": "Slik løser du problemet:",
        "report_search_web": "Søk på Internett etter:",
        "report_after_steps": "Kjør systemkontrollen på nytt etter at disse trinnene er utført.",
    },

    "nl": {
        "system_check": "Systeemcontrole",
        "description": (
            "Controleert GPU, OCR, schermopname, lokale AI-modellen, "
            "tekstuitlijning en Windows-spraaksynthese."
        ),
        "ready_to_check": "Klaar voor controle.",
        "checking": (
            "Systeemcompatibiliteit wordt gecontroleerd. "
            "De test van de AI-modellen kan even duren..."
        ),
        "placeholder": "De resultaten van de systeemcontrole verschijnen hier.",
        "run_again": "Opnieuw controleren",
        "copy_report": "Rapport kopiëren",
        "close": "Sluiten",
        "copied": "Gekopieerd",
        "status_ready": "Systeem gereed — alle compatibiliteitscontroles zijn geslaagd.",
        "status_warnings": "Systeemcontrole voltooid met waarschuwingen.",
        "status_problems": "Er zijn problemen gevonden. Volg de onderstaande instructies.",
        "status_failed": "De systeemcontrole kon niet worden voltooid.",
        "technical_details": "TECHNISCHE DETAILS",
        "report_ready_title": "SYSTEEM GEREED",
        "report_ready_line1": "Alle compatibiliteitscontroles zijn succesvol uitgevoerd.",
        "report_ready_line2": "Local Screen Translator is klaar voor gebruik.",
        "report_self_help_title": "LOCAL SCREEN TRANSLATOR - ZELFHULPDIAGNOSE",
        "report_detected": "Gedetecteerd:",
        "report_how_to_fix": "Hoe dit op te lossen:",
        "report_search_web": "Zoek op Internet naar:",
        "report_after_steps": "Voer de systeemcontrole opnieuw uit nadat deze stappen zijn voltooid.",
    },
})


# SYSTEM CHECK LANGUAGE BATCH 3
SC_TRANSLATIONS.update({
    "el": {
        "system_check": "Έλεγχος συστήματος",
        "description": (
            "Ελέγχει GPU, OCR, καταγραφή οθόνης, τοπικά μοντέλα AI, "
            "στοίχιση κειμένου και σύνθεση ομιλίας των Windows."
        ),
        "ready_to_check": "Έτοιμο για έλεγχο.",
        "checking": (
            "Έλεγχος συμβατότητας συστήματος. "
            "Η δοκιμή των μοντέλων AI μπορεί να διαρκέσει λίγο..."
        ),
        "placeholder": "Τα αποτελέσματα του ελέγχου θα εμφανιστούν εδώ.",
        "run_again": "Έλεγχος ξανά",
        "copy_report": "Αντιγραφή αναφοράς",
        "close": "Κλείσιμο",
        "copied": "Αντιγράφηκε",
        "status_ready": "Το σύστημα είναι έτοιμο — όλοι οι έλεγχοι συμβατότητας ολοκληρώθηκαν.",
        "status_warnings": "Ο έλεγχος συστήματος ολοκληρώθηκε με προειδοποιήσεις.",
        "status_problems": "Βρέθηκαν προβλήματα. Ακολουθήστε τις παρακάτω οδηγίες.",
        "status_failed": "Δεν ήταν δυνατή η ολοκλήρωση του ελέγχου συστήματος.",
        "technical_details": "ΤΕΧΝΙΚΕΣ ΛΕΠΤΟΜΕΡΕΙΕΣ",
        "report_ready_title": "ΤΟ ΣΥΣΤΗΜΑ ΕΙΝΑΙ ΕΤΟΙΜΟ",
        "report_ready_line1": "Όλοι οι έλεγχοι συμβατότητας ολοκληρώθηκαν με επιτυχία.",
        "report_ready_line2": "Το Local Screen Translator είναι έτοιμο για χρήση.",
        "report_self_help_title": "LOCAL SCREEN TRANSLATOR - ΑΥΤΟΝΟΜΗ ΔΙΑΓΝΩΣΗ",
        "report_detected": "Εντοπίστηκε:",
        "report_how_to_fix": "Τρόπος επίλυσης:",
        "report_search_web": "Αναζήτηση στο Internet:",
        "report_after_steps": "Μετά την ολοκλήρωση αυτών των βημάτων, εκτελέστε ξανά τον έλεγχο συστήματος.",
    },

    "hu": {
        "system_check": "Rendszerellenőrzés",
        "description": (
            "Ellenőrzi a GPU-t, az OCR-t, a képernyőrögzítést, a helyi AI-modelleket, "
            "a szövegillesztést és a Windows beszédszintézisét."
        ),
        "ready_to_check": "Ellenőrzésre kész.",
        "checking": (
            "A rendszer kompatibilitásának ellenőrzése. "
            "Az AI-modellek tesztje eltarthat egy ideig..."
        ),
        "placeholder": "A rendszerellenőrzés eredményei itt jelennek meg.",
        "run_again": "Ellenőrzés újra",
        "copy_report": "Jelentés másolása",
        "close": "Bezárás",
        "copied": "Másolva",
        "status_ready": "A rendszer kész — minden kompatibilitási ellenőrzés sikeres.",
        "status_warnings": "A rendszerellenőrzés figyelmeztetésekkel fejeződött be.",
        "status_problems": "Problémákat találtunk. Kövesse az alábbi utasításokat.",
        "status_failed": "A rendszerellenőrzést nem sikerült befejezni.",
        "technical_details": "TECHNIKAI RÉSZLETEK",
        "report_ready_title": "A RENDSZER KÉSZ",
        "report_ready_line1": "Minden kompatibilitási ellenőrzés sikeresen befejeződött.",
        "report_ready_line2": "A Local Screen Translator használatra kész.",
        "report_self_help_title": "LOCAL SCREEN TRANSLATOR - ÖNÁLLÓ DIAGNOSZTIKA",
        "report_detected": "Észlelve:",
        "report_how_to_fix": "Megoldás:",
        "report_search_web": "Keresés az interneten:",
        "report_after_steps": "A lépések végrehajtása után futtassa újra a rendszerellenőrzést.",
    },

    "ro": {
        "system_check": "Verificarea sistemului",
        "description": (
            "Verifică GPU, OCR, capturarea ecranului, modelele AI locale, "
            "alinierea textului și sinteza vocală Windows."
        ),
        "ready_to_check": "Pregătit pentru verificare.",
        "checking": (
            "Se verifică compatibilitatea sistemului. "
            "Testarea modelelor AI poate dura puțin..."
        ),
        "placeholder": "Rezultatele verificării sistemului vor apărea aici.",
        "run_again": "Verifică din nou",
        "copy_report": "Copiază raportul",
        "close": "Închide",
        "copied": "Copiat",
        "status_ready": "Sistemul este pregătit — toate verificările de compatibilitate au reușit.",
        "status_warnings": "Verificarea sistemului s-a încheiat cu avertismente.",
        "status_problems": "Au fost detectate probleme. Urmați instrucțiunile de mai jos.",
        "status_failed": "Verificarea sistemului nu a putut fi finalizată.",
        "technical_details": "DETALII TEHNICE",
        "report_ready_title": "SISTEMUL ESTE PREGĂTIT",
        "report_ready_line1": "Toate verificările de compatibilitate au fost finalizate cu succes.",
        "report_ready_line2": "Local Screen Translator este gata de utilizare.",
        "report_self_help_title": "LOCAL SCREEN TRANSLATOR - DIAGNOSTIC AUTONOM",
        "report_detected": "Detectat:",
        "report_how_to_fix": "Cum se rezolvă:",
        "report_search_web": "Căutați pe Internet:",
        "report_after_steps": "După efectuarea acestor pași, rulați din nou verificarea sistemului.",
    },

    "lt": {
        "system_check": "Sistemos patikra",
        "description": (
            "Tikrina GPU, OCR, ekrano fiksavimą, vietinius AI modelius, "
            "teksto lygiavimą ir Windows kalbos sintezę."
        ),
        "ready_to_check": "Paruošta tikrinimui.",
        "checking": (
            "Tikrinamas sistemos suderinamumas. "
            "AI modelių testas gali šiek tiek užtrukti..."
        ),
        "placeholder": "Sistemos patikros rezultatai bus rodomi čia.",
        "run_again": "Tikrinti dar kartą",
        "copy_report": "Kopijuoti ataskaitą",
        "close": "Uždaryti",
        "copied": "Nukopijuota",
        "status_ready": "Sistema paruošta — visos suderinamumo patikros sėkmingos.",
        "status_warnings": "Sistemos patikra baigta su įspėjimais.",
        "status_problems": "Aptikta problemų. Vykdykite toliau pateiktas instrukcijas.",
        "status_failed": "Nepavyko užbaigti sistemos patikros.",
        "technical_details": "TECHNINĖ INFORMACIJA",
        "report_ready_title": "SISTEMA PARUOŠTA",
        "report_ready_line1": "Visos suderinamumo patikros sėkmingai užbaigtos.",
        "report_ready_line2": "Local Screen Translator paruoštas naudoti.",
        "report_self_help_title": "LOCAL SCREEN TRANSLATOR - SAVARANKIŠKA DIAGNOSTIKA",
        "report_detected": "Aptikta:",
        "report_how_to_fix": "Kaip išspręsti:",
        "report_search_web": "Ieškoti internete:",
        "report_after_steps": "Atlikę šiuos veiksmus, dar kartą paleiskite sistemos patikrą.",
    },

    "lv": {
        "system_check": "Sistēmas pārbaude",
        "description": (
            "Pārbauda GPU, OCR, ekrāna uztveršanu, lokālos AI modeļus, "
            "teksta izlīdzināšanu un Windows runas sintēzi."
        ),
        "ready_to_check": "Gatavs pārbaudei.",
        "checking": (
            "Tiek pārbaudīta sistēmas saderība. "
            "AI modeļu pārbaude var aizņemt kādu laiku..."
        ),
        "placeholder": "Sistēmas pārbaudes rezultāti parādīsies šeit.",
        "run_again": "Pārbaudīt vēlreiz",
        "copy_report": "Kopēt pārskatu",
        "close": "Aizvērt",
        "copied": "Nokopēts",
        "status_ready": "Sistēma ir gatava — visas saderības pārbaudes ir veiksmīgas.",
        "status_warnings": "Sistēmas pārbaude pabeigta ar brīdinājumiem.",
        "status_problems": "Atrastas problēmas. Izpildiet tālāk sniegtos norādījumus.",
        "status_failed": "Sistēmas pārbaudi neizdevās pabeigt.",
        "technical_details": "TEHNISKĀ INFORMĀCIJA",
        "report_ready_title": "SISTĒMA IR GATAVA",
        "report_ready_line1": "Visas saderības pārbaudes ir veiksmīgi pabeigtas.",
        "report_ready_line2": "Local Screen Translator ir gatavs lietošanai.",
        "report_self_help_title": "LOCAL SCREEN TRANSLATOR - PAŠDIAGNOSTIKA",
        "report_detected": "Konstatēts:",
        "report_how_to_fix": "Kā novērst:",
        "report_search_web": "Meklēt internetā:",
        "report_after_steps": "Pēc šo darbību veikšanas vēlreiz palaidiet sistēmas pārbaudi.",
    },

    "et": {
        "system_check": "Süsteemi kontroll",
        "description": (
            "Kontrollib GPU-d, OCR-i, ekraanipüüdmist, kohalikke AI-mudeleid, "
            "teksti joondamist ja Windowsi kõnesünteesi."
        ),
        "ready_to_check": "Kontrollimiseks valmis.",
        "checking": (
            "Kontrollitakse süsteemi ühilduvust. "
            "AI-mudelite test võib veidi aega võtta..."
        ),
        "placeholder": "Süsteemikontrolli tulemused kuvatakse siin.",
        "run_again": "Kontrolli uuesti",
        "copy_report": "Kopeeri aruanne",
        "close": "Sulge",
        "copied": "Kopeeritud",
        "status_ready": "Süsteem on valmis — kõik ühilduvuskontrollid õnnestusid.",
        "status_warnings": "Süsteemikontroll lõppes hoiatustega.",
        "status_problems": "Leiti probleeme. Järgige allolevaid juhiseid.",
        "status_failed": "Süsteemikontrolli ei õnnestunud lõpetada.",
        "technical_details": "TEHNILISED ANDMED",
        "report_ready_title": "SÜSTEEM ON VALMIS",
        "report_ready_line1": "Kõik ühilduvuskontrollid lõpetati edukalt.",
        "report_ready_line2": "Local Screen Translator on kasutamiseks valmis.",
        "report_self_help_title": "LOCAL SCREEN TRANSLATOR - ISESEISEV DIAGNOSTIKA",
        "report_detected": "Tuvastatud:",
        "report_how_to_fix": "Kuidas parandada:",
        "report_search_web": "Otsi Internetist:",
        "report_after_steps": "Pärast nende toimingute tegemist käivitage süsteemikontroll uuesti.",
    },

    "sl": {
        "system_check": "Preverjanje sistema",
        "description": (
            "Preverja GPU, OCR, zajem zaslona, lokalne modele AI, "
            "poravnavo besedila in sintezo govora Windows."
        ),
        "ready_to_check": "Pripravljeno za preverjanje.",
        "checking": (
            "Preverjanje združljivosti sistema. "
            "Preizkus modelov AI lahko traja nekaj časa..."
        ),
        "placeholder": "Rezultati preverjanja sistema bodo prikazani tukaj.",
        "run_again": "Preveri znova",
        "copy_report": "Kopiraj poročilo",
        "close": "Zapri",
        "copied": "Kopirano",
        "status_ready": "Sistem je pripravljen — vsa preverjanja združljivosti so bila uspešna.",
        "status_warnings": "Preverjanje sistema je bilo zaključeno z opozorili.",
        "status_problems": "Najdene so bile težave. Sledite spodnjim navodilom.",
        "status_failed": "Preverjanja sistema ni bilo mogoče dokončati.",
        "technical_details": "TEHNIČNE PODROBNOSTI",
        "report_ready_title": "SISTEM JE PRIPRAVLJEN",
        "report_ready_line1": "Vsa preverjanja združljivosti so bila uspešno zaključena.",
        "report_ready_line2": "Local Screen Translator je pripravljen za uporabo.",
        "report_self_help_title": "LOCAL SCREEN TRANSLATOR - SAMOSTOJNA DIAGNOSTIKA",
        "report_detected": "Zaznano:",
        "report_how_to_fix": "Kako odpraviti:",
        "report_search_web": "Poiščite v internetu:",
        "report_after_steps": "Po izvedbi teh korakov znova zaženite preverjanje sistema.",
    },

    "bg": {
        "system_check": "Проверка на системата",
        "description": (
            "Проверява GPU, OCR, заснемане на екрана, локални AI модели, "
            "подравняване на текст и синтез на реч в Windows."
        ),
        "ready_to_check": "Готово за проверка.",
        "checking": (
            "Проверка на съвместимостта на системата. "
            "Тестът на AI моделите може да отнеме известно време..."
        ),
        "placeholder": "Резултатите от проверката ще се покажат тук.",
        "run_again": "Провери отново",
        "copy_report": "Копирай отчета",
        "close": "Затвори",
        "copied": "Копирано",
        "status_ready": "Системата е готова — всички проверки за съвместимост са успешни.",
        "status_warnings": "Проверката на системата приключи с предупреждения.",
        "status_problems": "Открити са проблеми. Следвайте инструкциите по-долу.",
        "status_failed": "Проверката на системата не можа да бъде завършена.",
        "technical_details": "ТЕХНИЧЕСКИ ДАННИ",
        "report_ready_title": "СИСТЕМАТА Е ГОТОВА",
        "report_ready_line1": "Всички проверки за съвместимост приключиха успешно.",
        "report_ready_line2": "Local Screen Translator е готов за използване.",
        "report_self_help_title": "LOCAL SCREEN TRANSLATOR - САМОСТОЯТЕЛНА ДИАГНОСТИКА",
        "report_detected": "Открито:",
        "report_how_to_fix": "Как да се поправи:",
        "report_search_web": "Търсене в интернет:",
        "report_after_steps": "След като изпълните тези стъпки, стартирайте проверката на системата отново.",
    },
})


# SYSTEM CHECK LANGUAGE BATCH 4A
SC_TRANSLATIONS.update({
    "hr": {
        "system_check": "Provjera sustava",
        "description": (
            "Provjerava GPU, OCR, snimanje zaslona, lokalne AI modele, "
            "poravnanje teksta i Windows sintezu govora."
        ),
        "ready_to_check": "Spremno za provjeru.",
        "checking": (
            "Provjera kompatibilnosti sustava. "
            "Test AI modela može potrajati..."
        ),
        "placeholder": "Rezultati provjere sustava pojavit će se ovdje.",
        "run_again": "Provjeri ponovno",
        "copy_report": "Kopiraj izvješće",
        "close": "Zatvori",
        "copied": "Kopirano",
        "status_ready": "Sustav je spreman — sve provjere kompatibilnosti su uspješne.",
        "status_warnings": "Provjera sustava završena je s upozorenjima.",
        "status_problems": "Pronađeni su problemi. Slijedite upute u nastavku.",
        "status_failed": "Provjera sustava nije mogla biti dovršena.",
        "technical_details": "TEHNIČKI DETALJI",
        "report_ready_title": "SUSTAV JE SPREMAN",
        "report_ready_line1": "Sve provjere kompatibilnosti uspješno su završene.",
        "report_ready_line2": "Local Screen Translator spreman je za korištenje.",
        "report_self_help_title": "LOCAL SCREEN TRANSLATOR - SAMOSTALNA DIJAGNOSTIKA",
        "report_detected": "Otkriveno:",
        "report_how_to_fix": "Kako riješiti:",
        "report_search_web": "Pretražite Internet:",
        "report_after_steps": "Nakon ovih koraka ponovno pokrenite provjeru sustava.",
    },

    "tr": {
        "system_check": "Sistem Kontrolü",
        "description": (
            "GPU, OCR, ekran yakalama, yerel AI modelleri, "
            "metin hizalama ve Windows konuşma sentezini kontrol eder."
        ),
        "ready_to_check": "Kontrole hazır.",
        "checking": (
            "Sistem uyumluluğu kontrol ediliyor. "
            "AI modeli testi biraz zaman alabilir..."
        ),
        "placeholder": "Sistem kontrolü sonuçları burada görünecek.",
        "run_again": "Tekrar kontrol et",
        "copy_report": "Raporu kopyala",
        "close": "Kapat",
        "copied": "Kopyalandı",
        "status_ready": "Sistem hazır — tüm uyumluluk kontrolleri başarıyla tamamlandı.",
        "status_warnings": "Sistem kontrolü uyarılarla tamamlandı.",
        "status_problems": "Sorunlar bulundu. Aşağıdaki talimatları uygulayın.",
        "status_failed": "Sistem kontrolü tamamlanamadı.",
        "technical_details": "TEKNİK AYRINTILAR",
        "report_ready_title": "SİSTEM HAZIR",
        "report_ready_line1": "Tüm uyumluluk kontrolleri başarıyla tamamlandı.",
        "report_ready_line2": "Local Screen Translator kullanıma hazır.",
        "report_self_help_title": "LOCAL SCREEN TRANSLATOR - KENDİ KENDİNE TANI",
        "report_detected": "Algılandı:",
        "report_how_to_fix": "Nasıl düzeltilir:",
        "report_search_web": "İnternette ara:",
        "report_after_steps": "Bu adımları tamamladıktan sonra Sistem Kontrolünü tekrar çalıştırın.",
    },

    "ar": {
        "system_check": "فحص النظام",
        "description": (
            "يفحص بطاقة الرسومات وOCR والتقاط الشاشة ونماذج الذكاء الاصطناعي المحلية "
            "ومحاذاة النص وتحويل النص إلى كلام في Windows."
        ),
        "ready_to_check": "جاهز للفحص.",
        "checking": (
            "جارٍ فحص توافق النظام. "
            "قد يستغرق اختبار نماذج الذكاء الاصطناعي بعض الوقت..."
        ),
        "placeholder": "ستظهر نتائج فحص النظام هنا.",
        "run_again": "إعادة الفحص",
        "copy_report": "نسخ التقرير",
        "close": "إغلاق",
        "copied": "تم النسخ",
        "status_ready": "النظام جاهز — اجتازت جميع اختبارات التوافق.",
        "status_warnings": "اكتمل فحص النظام مع وجود تحذيرات.",
        "status_problems": "تم العثور على مشكلات. اتبع التعليمات أدناه.",
        "status_failed": "تعذر إكمال فحص النظام.",
        "technical_details": "التفاصيل التقنية",
        "report_ready_title": "النظام جاهز",
        "report_ready_line1": "تم اجتياز جميع اختبارات التوافق بنجاح.",
        "report_ready_line2": "Local Screen Translator جاهز للاستخدام.",
        "report_self_help_title": "LOCAL SCREEN TRANSLATOR - التشخيص الذاتي",
        "report_detected": "تم اكتشاف:",
        "report_how_to_fix": "طريقة الإصلاح:",
        "report_search_web": "ابحث على الإنترنت عن:",
        "report_after_steps": "بعد تنفيذ هذه الخطوات، شغّل فحص النظام مرة أخرى.",
    },

    "hi": {
        "system_check": "सिस्टम जाँच",
        "description": (
            "GPU, OCR, स्क्रीन कैप्चर, स्थानीय AI मॉडल, "
            "टेक्स्ट अलाइनमेंट और Windows स्पीच सिंथेसिस की जाँच करता है।"
        ),
        "ready_to_check": "जाँच के लिए तैयार।",
        "checking": (
            "सिस्टम संगतता की जाँच की जा रही है। "
            "AI मॉडल परीक्षण में थोड़ा समय लग सकता है..."
        ),
        "placeholder": "सिस्टम जाँच के परिणाम यहाँ दिखाई देंगे।",
        "run_again": "फिर से जाँचें",
        "copy_report": "रिपोर्ट कॉपी करें",
        "close": "बंद करें",
        "copied": "कॉपी किया गया",
        "status_ready": "सिस्टम तैयार है — सभी संगतता जाँच सफल रहीं।",
        "status_warnings": "सिस्टम जाँच चेतावनियों के साथ पूरी हुई।",
        "status_problems": "समस्याएँ मिलीं। नीचे दिए गए निर्देशों का पालन करें।",
        "status_failed": "सिस्टम जाँच पूरी नहीं हो सकी।",
        "technical_details": "तकनीकी विवरण",
        "report_ready_title": "सिस्टम तैयार है",
        "report_ready_line1": "सभी संगतता जाँच सफलतापूर्वक पूरी हुईं।",
        "report_ready_line2": "Local Screen Translator उपयोग के लिए तैयार है।",
        "report_self_help_title": "LOCAL SCREEN TRANSLATOR - स्व-सहायता निदान",
        "report_detected": "पता चला:",
        "report_how_to_fix": "कैसे ठीक करें:",
        "report_search_web": "इंटरनेट पर खोजें:",
        "report_after_steps": "इन चरणों को पूरा करने के बाद सिस्टम जाँच फिर से चलाएँ।",
    },

    "vi": {
        "system_check": "Kiểm tra hệ thống",
        "description": (
            "Kiểm tra GPU, OCR, chụp màn hình, mô hình AI cục bộ, "
            "căn chỉnh văn bản và tổng hợp giọng nói Windows."
        ),
        "ready_to_check": "Sẵn sàng kiểm tra.",
        "checking": (
            "Đang kiểm tra khả năng tương thích của hệ thống. "
            "Kiểm tra mô hình AI có thể mất một chút thời gian..."
        ),
        "placeholder": "Kết quả kiểm tra hệ thống sẽ xuất hiện ở đây.",
        "run_again": "Kiểm tra lại",
        "copy_report": "Sao chép báo cáo",
        "close": "Đóng",
        "copied": "Đã sao chép",
        "status_ready": "Hệ thống đã sẵn sàng — tất cả kiểm tra tương thích đều thành công.",
        "status_warnings": "Kiểm tra hệ thống hoàn tất với cảnh báo.",
        "status_problems": "Đã phát hiện sự cố. Hãy làm theo hướng dẫn bên dưới.",
        "status_failed": "Không thể hoàn tất kiểm tra hệ thống.",
        "technical_details": "CHI TIẾT KỸ THUẬT",
        "report_ready_title": "HỆ THỐNG ĐÃ SẴN SÀNG",
        "report_ready_line1": "Tất cả kiểm tra tương thích đã hoàn tất thành công.",
        "report_ready_line2": "Local Screen Translator đã sẵn sàng để sử dụng.",
        "report_self_help_title": "LOCAL SCREEN TRANSLATOR - CHẨN ĐOÁN TỰ PHỤC VỤ",
        "report_detected": "Phát hiện:",
        "report_how_to_fix": "Cách khắc phục:",
        "report_search_web": "Tìm kiếm trên Internet:",
        "report_after_steps": "Sau khi hoàn thành các bước này, hãy chạy lại Kiểm tra hệ thống.",
    },

    "id": {
        "system_check": "Pemeriksaan Sistem",
        "description": (
            "Memeriksa GPU, OCR, tangkapan layar, model AI lokal, "
            "penyelarasan teks, dan sintesis suara Windows."
        ),
        "ready_to_check": "Siap diperiksa.",
        "checking": (
            "Memeriksa kompatibilitas sistem. "
            "Pengujian model AI mungkin memerlukan sedikit waktu..."
        ),
        "placeholder": "Hasil Pemeriksaan Sistem akan muncul di sini.",
        "run_again": "Periksa lagi",
        "copy_report": "Salin laporan",
        "close": "Tutup",
        "copied": "Disalin",
        "status_ready": "Sistem siap — semua pemeriksaan kompatibilitas berhasil.",
        "status_warnings": "Pemeriksaan sistem selesai dengan peringatan.",
        "status_problems": "Masalah ditemukan. Ikuti petunjuk di bawah.",
        "status_failed": "Pemeriksaan sistem tidak dapat diselesaikan.",
        "technical_details": "DETAIL TEKNIS",
        "report_ready_title": "SISTEM SIAP",
        "report_ready_line1": "Semua pemeriksaan kompatibilitas berhasil diselesaikan.",
        "report_ready_line2": "Local Screen Translator siap digunakan.",
        "report_self_help_title": "LOCAL SCREEN TRANSLATOR - DIAGNOSIS MANDIRI",
        "report_detected": "Terdeteksi:",
        "report_how_to_fix": "Cara memperbaiki:",
        "report_search_web": "Cari di Internet:",
        "report_after_steps": "Setelah menyelesaikan langkah-langkah ini, jalankan Pemeriksaan Sistem lagi.",
    },
})


# SYSTEM CHECK LANGUAGE BATCH 4B
SC_TRANSLATIONS.update({
    "th": {
        "system_check": "ตรวจสอบระบบ",
        "description": (
            "ตรวจสอบ GPU, OCR, การจับภาพหน้าจอ, โมเดล AI ภายในเครื่อง, "
            "การจัดแนวข้อความ และการสังเคราะห์เสียงของ Windows"
        ),
        "ready_to_check": "พร้อมตรวจสอบ",
        "checking": (
            "กำลังตรวจสอบความเข้ากันได้ของระบบ "
            "การทดสอบโมเดล AI อาจใช้เวลาสักครู่..."
        ),
        "placeholder": "ผลการตรวจสอบระบบจะแสดงที่นี่",
        "run_again": "ตรวจสอบอีกครั้ง",
        "copy_report": "คัดลอกรายงาน",
        "close": "ปิด",
        "copied": "คัดลอกแล้ว",
        "status_ready": "ระบบพร้อมใช้งาน — ผ่านการตรวจสอบความเข้ากันได้ทั้งหมดแล้ว",
        "status_warnings": "การตรวจสอบระบบเสร็จสิ้นพร้อมคำเตือน",
        "status_problems": "พบปัญหา โปรดทำตามคำแนะนำด้านล่าง",
        "status_failed": "ไม่สามารถตรวจสอบระบบให้เสร็จสมบูรณ์ได้",
        "technical_details": "รายละเอียดทางเทคนิค",
        "report_ready_title": "ระบบพร้อมใช้งาน",
        "report_ready_line1": "ผ่านการตรวจสอบความเข้ากันได้ทั้งหมดเรียบร้อยแล้ว",
        "report_ready_line2": "Local Screen Translator พร้อมใช้งานแล้ว",
        "report_self_help_title": "LOCAL SCREEN TRANSLATOR - การวินิจฉัยด้วยตนเอง",
        "report_detected": "ตรวจพบ:",
        "report_how_to_fix": "วิธีแก้ไข:",
        "report_search_web": "ค้นหาบนอินเทอร์เน็ต:",
        "report_after_steps": "หลังจากทำตามขั้นตอนเหล่านี้แล้ว ให้เรียกใช้การตรวจสอบระบบอีกครั้ง",
    },

    "zh-CN": {
        "system_check": "系统检查",
        "description": (
            "检查 GPU、OCR、屏幕捕获、本地 AI 模型、"
            "文本对齐以及 Windows 语音合成。"
        ),
        "ready_to_check": "已准备好检查。",
        "checking": (
            "正在检查系统兼容性。"
            "AI 模型测试可能需要一些时间..."
        ),
        "placeholder": "系统检查结果将显示在这里。",
        "run_again": "重新检查",
        "copy_report": "复制报告",
        "close": "关闭",
        "copied": "已复制",
        "status_ready": "系统已就绪 — 所有兼容性检查均已通过。",
        "status_warnings": "系统检查已完成，但存在警告。",
        "status_problems": "发现问题。请按照下面的说明操作。",
        "status_failed": "无法完成系统检查。",
        "technical_details": "技术详细信息",
        "report_ready_title": "系统已就绪",
        "report_ready_line1": "所有兼容性检查均已成功通过。",
        "report_ready_line2": "Local Screen Translator 已准备好使用。",
        "report_self_help_title": "LOCAL SCREEN TRANSLATOR - 自助诊断",
        "report_detected": "检测到:",
        "report_how_to_fix": "解决方法:",
        "report_search_web": "在互联网上搜索:",
        "report_after_steps": "完成这些步骤后，请再次运行系统检查。",
    },

    "zh-TW": {
        "system_check": "系統檢查",
        "description": (
            "檢查 GPU、OCR、螢幕擷取、本機 AI 模型、"
            "文字對齊以及 Windows 語音合成。"
        ),
        "ready_to_check": "已準備好檢查。",
        "checking": (
            "正在檢查系統相容性。"
            "AI 模型測試可能需要一些時間..."
        ),
        "placeholder": "系統檢查結果將顯示在這裡。",
        "run_again": "重新檢查",
        "copy_report": "複製報告",
        "close": "關閉",
        "copied": "已複製",
        "status_ready": "系統已就緒 — 所有相容性檢查皆已通過。",
        "status_warnings": "系統檢查已完成，但有警告。",
        "status_problems": "發現問題。請依照下方說明操作。",
        "status_failed": "無法完成系統檢查。",
        "technical_details": "技術詳細資訊",
        "report_ready_title": "系統已就緒",
        "report_ready_line1": "所有相容性檢查皆已成功通過。",
        "report_ready_line2": "Local Screen Translator 已準備好使用。",
        "report_self_help_title": "LOCAL SCREEN TRANSLATOR - 自助診斷",
        "report_detected": "偵測到:",
        "report_how_to_fix": "解決方法:",
        "report_search_web": "在網路上搜尋:",
        "report_after_steps": "完成這些步驟後，請再次執行系統檢查。",
    },

    "ja": {
        "system_check": "システムチェック",
        "description": (
            "GPU、OCR、画面キャプチャ、ローカル AI モデル、"
            "テキスト整列、Windows 音声合成を確認します。"
        ),
        "ready_to_check": "チェックの準備ができました。",
        "checking": (
            "システムの互換性を確認しています。"
            "AI モデルのテストには少し時間がかかる場合があります..."
        ),
        "placeholder": "システムチェックの結果がここに表示されます。",
        "run_again": "もう一度チェック",
        "copy_report": "レポートをコピー",
        "close": "閉じる",
        "copied": "コピーしました",
        "status_ready": "システムは準備完了です — すべての互換性チェックに合格しました。",
        "status_warnings": "システムチェックは警告付きで完了しました。",
        "status_problems": "問題が見つかりました。以下の手順に従ってください。",
        "status_failed": "システムチェックを完了できませんでした。",
        "technical_details": "技術情報",
        "report_ready_title": "システムは準備完了です",
        "report_ready_line1": "すべての互換性チェックに正常に合格しました。",
        "report_ready_line2": "Local Screen Translator を使用する準備ができました。",
        "report_self_help_title": "LOCAL SCREEN TRANSLATOR - 自己診断",
        "report_detected": "検出:",
        "report_how_to_fix": "解決方法:",
        "report_search_web": "インターネットで検索:",
        "report_after_steps": "これらの手順を完了した後、システムチェックをもう一度実行してください。",
    },

    "ko": {
        "system_check": "시스템 검사",
        "description": (
            "GPU, OCR, 화면 캡처, 로컬 AI 모델, "
            "텍스트 정렬 및 Windows 음성 합성을 검사합니다."
        ),
        "ready_to_check": "검사 준비가 되었습니다.",
        "checking": (
            "시스템 호환성을 검사하고 있습니다. "
            "AI 모델 테스트에는 시간이 조금 걸릴 수 있습니다..."
        ),
        "placeholder": "시스템 검사 결과가 여기에 표시됩니다.",
        "run_again": "다시 검사",
        "copy_report": "보고서 복사",
        "close": "닫기",
        "copied": "복사됨",
        "status_ready": "시스템이 준비되었습니다 — 모든 호환성 검사를 통과했습니다.",
        "status_warnings": "시스템 검사가 경고와 함께 완료되었습니다.",
        "status_problems": "문제가 발견되었습니다. 아래 지침을 따르십시오.",
        "status_failed": "시스템 검사를 완료할 수 없습니다.",
        "technical_details": "기술 세부 정보",
        "report_ready_title": "시스템 준비 완료",
        "report_ready_line1": "모든 호환성 검사를 성공적으로 통과했습니다.",
        "report_ready_line2": "Local Screen Translator를 사용할 준비가 되었습니다.",
        "report_self_help_title": "LOCAL SCREEN TRANSLATOR - 자체 진단",
        "report_detected": "감지됨:",
        "report_how_to_fix": "해결 방법:",
        "report_search_web": "인터넷 검색:",
        "report_after_steps": "이 단계를 완료한 후 시스템 검사를 다시 실행하십시오.",
    },
})


def current_system_check_language() -> str:
    try:
        from user_settings import USER_SETTINGS

        return resolve_ui_language(
            USER_SETTINGS.ui_language
        )

    except Exception:
        return detect_system_language()


def sc_t(
    key: str,
    language: str | None = None,
) -> str:
    language = (
        language
        or current_system_check_language()
    )

    table = SC_TRANSLATIONS.get(
        language,
        SC_TRANSLATIONS["en"],
    )

    return table.get(
        key,
        SC_TRANSLATIONS["en"].get(
            key,
            key,
        ),
    )
