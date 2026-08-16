#define MyAppName "Local Screen Translator"
#define MyAppVersion "1.0.0"
#define MyAppPublisher "kukilvan"
#define MyAppExeName "LocalScreenTranslator.exe"
#define SourceRoot "C:\LST_FINAL\LocalScreenTranslator"

[Setup]
AppId={{6F468F8D-083D-4C5E-A550-CC6D6E76F2AA}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}

DefaultDirName={autopf}\Local Screen Translator
DefaultGroupName=Local Screen Translator

OutputDir=C:\LST_INSTALLER
OutputBaseFilename=LocalScreenTranslator_Setup_1.0.0

SetupIconFile={#SourceRoot}\app.ico
UninstallDisplayIcon={app}\{#MyAppExeName}

ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64compatible
PrivilegesRequired=admin

Compression=lzma2/normal
SolidCompression=no

DiskSpanning=yes
DiskSliceSize=1900000000
SlicesPerDisk=1

WizardStyle=modern
DisableProgramGroupPage=yes

LanguageDetectionMethod=uilanguage
ShowLanguageDialog=no

[Languages]
Name: "en"; MessagesFile: "compiler:Default.isl"
Name: "ru"; MessagesFile: "compiler:Languages\Russian.isl"
Name: "uk"; MessagesFile: "compiler:Languages\Ukrainian.isl"
Name: "de"; MessagesFile: "compiler:Languages\German.isl"
Name: "fr"; MessagesFile: "compiler:Languages\French.isl"
Name: "it"; MessagesFile: "compiler:Languages\Italian.isl"
Name: "es"; MessagesFile: "compiler:Languages\Spanish.isl"
Name: "pt_PT"; MessagesFile: "compiler:Languages\Portuguese.isl"
Name: "pt_BR"; MessagesFile: "compiler:Languages\BrazilianPortuguese.isl"
Name: "pl"; MessagesFile: "compiler:Languages\Polish.isl"
Name: "cs"; MessagesFile: "compiler:Languages\Czech.isl"
Name: "sk"; MessagesFile: "compiler:Languages\Slovak.isl"
Name: "da"; MessagesFile: "compiler:Languages\Danish.isl"
Name: "fi"; MessagesFile: "compiler:Languages\Finnish.isl"
Name: "sv"; MessagesFile: "compiler:Languages\Swedish.isl"
Name: "no"; MessagesFile: "compiler:Languages\Norwegian.isl"
Name: "nl"; MessagesFile: "compiler:Languages\Dutch.isl"
Name: "hu"; MessagesFile: "compiler:Languages\Hungarian.isl"
Name: "sl"; MessagesFile: "compiler:Languages\Slovenian.isl"
Name: "bg"; MessagesFile: "compiler:Languages\Bulgarian.isl"
Name: "tr"; MessagesFile: "compiler:Languages\Turkish.isl"
Name: "ar"; MessagesFile: "compiler:Languages\Arabic.isl"
Name: "th"; MessagesFile: "compiler:Languages\Thai.isl"
Name: "ja"; MessagesFile: "compiler:Languages\Japanese.isl"
Name: "ko"; MessagesFile: "compiler:Languages\Korean.isl"

[Files]
Source: "{#SourceRoot}\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{autoprograms}\Local Screen Translator"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\Local Screen Translator"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#MyAppName}}"; Flags: nowait postinstall skipifsilent

