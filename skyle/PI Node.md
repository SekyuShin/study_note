1. 설치
2. Linux용 windows 하위 시스템 옵션 기능 활성화
	- 관리자 권한 power shell
		- `dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart`
	- virtual machine 기능 사용
		- `dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart`
	- wsl 설치
		- `wsl.exe --install`
		- 