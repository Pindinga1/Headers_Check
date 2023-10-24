import requests, json, sys
from colorama import Fore
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# Consulta de cabeceras BY Pindinga1
def Headers(target, redirect, ssl):
    banner = """
   _____ ____  __  __ _____  _    _ _   _ ______ _______ 
  / ____/ __ \|  \/  |  __ \| |  | | \ | |  ____|__   __|
 | |   | |  | | \  / | |__) | |  | |  \| | |__     | |   
 | |   | |  | | |\/| |  ___/| |  | | . ` |  __|    | |   
 | |___| |__| | |  | | |    | |__| | |\  | |____   | |   
  \_____\____/|_|  |_|_|     \____/|_| \_|______|  |_|   
"""
    print (Fore.LIGHTBLUE_EX + banner + Fore.RESET)
    print(Fore.CYAN + f'Realizando petición a {target}, espere un momento...\nSeguir Redirecciones: {redirect}' + Fore.RESET)
    try:
        security_headers_check = [
            "X-XSS-Protection",
            "X-Frame-Options",
            "X-Content-Type-Options",
            "Content-Security-Policy",
            "Referrer-Policy",
            "Permissions-Policy",
            "Strict-Transport-Security"
        ]
        count_present = 0
        count_absent = 0
        found = []
        not_found = []
        r = requests.get(f'{target}', allow_redirects=redirect, verify=ssl)
        resp_headers = r.headers
        status = r.status_code
        if r.status_code:
            print(Fore.CYAN + f'Código de respuesta: [{status}]\n' + Fore.RESET)
            for i in security_headers_check:
                if i in resp_headers:
                    print (Fore.LIGHTGREEN_EX + f'[OK] Cabecera: {i}, Valor: {resp_headers[i]} | PRESENTE' + Fore.RESET)
                    count_present += 1
                    found.append(f'{i}')
                else:
                    print (Fore.LIGHTRED_EX + f'[NOK] Cabecera {i} | NO PRESENTE'  + Fore.RESET)
                    count_absent += 1
                    not_found.append(f'{i}')
            print(Fore.LIGHTMAGENTA_EX + f'\n-------------------------------\n-------RESUMEN DE PRUEBA-------\n-------------------------------\nURL: {target}\n' + Fore.RESET)
            print(Fore.LIGHTMAGENTA_EX + f'Cabeceras de seguridad encontradas:' + Fore.RESET + Fore.LIGHTGREEN_EX + f' [{count_present}]\n' + Fore.RESET + Fore.LIGHTMAGENTA_EX + f'-----------------------------------'+ Fore.RESET)
            for i in found:
                print(Fore.LIGHTGREEN_EX + f'[OK] {i}' + Fore.RESET)
            print(Fore.LIGHTMAGENTA_EX + f'\nCabeceras de seguridad no encontradas:' + Fore.RESET + Fore.LIGHTRED_EX + f' [{count_absent}]\n' + Fore.RESET + Fore.LIGHTMAGENTA_EX + f'-----------------------------------'+ Fore.RESET)
            for i in not_found:
                print(Fore.LIGHTRED_EX + f'[NOK] {i}' + Fore.RESET)
            print(Fore.LIGHTMAGENTA_EX + f'\n-----------------------------------' + Fore.RESET)
            print(Fore.LIGHTBLUE_EX + f'ANÁLISIS FINALIZADO CORRECTAMENTE' + Fore.RESET)
        else:
            print (Fore.RED + 'Error en la respuesta, codigo de error: [{status}]\n' + Fore.RESET)
    except requests.exceptions.RequestException as e:
        if "CERTIFICATE_VERIFY_FAILED" in str(e):
            print(Fore.RED + f'Error en la solicitud: {e}\n Intenta utilizar el argumento nossl\n Ejemplo: headers.py url True nossl' + Fore.RESET)
        else:
            print(Fore.RED + f'Error en la solicitud: {e}' + Fore.RESET)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python headers.py URL False/True, False para no redirecciones y True para redirecciones\nPara deshabilitar SSL adicionar argumento nossl al final.")
    else:
        url = sys.argv[1]
        redirect = sys.argv[2].lower()
        ssl = True  # Establecemos un valor predeterminado para ssl
        if len(sys.argv) >= 4:
            ssl_arg = sys.argv[3].lower()
            if ssl_arg == 'nossl':
                ssl = False
        if redirect == 'true':
            redirect = True
        elif redirect == 'false':
            redirect = False
        else:
            print("El segundo argumento debe ser 'True' o 'False'.")
            redirect = False
            ssl = True 

        Headers(url, redirect, ssl)