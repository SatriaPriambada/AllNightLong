[Setup]
AppName=Hello App
AppVersion=1.0
DefaultDirName={pf}\HelloApp
DefaultGroupName=Hello App
OutputBaseFilename=HelloAppInstaller
Compression=lzma
SolidCompression=yes
OutputDir=.

[Files]
Source: "dist\hello_app\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs

[Icons]
Name: "{group}\Hello App"; Filename: "{app}\hello_app.exe"
