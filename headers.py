import requests, json, sys
from colorama import Fore
# Consulta de cabeceras BY Pindinga1
def Headers(target, redirect):
    banner = '##################################\n#CONSULTA CABECERAS By Pindinga1 #\n##################################\n'
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
        r = requests.get(f'{target}', allow_redirects=redirect)
        resp_headers = r.headers
        status = r.status_code
        if r.status_code:
            print(Fore.CYAN + f'Codigo de respuesta: [{status}]\n' + Fore.RESET)
            for i in security_headers_check:
                if i in resp_headers:
                    print (Fore.LIGHTGREEN_EX + f'Cabecera: {i}, Valor: {resp_headers[i]} | PRESENTE' + Fore.RESET)
                else:
                    print (Fore.RED + f'Cabecera {i} | NO PRESENTE :('  + Fore.RESET)
        else:
            print (Fore.RED + 'Error en la respuesta, codigo de error: [{status}]\n' + Fore.RESET)
    except requests.exceptions.RequestException as e:
        # Capturar excepciones de solicitud, como problemas de conexión
        print(Fore.RED + f'Error en la solicitud: {e}' + Fore.RESET)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python headers.py URL False/True , False para no redirecciones y True para redirecciones.")
    else:
        url = sys.argv[1]
        redirect = sys.argv[2].lower().strip() == 'true'
        Headers(url, redirect)