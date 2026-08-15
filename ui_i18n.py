from __future__ import annotations

import ctypes
import os


UI_LANGUAGES = (
    ("auto", "System language"),
    ("en", "English"),
    ("ru", "Русский"),
    ("uk", "Українська"),
    ("de", "Deutsch"),
    ("fr", "Français"),
    ("it", "Italiano"),
    ("es-ES", "Español (España)"),
    ("es-US", "Español (Latinoamérica)"),
    ("pt-PT", "Português (Portugal)"),
    ("pt-BR", "Português (Brasil)"),
    ("pl", "Polski"),
    ("cs", "Čeština"),
    ("sk", "Slovenčina"),
    ("da", "Dansk"),
    ("fi", "Suomi"),
    ("sv", "Svenska"),
    ("no", "Norsk"),
    ("nl", "Nederlands"),
    ("el", "Ελληνικά"),
    ("hu", "Magyar"),
    ("ro", "Română"),
    ("lt", "Lietuvių"),
    ("lv", "Latviešu"),
    ("et", "Eesti"),
    ("sl", "Slovenščina"),
    ("bg", "Български"),
    ("hr", "Hrvatski"),
    ("tr", "Türkçe"),
    ("ar", "العربية"),
    ("hi", "हिन्दी"),
    ("vi", "Tiếng Việt"),
    ("id", "Bahasa Indonesia"),
    ("th", "ไทย"),
    ("zh-CN", "简体中文"),
    ("zh-TW", "繁體中文"),
    ("ja", "日本語"),
    ("ko", "한국어"),
)


TRANSLATIONS = {
    "en": {
        "settings_title": "Local Screen Translator - Settings",
        "interface_language": "Interface language:",
        "translation_language": "Translation language:",
        "word_hotkey": "Word hotkey:",
        "paragraph_hotkey": "Paragraph hotkey:",
        "hud_auto_hide": "HUD auto-hide:",
        "seconds": " sec",
        "autostart": "Start Local Screen Translator with Windows",
        "tray_settings": "Settings...",
        "tray_exit": "Exit",
        "startup_error": "Startup error: {error}",
        "error": "Error: {error}",
        "translation_failed": "Could not translate {text}",
        "save": "Save",
        "cancel": "Cancel",
        "system_language": "System language",
    },

    "ru": {
        "settings_title": "Local Screen Translator — Настройки",
        "interface_language": "Язык интерфейса:",
        "translation_language": "Язык перевода:",
        "word_hotkey": "Горячая клавиша для слова:",
        "paragraph_hotkey": "Горячая клавиша для абзаца:",
        "hud_auto_hide": "Автоскрытие HUD:",
        "seconds": " сек",
        "autostart": "Запускать Local Screen Translator вместе с Windows",
        "tray_settings": "Настройки...",
        "tray_exit": "Выход",
        "startup_error": "Ошибка запуска: {error}",
        "error": "Ошибка: {error}",
        "translation_failed": "Не удалось перевести {text}",
        "save": "Сохранить",
        "cancel": "Отмена",
        "system_language": "Язык системы",
    },

    "uk": {
        "settings_title": "Local Screen Translator — Налаштування",
        "interface_language": "Мова інтерфейсу:",
        "translation_language": "Мова перекладу:",
        "word_hotkey": "Гаряча клавіша для слова:",
        "paragraph_hotkey": "Гаряча клавіша для абзацу:",
        "hud_auto_hide": "Автоприховування HUD:",
        "seconds": " с",
        "autostart": "Запускати Local Screen Translator разом із Windows",
        "tray_settings": "Налаштування...",
        "tray_exit": "Вихід",
        "startup_error": "Помилка запуску: {error}",
        "error": "Помилка: {error}",
        "translation_failed": "Не вдалося перекласти {text}",
        "save": "Зберегти",
        "cancel": "Скасувати",
        "system_language": "Мова системи",
    },

    "de": {
        "settings_title": "Local Screen Translator – Einstellungen",
        "interface_language": "Sprache der Benutzeroberfläche:",
        "translation_language": "Übersetzungssprache:",
        "word_hotkey": "Tastenkürzel für Wort:",
        "paragraph_hotkey": "Tastenkürzel für Absatz:",
        "hud_auto_hide": "HUD automatisch ausblenden:",
        "seconds": " Sek.",
        "autostart": "Local Screen Translator mit Windows starten",
        "tray_settings": "Einstellungen...",
        "tray_exit": "Beenden",
        "startup_error": "Startfehler: {error}",
        "error": "Fehler: {error}",
        "translation_failed": "{text} konnte nicht übersetzt werden",
        "save": "Speichern",
        "cancel": "Abbrechen",
        "system_language": "Systemsprache",
    },

    "fr": {
        "settings_title": "Local Screen Translator – Paramètres",
        "interface_language": "Langue de l’interface :",
        "translation_language": "Langue de traduction :",
        "word_hotkey": "Raccourci pour un mot :",
        "paragraph_hotkey": "Raccourci pour un paragraphe :",
        "hud_auto_hide": "Masquage automatique du HUD :",
        "seconds": " s",
        "autostart": "Démarrer Local Screen Translator avec Windows",
        "tray_settings": "Paramètres...",
        "tray_exit": "Quitter",
        "startup_error": "Erreur de démarrage : {error}",
        "error": "Erreur : {error}",
        "translation_failed": "Impossible de traduire {text}",
        "save": "Enregistrer",
        "cancel": "Annuler",
        "system_language": "Langue du système",
    },

    "it": {
        "settings_title": "Local Screen Translator – Impostazioni",
        "interface_language": "Lingua dell'interfaccia:",
        "translation_language": "Lingua di traduzione:",
        "word_hotkey": "Scorciatoia per parola:",
        "paragraph_hotkey": "Scorciatoia per paragrafo:",
        "hud_auto_hide": "Nascondi automaticamente HUD:",
        "seconds": " sec",
        "autostart": "Avvia Local Screen Translator con Windows",
        "tray_settings": "Impostazioni...",
        "tray_exit": "Esci",
        "startup_error": "Errore di avvio: {error}",
        "error": "Errore: {error}",
        "translation_failed": "Impossibile tradurre {text}",
        "save": "Salva",
        "cancel": "Annulla",
        "system_language": "Lingua di sistema",
    },

    "es-ES": {
        "settings_title": "Local Screen Translator – Configuración",
        "interface_language": "Idioma de la interfaz:",
        "translation_language": "Idioma de traducción:",
        "word_hotkey": "Atajo para palabra:",
        "paragraph_hotkey": "Atajo para párrafo:",
        "hud_auto_hide": "Ocultar HUD automáticamente:",
        "seconds": " s",
        "autostart": "Iniciar Local Screen Translator con Windows",
        "tray_settings": "Configuración...",
        "tray_exit": "Salir",
        "startup_error": "Error de inicio: {error}",
        "error": "Error: {error}",
        "translation_failed": "No se pudo traducir {text}",
        "save": "Guardar",
        "cancel": "Cancelar",
        "system_language": "Idioma del sistema",
    },

    "es-US": {
        "settings_title": "Local Screen Translator – Configuración",
        "interface_language": "Idioma de la interfaz:",
        "translation_language": "Idioma de traducción:",
        "word_hotkey": "Atajo para palabra:",
        "paragraph_hotkey": "Atajo para párrafo:",
        "hud_auto_hide": "Ocultar HUD automáticamente:",
        "seconds": " s",
        "autostart": "Iniciar Local Screen Translator con Windows",
        "tray_settings": "Configuración...",
        "tray_exit": "Salir",
        "startup_error": "Error de inicio: {error}",
        "error": "Error: {error}",
        "translation_failed": "No se pudo traducir {text}",
        "save": "Guardar",
        "cancel": "Cancelar",
        "system_language": "Idioma del sistema",
    },

    "pt-PT": {
        "settings_title": "Local Screen Translator – Definições",
        "interface_language": "Idioma da interface:",
        "translation_language": "Idioma de tradução:",
        "word_hotkey": "Atalho para palavra:",
        "paragraph_hotkey": "Atalho para parágrafo:",
        "hud_auto_hide": "Ocultar HUD automaticamente:",
        "seconds": " s",
        "autostart": "Iniciar Local Screen Translator com o Windows",
        "tray_settings": "Definições...",
        "tray_exit": "Sair",
        "startup_error": "Erro de arranque: {error}",
        "error": "Erro: {error}",
        "translation_failed": "Não foi possível traduzir {text}",
        "save": "Guardar",
        "cancel": "Cancelar",
        "system_language": "Idioma do sistema",
    },

    "pt-BR": {
        "settings_title": "Local Screen Translator – Configurações",
        "interface_language": "Idioma da interface:",
        "translation_language": "Idioma da tradução:",
        "word_hotkey": "Atalho para palavra:",
        "paragraph_hotkey": "Atalho para parágrafo:",
        "hud_auto_hide": "Ocultar HUD automaticamente:",
        "seconds": " s",
        "autostart": "Iniciar Local Screen Translator com o Windows",
        "tray_settings": "Configurações...",
        "tray_exit": "Sair",
        "startup_error": "Erro de inicialização: {error}",
        "error": "Erro: {error}",
        "translation_failed": "Não foi possível traduzir {text}",
        "save": "Salvar",
        "cancel": "Cancelar",
        "system_language": "Idioma do sistema",
    },

    "pl": {
        "settings_title": "Local Screen Translator – Ustawienia",
        "interface_language": "Język interfejsu:",
        "translation_language": "Język tłumaczenia:",
        "word_hotkey": "Skrót dla słowa:",
        "paragraph_hotkey": "Skrót dla akapitu:",
        "hud_auto_hide": "Automatyczne ukrywanie HUD:",
        "seconds": " s",
        "autostart": "Uruchamiaj Local Screen Translator z systemem Windows",
        "tray_settings": "Ustawienia...",
        "tray_exit": "Zakończ",
        "startup_error": "Błąd uruchamiania: {error}",
        "error": "Błąd: {error}",
        "translation_failed": "Nie udało się przetłumaczyć {text}",
        "save": "Zapisz",
        "cancel": "Anuluj",
        "system_language": "Język systemu",
    },

    "cs": {
        "settings_title": "Local Screen Translator – Nastavení",
        "interface_language": "Jazyk rozhraní:",
        "translation_language": "Jazyk překladu:",
        "word_hotkey": "Klávesová zkratka pro slovo:",
        "paragraph_hotkey": "Klávesová zkratka pro odstavec:",
        "hud_auto_hide": "Automatické skrytí HUD:",
        "seconds": " s",
        "autostart": "Spouštět Local Screen Translator se systémem Windows",
        "tray_settings": "Nastavení...",
        "tray_exit": "Ukončit",
        "startup_error": "Chyba při spuštění: {error}",
        "error": "Chyba: {error}",
        "translation_failed": "Nepodařilo se přeložit {text}",
        "save": "Uložit",
        "cancel": "Zrušit",
        "system_language": "Jazyk systému",
    },

    "sk": {
        "settings_title": "Local Screen Translator – Nastavenia",
        "interface_language": "Jazyk rozhrania:",
        "translation_language": "Jazyk prekladu:",
        "word_hotkey": "Klávesová skratka pre slovo:",
        "paragraph_hotkey": "Klávesová skratka pre odsek:",
        "hud_auto_hide": "Automatické skrytie HUD:",
        "seconds": " s",
        "autostart": "Spúšťať Local Screen Translator so systémom Windows",
        "tray_settings": "Nastavenia...",
        "tray_exit": "Ukončiť",
        "startup_error": "Chyba pri spustení: {error}",
        "error": "Chyba: {error}",
        "translation_failed": "Nepodarilo sa preložiť {text}",
        "save": "Uložiť",
        "cancel": "Zrušiť",
        "system_language": "Jazyk systému",
    },

    "da": {
        "settings_title": "Local Screen Translator – Indstillinger",
        "interface_language": "Grænsefladesprog:",
        "translation_language": "Oversættelsessprog:",
        "word_hotkey": "Genvejstast for ord:",
        "paragraph_hotkey": "Genvejstast for afsnit:",
        "hud_auto_hide": "Skjul HUD automatisk:",
        "seconds": " sek.",
        "autostart": "Start Local Screen Translator med Windows",
        "tray_settings": "Indstillinger...",
        "tray_exit": "Afslut",
        "startup_error": "Startfejl: {error}",
        "error": "Fejl: {error}",
        "translation_failed": "Kunne ikke oversætte {text}",
        "save": "Gem",
        "cancel": "Annuller",
        "system_language": "Systemsprog",
    },

    "fi": {
        "settings_title": "Local Screen Translator – Asetukset",
        "interface_language": "Käyttöliittymän kieli:",
        "translation_language": "Käännöskieli:",
        "word_hotkey": "Sanan pikanäppäin:",
        "paragraph_hotkey": "Kappaleen pikanäppäin:",
        "hud_auto_hide": "HUD:n automaattinen piilotus:",
        "seconds": " s",
        "autostart": "Käynnistä Local Screen Translator Windowsin kanssa",
        "tray_settings": "Asetukset...",
        "tray_exit": "Lopeta",
        "startup_error": "Käynnistysvirhe: {error}",
        "error": "Virhe: {error}",
        "translation_failed": "Tekstiä {text} ei voitu kääntää",
        "save": "Tallenna",
        "cancel": "Peruuta",
        "system_language": "Järjestelmän kieli",
    },

    "sv": {
        "settings_title": "Local Screen Translator – Inställningar",
        "interface_language": "Gränssnittsspråk:",
        "translation_language": "Översättningsspråk:",
        "word_hotkey": "Kortkommando för ord:",
        "paragraph_hotkey": "Kortkommando för stycke:",
        "hud_auto_hide": "Dölj HUD automatiskt:",
        "seconds": " s",
        "autostart": "Starta Local Screen Translator med Windows",
        "tray_settings": "Inställningar...",
        "tray_exit": "Avsluta",
        "startup_error": "Startfel: {error}",
        "error": "Fel: {error}",
        "translation_failed": "Kunde inte översätta {text}",
        "save": "Spara",
        "cancel": "Avbryt",
        "system_language": "Systemspråk",
    },

    "no": {
        "settings_title": "Local Screen Translator – Innstillinger",
        "interface_language": "Grensesnittspråk:",
        "translation_language": "Oversettelsesspråk:",
        "word_hotkey": "Hurtigtast for ord:",
        "paragraph_hotkey": "Hurtigtast for avsnitt:",
        "hud_auto_hide": "Skjul HUD automatisk:",
        "seconds": " sek.",
        "autostart": "Start Local Screen Translator med Windows",
        "tray_settings": "Innstillinger...",
        "tray_exit": "Avslutt",
        "startup_error": "Oppstartsfeil: {error}",
        "error": "Feil: {error}",
        "translation_failed": "Kunne ikke oversette {text}",
        "save": "Lagre",
        "cancel": "Avbryt",
        "system_language": "Systemspråk",
    },

    "nl": {
        "settings_title": "Local Screen Translator – Instellingen",
        "interface_language": "Interfacetaal:",
        "translation_language": "Vertaaltaal:",
        "word_hotkey": "Sneltoets voor woord:",
        "paragraph_hotkey": "Sneltoets voor alinea:",
        "hud_auto_hide": "HUD automatisch verbergen:",
        "seconds": " sec",
        "autostart": "Local Screen Translator starten met Windows",
        "tray_settings": "Instellingen...",
        "tray_exit": "Afsluiten",
        "startup_error": "Opstartfout: {error}",
        "error": "Fout: {error}",
        "translation_failed": "Kon {text} niet vertalen",
        "save": "Opslaan",
        "cancel": "Annuleren",
        "system_language": "Systeemtaal",
    },

    "el": {
        "settings_title": "Local Screen Translator – Ρυθμίσεις",
        "interface_language": "Γλώσσα διεπαφής:",
        "translation_language": "Γλώσσα μετάφρασης:",
        "word_hotkey": "Συντόμευση για λέξη:",
        "paragraph_hotkey": "Συντόμευση για παράγραφο:",
        "hud_auto_hide": "Αυτόματη απόκρυψη HUD:",
        "seconds": " δευτ.",
        "autostart": "Εκκίνηση του Local Screen Translator με τα Windows",
        "tray_settings": "Ρυθμίσεις...",
        "tray_exit": "Έξοδος",
        "startup_error": "Σφάλμα εκκίνησης: {error}",
        "error": "Σφάλμα: {error}",
        "translation_failed": "Δεν ήταν δυνατή η μετάφραση του {text}",
        "save": "Αποθήκευση",
        "cancel": "Ακύρωση",
        "system_language": "Γλώσσα συστήματος",
    },

    "hu": {
        "settings_title": "Local Screen Translator – Beállítások",
        "interface_language": "Felület nyelve:",
        "translation_language": "Fordítás nyelve:",
        "word_hotkey": "Szó gyorsbillentyűje:",
        "paragraph_hotkey": "Bekezdés gyorsbillentyűje:",
        "hud_auto_hide": "HUD automatikus elrejtése:",
        "seconds": " mp",
        "autostart": "Local Screen Translator indítása a Windowszal",
        "tray_settings": "Beállítások...",
        "tray_exit": "Kilépés",
        "startup_error": "Indítási hiba: {error}",
        "error": "Hiba: {error}",
        "translation_failed": "Nem sikerült lefordítani: {text}",
        "save": "Mentés",
        "cancel": "Mégse",
        "system_language": "Rendszernyelv",
    },

    "ro": {
        "settings_title": "Local Screen Translator – Setări",
        "interface_language": "Limba interfeței:",
        "translation_language": "Limba traducerii:",
        "word_hotkey": "Scurtătură pentru cuvânt:",
        "paragraph_hotkey": "Scurtătură pentru paragraf:",
        "hud_auto_hide": "Ascundere automată HUD:",
        "seconds": " sec",
        "autostart": "Pornește Local Screen Translator odată cu Windows",
        "tray_settings": "Setări...",
        "tray_exit": "Ieșire",
        "startup_error": "Eroare la pornire: {error}",
        "error": "Eroare: {error}",
        "translation_failed": "Nu s-a putut traduce {text}",
        "save": "Salvează",
        "cancel": "Anulează",
        "system_language": "Limba sistemului",
    },

    "lt": {
        "settings_title": "Local Screen Translator – Nustatymai",
        "interface_language": "Sąsajos kalba:",
        "translation_language": "Vertimo kalba:",
        "word_hotkey": "Žodžio spartusis klavišas:",
        "paragraph_hotkey": "Pastraipos spartusis klavišas:",
        "hud_auto_hide": "Automatiškai slėpti HUD:",
        "seconds": " sek.",
        "autostart": "Paleisti Local Screen Translator kartu su Windows",
        "tray_settings": "Nustatymai...",
        "tray_exit": "Išeiti",
        "startup_error": "Paleidimo klaida: {error}",
        "error": "Klaida: {error}",
        "translation_failed": "Nepavyko išversti {text}",
        "save": "Išsaugoti",
        "cancel": "Atšaukti",
        "system_language": "Sistemos kalba",
    },

    "lv": {
        "settings_title": "Local Screen Translator – Iestatījumi",
        "interface_language": "Saskarnes valoda:",
        "translation_language": "Tulkojuma valoda:",
        "word_hotkey": "Vārda karstais taustiņš:",
        "paragraph_hotkey": "Rindkopas karstais taustiņš:",
        "hud_auto_hide": "Automātiski paslēpt HUD:",
        "seconds": " sek.",
        "autostart": "Palaist Local Screen Translator kopā ar Windows",
        "tray_settings": "Iestatījumi...",
        "tray_exit": "Iziet",
        "startup_error": "Palaišanas kļūda: {error}",
        "error": "Kļūda: {error}",
        "translation_failed": "Neizdevās iztulkot {text}",
        "save": "Saglabāt",
        "cancel": "Atcelt",
        "system_language": "Sistēmas valoda",
    },

    "et": {
        "settings_title": "Local Screen Translator – Seaded",
        "interface_language": "Liidese keel:",
        "translation_language": "Tõlkekeel:",
        "word_hotkey": "Sõna kiirklahv:",
        "paragraph_hotkey": "Lõigu kiirklahv:",
        "hud_auto_hide": "Peida HUD automaatselt:",
        "seconds": " s",
        "autostart": "Käivita Local Screen Translator koos Windowsiga",
        "tray_settings": "Seaded...",
        "tray_exit": "Välju",
        "startup_error": "Käivitusviga: {error}",
        "error": "Viga: {error}",
        "translation_failed": "Teksti {text} ei saanud tõlkida",
        "save": "Salvesta",
        "cancel": "Tühista",
        "system_language": "Süsteemi keel",
    },

    "sl": {
        "settings_title": "Local Screen Translator – Nastavitve",
        "interface_language": "Jezik vmesnika:",
        "translation_language": "Jezik prevoda:",
        "word_hotkey": "Bližnjica za besedo:",
        "paragraph_hotkey": "Bližnjica za odstavek:",
        "hud_auto_hide": "Samodejno skrij HUD:",
        "seconds": " s",
        "autostart": "Zaženi Local Screen Translator skupaj z Windows",
        "tray_settings": "Nastavitve...",
        "tray_exit": "Izhod",
        "startup_error": "Napaka pri zagonu: {error}",
        "error": "Napaka: {error}",
        "translation_failed": "Ni bilo mogoče prevesti {text}",
        "save": "Shrani",
        "cancel": "Prekliči",
        "system_language": "Jezik sistema",
    },

    "bg": {
        "settings_title": "Local Screen Translator – Настройки",
        "interface_language": "Език на интерфейса:",
        "translation_language": "Език за превод:",
        "word_hotkey": "Клавишна комбинация за дума:",
        "paragraph_hotkey": "Клавишна комбинация за абзац:",
        "hud_auto_hide": "Автоматично скриване на HUD:",
        "seconds": " сек",
        "autostart": "Стартиране на Local Screen Translator с Windows",
        "tray_settings": "Настройки...",
        "tray_exit": "Изход",
        "startup_error": "Грешка при стартиране: {error}",
        "error": "Грешка: {error}",
        "translation_failed": "Неуспешен превод на {text}",
        "save": "Запази",
        "cancel": "Отказ",
        "system_language": "Език на системата",
    },

    "hr": {
        "settings_title": "Local Screen Translator – Postavke",
        "interface_language": "Jezik sučelja:",
        "translation_language": "Jezik prijevoda:",
        "word_hotkey": "Prečac za riječ:",
        "paragraph_hotkey": "Prečac za odlomak:",
        "hud_auto_hide": "Automatski sakrij HUD:",
        "seconds": " s",
        "autostart": "Pokreni Local Screen Translator s Windowsima",
        "tray_settings": "Postavke...",
        "tray_exit": "Izlaz",
        "startup_error": "Pogreška pri pokretanju: {error}",
        "error": "Pogreška: {error}",
        "translation_failed": "Nije moguće prevesti {text}",
        "save": "Spremi",
        "cancel": "Odustani",
        "system_language": "Jezik sustava",
    },

    "tr": {
        "settings_title": "Local Screen Translator – Ayarlar",
        "interface_language": "Arayüz dili:",
        "translation_language": "Çeviri dili:",
        "word_hotkey": "Kelime kısayolu:",
        "paragraph_hotkey": "Paragraf kısayolu:",
        "hud_auto_hide": "HUD'u otomatik gizle:",
        "seconds": " sn",
        "autostart": "Local Screen Translator'ı Windows ile başlat",
        "tray_settings": "Ayarlar...",
        "tray_exit": "Çıkış",
        "startup_error": "Başlatma hatası: {error}",
        "error": "Hata: {error}",
        "translation_failed": "{text} çevrilemedi",
        "save": "Kaydet",
        "cancel": "İptal",
        "system_language": "Sistem dili",
    },

    "ar": {
        "settings_title": "Local Screen Translator – الإعدادات",
        "interface_language": "لغة الواجهة:",
        "translation_language": "لغة الترجمة:",
        "word_hotkey": "اختصار ترجمة الكلمة:",
        "paragraph_hotkey": "اختصار ترجمة الفقرة:",
        "hud_auto_hide": "إخفاء HUD تلقائيًا:",
        "seconds": " ث",
        "autostart": "تشغيل Local Screen Translator مع Windows",
        "tray_settings": "الإعدادات...",
        "tray_exit": "خروج",
        "startup_error": "خطأ في بدء التشغيل: {error}",
        "error": "خطأ: {error}",
        "translation_failed": "تعذرت ترجمة {text}",
        "save": "حفظ",
        "cancel": "إلغاء",
        "system_language": "لغة النظام",
    },

    "hi": {
        "settings_title": "Local Screen Translator – सेटिंग्स",
        "interface_language": "इंटरफ़ेस भाषा:",
        "translation_language": "अनुवाद भाषा:",
        "word_hotkey": "शब्द हॉटकी:",
        "paragraph_hotkey": "पैराग्राफ हॉटकी:",
        "hud_auto_hide": "HUD स्वतः छिपाएँ:",
        "seconds": " सेकंड",
        "autostart": "Windows के साथ Local Screen Translator शुरू करें",
        "tray_settings": "सेटिंग्स...",
        "tray_exit": "बाहर निकलें",
        "startup_error": "स्टार्टअप त्रुटि: {error}",
        "error": "त्रुटि: {error}",
        "translation_failed": "{text} का अनुवाद नहीं हो सका",
        "save": "सहेजें",
        "cancel": "रद्द करें",
        "system_language": "सिस्टम भाषा",
    },

    "vi": {
        "settings_title": "Local Screen Translator – Cài đặt",
        "interface_language": "Ngôn ngữ giao diện:",
        "translation_language": "Ngôn ngữ dịch:",
        "word_hotkey": "Phím tắt cho từ:",
        "paragraph_hotkey": "Phím tắt cho đoạn văn:",
        "hud_auto_hide": "Tự động ẩn HUD:",
        "seconds": " giây",
        "autostart": "Khởi động Local Screen Translator cùng Windows",
        "tray_settings": "Cài đặt...",
        "tray_exit": "Thoát",
        "startup_error": "Lỗi khởi động: {error}",
        "error": "Lỗi: {error}",
        "translation_failed": "Không thể dịch {text}",
        "save": "Lưu",
        "cancel": "Hủy",
        "system_language": "Ngôn ngữ hệ thống",
    },

    "id": {
        "settings_title": "Local Screen Translator – Pengaturan",
        "interface_language": "Bahasa antarmuka:",
        "translation_language": "Bahasa terjemahan:",
        "word_hotkey": "Tombol pintas kata:",
        "paragraph_hotkey": "Tombol pintas paragraf:",
        "hud_auto_hide": "Sembunyikan HUD otomatis:",
        "seconds": " dtk",
        "autostart": "Jalankan Local Screen Translator bersama Windows",
        "tray_settings": "Pengaturan...",
        "tray_exit": "Keluar",
        "startup_error": "Kesalahan saat memulai: {error}",
        "error": "Kesalahan: {error}",
        "translation_failed": "Tidak dapat menerjemahkan {text}",
        "save": "Simpan",
        "cancel": "Batal",
        "system_language": "Bahasa sistem",
    },

    "th": {
        "settings_title": "Local Screen Translator – การตั้งค่า",
        "interface_language": "ภาษาของอินเทอร์เฟซ:",
        "translation_language": "ภาษาสำหรับแปล:",
        "word_hotkey": "ปุ่มลัดสำหรับคำ:",
        "paragraph_hotkey": "ปุ่มลัดสำหรับย่อหน้า:",
        "hud_auto_hide": "ซ่อน HUD อัตโนมัติ:",
        "seconds": " วินาที",
        "autostart": "เริ่ม Local Screen Translator พร้อม Windows",
        "tray_settings": "การตั้งค่า...",
        "tray_exit": "ออก",
        "startup_error": "ข้อผิดพลาดในการเริ่มต้น: {error}",
        "error": "ข้อผิดพลาด: {error}",
        "translation_failed": "ไม่สามารถแปล {text} ได้",
        "save": "บันทึก",
        "cancel": "ยกเลิก",
        "system_language": "ภาษาของระบบ",
    },

    "zh-CN": {
        "settings_title": "Local Screen Translator – 设置",
        "interface_language": "界面语言：",
        "translation_language": "翻译语言：",
        "word_hotkey": "单词快捷键：",
        "paragraph_hotkey": "段落快捷键：",
        "hud_auto_hide": "HUD 自动隐藏：",
        "seconds": " 秒",
        "autostart": "随 Windows 启动 Local Screen Translator",
        "tray_settings": "设置...",
        "tray_exit": "退出",
        "startup_error": "启动错误：{error}",
        "error": "错误：{error}",
        "translation_failed": "无法翻译 {text}",
        "save": "保存",
        "cancel": "取消",
        "system_language": "系统语言",
    },

    "zh-TW": {
        "settings_title": "Local Screen Translator – 設定",
        "interface_language": "介面語言：",
        "translation_language": "翻譯語言：",
        "word_hotkey": "單字快捷鍵：",
        "paragraph_hotkey": "段落快捷鍵：",
        "hud_auto_hide": "HUD 自動隱藏：",
        "seconds": " 秒",
        "autostart": "隨 Windows 啟動 Local Screen Translator",
        "tray_settings": "設定...",
        "tray_exit": "結束",
        "startup_error": "啟動錯誤：{error}",
        "error": "錯誤：{error}",
        "translation_failed": "無法翻譯 {text}",
        "save": "儲存",
        "cancel": "取消",
        "system_language": "系統語言",
    },

    "ja": {
        "settings_title": "Local Screen Translator – 設定",
        "interface_language": "インターフェース言語:",
        "translation_language": "翻訳先言語:",
        "word_hotkey": "単語のホットキー:",
        "paragraph_hotkey": "段落のホットキー:",
        "hud_auto_hide": "HUDの自動非表示:",
        "seconds": " 秒",
        "autostart": "Windows起動時にLocal Screen Translatorを起動",
        "tray_settings": "設定...",
        "tray_exit": "終了",
        "startup_error": "起動エラー: {error}",
        "error": "エラー: {error}",
        "translation_failed": "{text}を翻訳できませんでした",
        "save": "保存",
        "cancel": "キャンセル",
        "system_language": "システム言語",
    },

    "ko": {
        "settings_title": "Local Screen Translator – 설정",
        "interface_language": "인터페이스 언어:",
        "translation_language": "번역 언어:",
        "word_hotkey": "단어 단축키:",
        "paragraph_hotkey": "문단 단축키:",
        "hud_auto_hide": "HUD 자동 숨김:",
        "seconds": "초",
        "autostart": "Windows 시작 시 Local Screen Translator 실행",
        "tray_settings": "설정...",
        "tray_exit": "종료",
        "startup_error": "시작 오류: {error}",
        "error": "오류: {error}",
        "translation_failed": "{text}을(를) 번역할 수 없습니다",
        "save": "저장",
        "cancel": "취소",
        "system_language": "시스템 언어",
    },
}



TTS_UI_TRANSLATIONS = {
    "en": {
        "pronunciation_voice": "Pronunciation voice:",
        "automatic_voice": "Automatic (recommended)",
        "microsoft_voice_pack": "Microsoft voice pack:",
        "install_voice_pack": "Install Microsoft voice",
        "installing_voice_pack": "Installing...",
        "installing_voice_pack_status": "Installing {locale} from Microsoft...",
        "voice_pack_installed": "{locale} voice pack installed successfully.",
        "voice_pack_restart": "{locale} installed. Restart Windows to finish installation.",
        "voice_pack_install_error": "Voice installation failed: {error}",
    },

    "ru": {
        "pronunciation_voice": "Голос произношения:",
        "automatic_voice": "Автоматически (рекомендуется)",
        "microsoft_voice_pack": "Голосовой пакет Microsoft:",
        "install_voice_pack": "Установить голос Microsoft",
        "installing_voice_pack": "Установка...",
        "installing_voice_pack_status": "Установка {locale} с серверов Microsoft...",
        "voice_pack_installed": "Голосовой пакет {locale} успешно установлен.",
        "voice_pack_restart": "{locale} установлен. Перезапустите Windows для завершения установки.",
        "voice_pack_install_error": "Не удалось установить голос: {error}",
    },

    "uk": {
        "pronunciation_voice": "Голос вимови:",
        "automatic_voice": "Автоматично (рекомендовано)",
        "microsoft_voice_pack": "Голосовий пакет Microsoft:",
        "install_voice_pack": "Встановити голос Microsoft",
        "installing_voice_pack": "Встановлення...",
        "installing_voice_pack_status": "Встановлення {locale} із серверів Microsoft...",
        "voice_pack_installed": "Голосовий пакет {locale} успішно встановлено.",
        "voice_pack_restart": "{locale} встановлено. Перезапустіть Windows для завершення.",
        "voice_pack_install_error": "Не вдалося встановити голос: {error}",
    },

    "de": {
        "pronunciation_voice": "Aussprache-Stimme:",
        "automatic_voice": "Automatisch (empfohlen)",
        "microsoft_voice_pack": "Microsoft-Sprachpaket:",
        "install_voice_pack": "Microsoft-Stimme installieren",
        "installing_voice_pack": "Wird installiert...",
        "installing_voice_pack_status": "{locale} wird von Microsoft installiert...",
        "voice_pack_installed": "Sprachpaket {locale} wurde erfolgreich installiert.",
        "voice_pack_restart": "{locale} wurde installiert. Starten Sie Windows neu.",
        "voice_pack_install_error": "Stimme konnte nicht installiert werden: {error}",
    },

    "fr": {
        "pronunciation_voice": "Voix de prononciation :",
        "automatic_voice": "Automatique (recommandé)",
        "microsoft_voice_pack": "Pack vocal Microsoft :",
        "install_voice_pack": "Installer une voix Microsoft",
        "installing_voice_pack": "Installation...",
        "installing_voice_pack_status": "Installation de {locale} depuis Microsoft...",
        "voice_pack_installed": "Le pack vocal {locale} a été installé.",
        "voice_pack_restart": "{locale} est installé. Redémarrez Windows pour terminer.",
        "voice_pack_install_error": "Échec de l’installation de la voix : {error}",
    },

    "it": {
        "pronunciation_voice": "Voce di pronuncia:",
        "automatic_voice": "Automatica (consigliata)",
        "microsoft_voice_pack": "Pacchetto vocale Microsoft:",
        "install_voice_pack": "Installa voce Microsoft",
        "installing_voice_pack": "Installazione...",
        "installing_voice_pack_status": "Installazione di {locale} da Microsoft...",
        "voice_pack_installed": "Pacchetto vocale {locale} installato.",
        "voice_pack_restart": "{locale} installato. Riavvia Windows per completare.",
        "voice_pack_install_error": "Installazione della voce non riuscita: {error}",
    },

    "es-ES": {
        "pronunciation_voice": "Voz de pronunciación:",
        "automatic_voice": "Automática (recomendada)",
        "microsoft_voice_pack": "Paquete de voz de Microsoft:",
        "install_voice_pack": "Instalar voz de Microsoft",
        "installing_voice_pack": "Instalando...",
        "installing_voice_pack_status": "Instalando {locale} desde Microsoft...",
        "voice_pack_installed": "Paquete de voz {locale} instalado correctamente.",
        "voice_pack_restart": "{locale} instalado. Reinicia Windows para finalizar.",
        "voice_pack_install_error": "No se pudo instalar la voz: {error}",
    },

    "es-US": {
        "pronunciation_voice": "Voz de pronunciación:",
        "automatic_voice": "Automática (recomendada)",
        "microsoft_voice_pack": "Paquete de voz de Microsoft:",
        "install_voice_pack": "Instalar voz de Microsoft",
        "installing_voice_pack": "Instalando...",
        "installing_voice_pack_status": "Instalando {locale} desde Microsoft...",
        "voice_pack_installed": "Paquete de voz {locale} instalado correctamente.",
        "voice_pack_restart": "{locale} instalado. Reinicia Windows para finalizar.",
        "voice_pack_install_error": "No se pudo instalar la voz: {error}",
    },

    "pt-PT": {
        "pronunciation_voice": "Voz de pronúncia:",
        "automatic_voice": "Automática (recomendado)",
        "microsoft_voice_pack": "Pacote de voz Microsoft:",
        "install_voice_pack": "Instalar voz Microsoft",
        "installing_voice_pack": "A instalar...",
        "installing_voice_pack_status": "A instalar {locale} da Microsoft...",
        "voice_pack_installed": "Pacote de voz {locale} instalado.",
        "voice_pack_restart": "{locale} instalado. Reinicie o Windows para concluir.",
        "voice_pack_install_error": "Falha ao instalar a voz: {error}",
    },

    "pt-BR": {
        "pronunciation_voice": "Voz de pronúncia:",
        "automatic_voice": "Automática (recomendado)",
        "microsoft_voice_pack": "Pacote de voz da Microsoft:",
        "install_voice_pack": "Instalar voz da Microsoft",
        "installing_voice_pack": "Instalando...",
        "installing_voice_pack_status": "Instalando {locale} da Microsoft...",
        "voice_pack_installed": "Pacote de voz {locale} instalado com sucesso.",
        "voice_pack_restart": "{locale} instalado. Reinicie o Windows para concluir.",
        "voice_pack_install_error": "Falha ao instalar a voz: {error}",
    },

    "pl": {
        "pronunciation_voice": "Głos wymowy:",
        "automatic_voice": "Automatycznie (zalecane)",
        "microsoft_voice_pack": "Pakiet głosowy Microsoft:",
        "install_voice_pack": "Zainstaluj głos Microsoft",
        "installing_voice_pack": "Instalowanie...",
        "installing_voice_pack_status": "Instalowanie {locale} z Microsoft...",
        "voice_pack_installed": "Pakiet głosowy {locale} został zainstalowany.",
        "voice_pack_restart": "{locale} zainstalowano. Uruchom ponownie Windows.",
        "voice_pack_install_error": "Nie udało się zainstalować głosu: {error}",
    },

    "cs": {
        "pronunciation_voice": "Hlas výslovnosti:",
        "automatic_voice": "Automaticky (doporučeno)",
        "microsoft_voice_pack": "Hlasový balíček Microsoft:",
        "install_voice_pack": "Nainstalovat hlas Microsoft",
        "installing_voice_pack": "Instalace...",
        "installing_voice_pack_status": "Instaluje se {locale} od Microsoftu...",
        "voice_pack_installed": "Hlasový balíček {locale} byl nainstalován.",
        "voice_pack_restart": "{locale} byl nainstalován. Restartujte Windows.",
        "voice_pack_install_error": "Hlas se nepodařilo nainstalovat: {error}",
    },

    "sk": {
        "pronunciation_voice": "Hlas výslovnosti:",
        "automatic_voice": "Automaticky (odporúčané)",
        "microsoft_voice_pack": "Hlasový balík Microsoft:",
        "install_voice_pack": "Nainštalovať hlas Microsoft",
        "installing_voice_pack": "Inštalácia...",
        "installing_voice_pack_status": "Inštaluje sa {locale} od Microsoftu...",
        "voice_pack_installed": "Hlasový balík {locale} bol nainštalovaný.",
        "voice_pack_restart": "{locale} bol nainštalovaný. Reštartujte Windows.",
        "voice_pack_install_error": "Hlas sa nepodarilo nainštalovať: {error}",
    },

    "da": {
        "pronunciation_voice": "Udtalestemme:",
        "automatic_voice": "Automatisk (anbefalet)",
        "microsoft_voice_pack": "Microsoft-stemmepakke:",
        "install_voice_pack": "Installer Microsoft-stemme",
        "installing_voice_pack": "Installerer...",
        "installing_voice_pack_status": "Installerer {locale} fra Microsoft...",
        "voice_pack_installed": "Stemmepakken {locale} er installeret.",
        "voice_pack_restart": "{locale} er installeret. Genstart Windows.",
        "voice_pack_install_error": "Stemmen kunne ikke installeres: {error}",
    },

    "fi": {
        "pronunciation_voice": "Ääntämisääni:",
        "automatic_voice": "Automaattinen (suositeltu)",
        "microsoft_voice_pack": "Microsoft-äänipaketti:",
        "install_voice_pack": "Asenna Microsoft-ääni",
        "installing_voice_pack": "Asennetaan...",
        "installing_voice_pack_status": "Asennetaan {locale} Microsoftilta...",
        "voice_pack_installed": "Äänipaketti {locale} asennettiin.",
        "voice_pack_restart": "{locale} asennettiin. Käynnistä Windows uudelleen.",
        "voice_pack_install_error": "Äänen asennus epäonnistui: {error}",
    },

    "sv": {
        "pronunciation_voice": "Uttalsröst:",
        "automatic_voice": "Automatisk (rekommenderas)",
        "microsoft_voice_pack": "Microsoft-röstpaket:",
        "install_voice_pack": "Installera Microsoft-röst",
        "installing_voice_pack": "Installerar...",
        "installing_voice_pack_status": "Installerar {locale} från Microsoft...",
        "voice_pack_installed": "Röstpaketet {locale} har installerats.",
        "voice_pack_restart": "{locale} har installerats. Starta om Windows.",
        "voice_pack_install_error": "Rösten kunde inte installeras: {error}",
    },

    "no": {
        "pronunciation_voice": "Uttalestemme:",
        "automatic_voice": "Automatisk (anbefalt)",
        "microsoft_voice_pack": "Microsoft-stemmepakke:",
        "install_voice_pack": "Installer Microsoft-stemme",
        "installing_voice_pack": "Installerer...",
        "installing_voice_pack_status": "Installerer {locale} fra Microsoft...",
        "voice_pack_installed": "Stemmepakken {locale} er installert.",
        "voice_pack_restart": "{locale} er installert. Start Windows på nytt.",
        "voice_pack_install_error": "Kunne ikke installere stemmen: {error}",
    },

    "nl": {
        "pronunciation_voice": "Uitspraakstem:",
        "automatic_voice": "Automatisch (aanbevolen)",
        "microsoft_voice_pack": "Microsoft-stempakket:",
        "install_voice_pack": "Microsoft-stem installeren",
        "installing_voice_pack": "Installeren...",
        "installing_voice_pack_status": "{locale} wordt geïnstalleerd vanaf Microsoft...",
        "voice_pack_installed": "Stempakket {locale} is geïnstalleerd.",
        "voice_pack_restart": "{locale} is geïnstalleerd. Start Windows opnieuw.",
        "voice_pack_install_error": "Stem installeren mislukt: {error}",
    },

    "el": {
        "pronunciation_voice": "Φωνή προφοράς:",
        "automatic_voice": "Αυτόματα (συνιστάται)",
        "microsoft_voice_pack": "Πακέτο φωνής Microsoft:",
        "install_voice_pack": "Εγκατάσταση φωνής Microsoft",
        "installing_voice_pack": "Εγκατάσταση...",
        "installing_voice_pack_status": "Εγκατάσταση {locale} από τη Microsoft...",
        "voice_pack_installed": "Το πακέτο φωνής {locale} εγκαταστάθηκε.",
        "voice_pack_restart": "Το {locale} εγκαταστάθηκε. Επανεκκινήστε τα Windows.",
        "voice_pack_install_error": "Αποτυχία εγκατάστασης φωνής: {error}",
    },

    "hu": {
        "pronunciation_voice": "Kiejtési hang:",
        "automatic_voice": "Automatikus (ajánlott)",
        "microsoft_voice_pack": "Microsoft hangcsomag:",
        "install_voice_pack": "Microsoft-hang telepítése",
        "installing_voice_pack": "Telepítés...",
        "installing_voice_pack_status": "{locale} telepítése a Microsofttól...",
        "voice_pack_installed": "A(z) {locale} hangcsomag telepítve.",
        "voice_pack_restart": "{locale} telepítve. Indítsa újra a Windowst.",
        "voice_pack_install_error": "A hang telepítése sikertelen: {error}",
    },

    "ro": {
        "pronunciation_voice": "Voce pentru pronunție:",
        "automatic_voice": "Automat (recomandat)",
        "microsoft_voice_pack": "Pachet vocal Microsoft:",
        "install_voice_pack": "Instalează voce Microsoft",
        "installing_voice_pack": "Se instalează...",
        "installing_voice_pack_status": "Se instalează {locale} de la Microsoft...",
        "voice_pack_installed": "Pachetul vocal {locale} a fost instalat.",
        "voice_pack_restart": "{locale} a fost instalat. Reporniți Windows.",
        "voice_pack_install_error": "Instalarea vocii a eșuat: {error}",
    },

    "lt": {
        "pronunciation_voice": "Tarimo balsas:",
        "automatic_voice": "Automatiškai (rekomenduojama)",
        "microsoft_voice_pack": "Microsoft balso paketas:",
        "install_voice_pack": "Įdiegti Microsoft balsą",
        "installing_voice_pack": "Diegiama...",
        "installing_voice_pack_status": "Diegiamas {locale} iš Microsoft...",
        "voice_pack_installed": "Balso paketas {locale} įdiegtas.",
        "voice_pack_restart": "{locale} įdiegtas. Paleiskite Windows iš naujo.",
        "voice_pack_install_error": "Nepavyko įdiegti balso: {error}",
    },

    "lv": {
        "pronunciation_voice": "Izrunas balss:",
        "automatic_voice": "Automātiski (ieteicams)",
        "microsoft_voice_pack": "Microsoft balss pakotne:",
        "install_voice_pack": "Instalēt Microsoft balsi",
        "installing_voice_pack": "Instalē...",
        "installing_voice_pack_status": "Instalē {locale} no Microsoft...",
        "voice_pack_installed": "Balss pakotne {locale} ir instalēta.",
        "voice_pack_restart": "{locale} ir instalēts. Restartējiet Windows.",
        "voice_pack_install_error": "Neizdevās instalēt balsi: {error}",
    },

    "et": {
        "pronunciation_voice": "Hääldushääl:",
        "automatic_voice": "Automaatne (soovitatud)",
        "microsoft_voice_pack": "Microsofti häälepakett:",
        "install_voice_pack": "Installi Microsofti hääl",
        "installing_voice_pack": "Installimine...",
        "installing_voice_pack_status": "{locale} installimine Microsoftilt...",
        "voice_pack_installed": "Häälepakett {locale} on installitud.",
        "voice_pack_restart": "{locale} on installitud. Taaskäivitage Windows.",
        "voice_pack_install_error": "Hääle installimine ebaõnnestus: {error}",
    },

    "sl": {
        "pronunciation_voice": "Glas izgovorjave:",
        "automatic_voice": "Samodejno (priporočeno)",
        "microsoft_voice_pack": "Microsoftov glasovni paket:",
        "install_voice_pack": "Namesti Microsoftov glas",
        "installing_voice_pack": "Nameščanje...",
        "installing_voice_pack_status": "Nameščanje {locale} iz Microsofta...",
        "voice_pack_installed": "Glasovni paket {locale} je nameščen.",
        "voice_pack_restart": "{locale} je nameščen. Znova zaženite Windows.",
        "voice_pack_install_error": "Glasu ni bilo mogoče namestiti: {error}",
    },

    "bg": {
        "pronunciation_voice": "Глас за произношение:",
        "automatic_voice": "Автоматично (препоръчително)",
        "microsoft_voice_pack": "Гласов пакет на Microsoft:",
        "install_voice_pack": "Инсталиране на Microsoft глас",
        "installing_voice_pack": "Инсталиране...",
        "installing_voice_pack_status": "Инсталиране на {locale} от Microsoft...",
        "voice_pack_installed": "Гласовият пакет {locale} е инсталиран.",
        "voice_pack_restart": "{locale} е инсталиран. Рестартирайте Windows.",
        "voice_pack_install_error": "Неуспешно инсталиране на гласа: {error}",
    },

    "hr": {
        "pronunciation_voice": "Glas izgovora:",
        "automatic_voice": "Automatski (preporučeno)",
        "microsoft_voice_pack": "Microsoft glasovni paket:",
        "install_voice_pack": "Instaliraj Microsoft glas",
        "installing_voice_pack": "Instaliranje...",
        "installing_voice_pack_status": "Instaliranje {locale} iz Microsofta...",
        "voice_pack_installed": "Glasovni paket {locale} je instaliran.",
        "voice_pack_restart": "{locale} je instaliran. Ponovno pokrenite Windows.",
        "voice_pack_install_error": "Instalacija glasa nije uspjela: {error}",
    },

    "tr": {
        "pronunciation_voice": "Telaffuz sesi:",
        "automatic_voice": "Otomatik (önerilen)",
        "microsoft_voice_pack": "Microsoft ses paketi:",
        "install_voice_pack": "Microsoft sesi yükle",
        "installing_voice_pack": "Yükleniyor...",
        "installing_voice_pack_status": "{locale} Microsoft'tan yükleniyor...",
        "voice_pack_installed": "{locale} ses paketi başarıyla yüklendi.",
        "voice_pack_restart": "{locale} yüklendi. Windows'u yeniden başlatın.",
        "voice_pack_install_error": "Ses yüklenemedi: {error}",
    },

    "ar": {
        "pronunciation_voice": "صوت النطق:",
        "automatic_voice": "تلقائي (موصى به)",
        "microsoft_voice_pack": "حزمة صوت Microsoft:",
        "install_voice_pack": "تثبيت صوت Microsoft",
        "installing_voice_pack": "جارٍ التثبيت...",
        "installing_voice_pack_status": "جارٍ تثبيت {locale} من Microsoft...",
        "voice_pack_installed": "تم تثبيت حزمة الصوت {locale}.",
        "voice_pack_restart": "تم تثبيت {locale}. أعد تشغيل Windows لإكمال التثبيت.",
        "voice_pack_install_error": "تعذر تثبيت الصوت: {error}",
    },

    "hi": {
        "pronunciation_voice": "उच्चारण की आवाज़:",
        "automatic_voice": "स्वचालित (अनुशंसित)",
        "microsoft_voice_pack": "Microsoft वॉइस पैक:",
        "install_voice_pack": "Microsoft आवाज़ इंस्टॉल करें",
        "installing_voice_pack": "इंस्टॉल हो रहा है...",
        "installing_voice_pack_status": "Microsoft से {locale} इंस्टॉल किया जा रहा है...",
        "voice_pack_installed": "{locale} वॉइस पैक सफलतापूर्वक इंस्टॉल हुआ।",
        "voice_pack_restart": "{locale} इंस्टॉल हुआ। Windows पुनः आरंभ करें।",
        "voice_pack_install_error": "आवाज़ इंस्टॉल नहीं हो सकी: {error}",
    },

    "vi": {
        "pronunciation_voice": "Giọng phát âm:",
        "automatic_voice": "Tự động (khuyến nghị)",
        "microsoft_voice_pack": "Gói giọng nói Microsoft:",
        "install_voice_pack": "Cài đặt giọng Microsoft",
        "installing_voice_pack": "Đang cài đặt...",
        "installing_voice_pack_status": "Đang cài {locale} từ Microsoft...",
        "voice_pack_installed": "Đã cài đặt gói giọng {locale}.",
        "voice_pack_restart": "Đã cài {locale}. Hãy khởi động lại Windows.",
        "voice_pack_install_error": "Không thể cài đặt giọng nói: {error}",
    },

    "id": {
        "pronunciation_voice": "Suara pengucapan:",
        "automatic_voice": "Otomatis (disarankan)",
        "microsoft_voice_pack": "Paket suara Microsoft:",
        "install_voice_pack": "Instal suara Microsoft",
        "installing_voice_pack": "Menginstal...",
        "installing_voice_pack_status": "Menginstal {locale} dari Microsoft...",
        "voice_pack_installed": "Paket suara {locale} berhasil diinstal.",
        "voice_pack_restart": "{locale} diinstal. Mulai ulang Windows.",
        "voice_pack_install_error": "Gagal menginstal suara: {error}",
    },

    "th": {
        "pronunciation_voice": "เสียงการออกเสียง:",
        "automatic_voice": "อัตโนมัติ (แนะนำ)",
        "microsoft_voice_pack": "แพ็กเสียง Microsoft:",
        "install_voice_pack": "ติดตั้งเสียง Microsoft",
        "installing_voice_pack": "กำลังติดตั้ง...",
        "installing_voice_pack_status": "กำลังติดตั้ง {locale} จาก Microsoft...",
        "voice_pack_installed": "ติดตั้งแพ็กเสียง {locale} สำเร็จแล้ว",
        "voice_pack_restart": "ติดตั้ง {locale} แล้ว โปรดรีสตาร์ต Windows",
        "voice_pack_install_error": "ติดตั้งเสียงไม่สำเร็จ: {error}",
    },

    "zh-CN": {
        "pronunciation_voice": "发音语音：",
        "automatic_voice": "自动（推荐）",
        "microsoft_voice_pack": "Microsoft 语音包：",
        "install_voice_pack": "安装 Microsoft 语音",
        "installing_voice_pack": "正在安装...",
        "installing_voice_pack_status": "正在从 Microsoft 安装 {locale}...",
        "voice_pack_installed": "{locale} 语音包已成功安装。",
        "voice_pack_restart": "{locale} 已安装。请重启 Windows 完成安装。",
        "voice_pack_install_error": "语音安装失败：{error}",
    },

    "zh-TW": {
        "pronunciation_voice": "發音語音：",
        "automatic_voice": "自動（建議）",
        "microsoft_voice_pack": "Microsoft 語音套件：",
        "install_voice_pack": "安裝 Microsoft 語音",
        "installing_voice_pack": "正在安裝...",
        "installing_voice_pack_status": "正在從 Microsoft 安裝 {locale}...",
        "voice_pack_installed": "{locale} 語音套件已成功安裝。",
        "voice_pack_restart": "{locale} 已安裝。請重新啟動 Windows。",
        "voice_pack_install_error": "語音安裝失敗：{error}",
    },

    "ja": {
        "pronunciation_voice": "発音音声:",
        "automatic_voice": "自動（推奨）",
        "microsoft_voice_pack": "Microsoft 音声パック:",
        "install_voice_pack": "Microsoft 音声をインストール",
        "installing_voice_pack": "インストール中...",
        "installing_voice_pack_status": "Microsoft から {locale} をインストールしています...",
        "voice_pack_installed": "{locale} 音声パックをインストールしました。",
        "voice_pack_restart": "{locale} をインストールしました。Windows を再起動してください。",
        "voice_pack_install_error": "音声のインストールに失敗しました: {error}",
    },

    "ko": {
        "pronunciation_voice": "발음 음성:",
        "automatic_voice": "자동 (권장)",
        "microsoft_voice_pack": "Microsoft 음성 팩:",
        "install_voice_pack": "Microsoft 음성 설치",
        "installing_voice_pack": "설치 중...",
        "installing_voice_pack_status": "Microsoft에서 {locale} 설치 중...",
        "voice_pack_installed": "{locale} 음성 팩이 설치되었습니다.",
        "voice_pack_restart": "{locale} 설치 완료. Windows를 다시 시작하세요.",
        "voice_pack_install_error": "음성 설치 실패: {error}",
    },
}

for _language, _values in TTS_UI_TRANSLATIONS.items():
    TRANSLATIONS[_language].update(
        _values
    )


def _windows_locale_name() -> str:
    if os.name != "nt":
        return ""

    try:
        buffer = ctypes.create_unicode_buffer(85)

        result = (
            ctypes.windll.kernel32
            .GetUserDefaultLocaleName(
                buffer,
                len(buffer),
            )
        )

        if result:
            return buffer.value

    except Exception:
        pass

    return ""


def normalize_language(
    code: str,
) -> str:
    code = (
        (code or "")
        .replace("_", "-")
        .strip()
    )

    lower = code.lower()

    if lower.startswith("zh"):
        if any(
            item in lower
            for item in (
                "tw",
                "hk",
                "mo",
                "hant",
            )
        ):
            return "zh-TW"

        return "zh-CN"

    if lower.startswith("pt"):
        if "br" in lower:
            return "pt-BR"

        return "pt-PT"

    if lower.startswith("es"):
        if any(
            item in lower
            for item in (
                "mx",
                "ar",
                "cl",
                "co",
                "pe",
                "ve",
                "uy",
                "py",
                "bo",
                "ec",
                "gt",
                "cu",
                "do",
                "hn",
                "ni",
                "pa",
                "pr",
                "sv",
                "cr",
            )
        ):
            return "es-US"

        return "es-ES"

    aliases = {
        "nb": "no",
        "nn": "no",
    }

    base = lower.split("-", 1)[0]
    base = aliases.get(
        base,
        base,
    )

    supported = {
        item[0]
        for item in UI_LANGUAGES
    }

    if base in supported:
        return base

    return "en"


def detect_system_language() -> str:
    return normalize_language(
        _windows_locale_name()
    )


def resolve_ui_language(
    selected: str,
) -> str:
    if (
        not selected
        or selected == "auto"
    ):
        return detect_system_language()

    return normalize_language(
        selected
    )


def t(
    key: str,
    language: str | None = None,
    **kwargs,
) -> str:
    if language is None:
        try:
            from user_settings import (
                USER_SETTINGS,
            )

            language = resolve_ui_language(
                USER_SETTINGS.ui_language
            )

        except Exception:
            language = (
                detect_system_language()
            )

    table = TRANSLATIONS.get(
        language,
        TRANSLATIONS["en"],
    )

    text = table.get(
        key,
        TRANSLATIONS["en"].get(
            key,
            key,
        ),
    )

    if kwargs:
        try:
            return text.format(
                **kwargs
            )
        except Exception:
            return text

    return text
