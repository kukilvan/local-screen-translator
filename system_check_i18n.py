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
