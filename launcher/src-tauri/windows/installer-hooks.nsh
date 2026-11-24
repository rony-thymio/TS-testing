; Thymio Suite installer additions (Windows, installed for all users).
;
; The device manager listens on the network ports 8596/8597 but only answers programs on the
; same computer. Without a rule, Windows Firewall asks "allow access?" the first time, a question
; pupils cannot answer. This rule blocks incoming network connections to it, so the question never
; appears and other computers cannot reach it. Programs on the same computer are not affected.

!macro NSIS_HOOK_POSTINSTALL
  nsExec::Exec 'netsh advfirewall firewall delete rule name="Thymio Suite device manager"'
  nsExec::Exec 'netsh advfirewall firewall add rule name="Thymio Suite device manager" dir=in action=block program="$INSTDIR\thymio-device-manager.exe" enable=yes profile=any'
!macroend

!macro NSIS_HOOK_POSTUNINSTALL
  nsExec::Exec 'netsh advfirewall firewall delete rule name="Thymio Suite device manager"'
!macroend
