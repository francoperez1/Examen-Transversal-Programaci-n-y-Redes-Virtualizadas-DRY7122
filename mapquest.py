import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "0ELbYtjcTZejmde2tO3AR7jMtIA6wdpj"
consumo_combustible_estimado = 9.0  


while True:
    orig = input("Ubicación de inicio: ")
    if orig.lower() in ["quit", "q", "s"]:
        break
    dest = input("Destino: ")
    if dest.lower() in ["quit", "q", "s"]:
        break
    url = main_api + urllib.parse.urlencode({"key": key, "from": orig, "to": dest})
    print("URL: " + url)
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("Estado de la API: " + str(json_status) + " = Llamada de ruta exitosa.\n")
        print("=============================================")
        print("Direcciones desde " + orig + " hasta " + dest)
        print("Duración del viaje: " + json_data["route"]["formattedTime"])
        
        
        millas = round(json_data["route"]["distance"], 1)
        kilometros = round(millas * 1.61, 1)
        print("Millas: " + str(millas))
        print("Kilómetros: " + str(kilometros))

        
        combustible_requerido_litros = (kilometros / 100) * consumo_combustible_estimado
        print("Combustible requerido (Litros): " + str(round(combustible_requerido_litros, 1)))

        print("=============================================")
        
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            narrativa = each["narrative"]
            
            distancia_km = round(each["distance"] * 1.61, 1)
            print(narrativa + " (" + str(distancia_km) + " km)")
        
        print("=============================================\n")

    elif json_status == 611:
        print("**********************************************")
        print("Código de estado: " + str(json_status) + "; Falta una entrada para una o ambas ubicaciones.")
        print("**********************************************\n")
    else:
        print("************************************************************************")
        print("Para el código de estado: " + str(json_status) + "; Consulte:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")

