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

[Files]
Source: "{#SourceRoot}\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{autoprograms}\Local Screen Translator"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\Local Screen Translator"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Создать ярлык на рабочем столе"; GroupDescription: "Дополнительные задачи:"

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "Запустить Local Screen Translator"; Flags: nowait postinstall skipifsilent
