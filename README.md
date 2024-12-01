# WiFi Password Recovery

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Version: 1.0](https://img.shields.io/badge/Version-1.0-blue.svg)](./README.md)

**WiFi Password Recovery** es un script en Python que permite recuperar las contraseñas de las redes Wi-Fi almacenadas en un PC. Funciona tanto en **Windows** como en **Linux**, aprovechando herramientas nativas del sistema operativo (`netsh` en Windows y `nmcli` en Linux).

> **Advertencia**: Este script está diseñado únicamente para uso educativo o personal. Asegúrate de usarlo en tus propios dispositivos o con permiso explícito.

## Características

- Recupera los nombres (SSID) de las redes Wi-Fi almacenadas.
- Muestra las contraseñas de las redes donde están disponibles.
- Compatible con sistemas **Windows** y **Linux**.
- Presenta la información de manera clara y legible.

## Requisitos

- **Python 3.6+**: Instalado y configurado en el sistema.
- **Permisos de administrador**:
  - En **Windows**: Para acceder a la información de redes Wi-Fi usando `netsh`.
  - En **Linux**: Para acceder a las redes almacenadas con `nmcli`.

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu-usuario/wifi-password-recovery.git
   cd wifi-password-recovery
   ```

2. Asegúrate de tener Python instalado. Puedes verificarlo con:
   ```bash
   python --version
   ```

3. El script no requiere dependencias adicionales.

## Uso

1. Ejecuta el script desde la terminal con:
   ```bash
   python recover_wifi_passwords.py
   ```

2. El script detectará automáticamente el sistema operativo y utilizará:
   - **`netsh`** en Windows.
   - **`nmcli`** en Linux.

3. Mostrará una lista de redes Wi-Fi almacenadas junto con sus contraseñas, si están disponibles.

### Ejemplo de Salida

```plaintext
Red WiFi 1                    contraseña123
Red WiFi 2                    password456
Red WiFi 3                    (sin contraseña almacenada)
```

## Advertencias

- **Uso Ético**: Asegúrate de usar este script únicamente en tus propios dispositivos o con permiso explícito.
- **Linux**: El script requiere `nmcli` (NetworkManager Command Line Tool) instalado. Puedes instalarlo si no está disponible:
   ```bash
   sudo apt install network-manager
   ```

## Contribuciones

Contribuciones, reportes de errores y sugerencias son bienvenidos. Siéntete libre de abrir un _issue_ o enviar un _pull request_.

## Licencia

Este proyecto está licenciado bajo la [Licencia MIT](./LICENSE).

---

**Nota**: Este script funciona en Windows y Linux utilizando herramientas específicas de cada sistema. En caso de necesitar soporte para macOS, sería necesario implementar una lógica adicional.
