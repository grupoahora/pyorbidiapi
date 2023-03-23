from hubspot import HubSpot
import requests
import json
import datetime

# Establecer la clave de la API
api_client = HubSpot(
    access_token='pat-eu1-9492283a-09bc-4833-9dca-8c643d662007')

# Configurar las credenciales de autenticación
hapikey = 'pat-eu1-9492283a-09bc-4833-9dca-8c643d662007'
headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer ' + hapikey}

# Obtener todos los contactos y crear un acuerdo para cada uno
all_contacts = api_client.crm.contacts.get_all()
for contact in all_contacts:

    # Convertir la fecha a UNIX epoch
    closedate = datetime.datetime.strptime(
        "2022-12-31", "%Y-%m-%d").timestamp()

    # Crear el acuerdo
    deal_properties = {
        "properties": [
            {
                "name": "dealname",
                "value": f"Deal with {contact.properties.get('firstname')} {contact.properties.get('lastname')}"
            },
            {
                "name": "dealstage",
                "value": "appointmentscheduled"
            },
            {
                "name": "pipeline",
                "value": "default"
            },
            {
                "name": "amount",
                "value": "100"
            },
            {
                "name": "closedate",
                "value": str(int(closedate * 1000))  # Convertir a milisegundos
            },
            {
                "name": "hubspot_owner_id",
                "value": contact.properties.get('hubspot_owner_id')
            }
        ],
        "associations": {
            "associatedVids": [contact.id],  # IDs de los contactos asociados
            "associatedCompanyIds": [],  # IDs de las empresas asociadas
            "associatedDealIds": [],  # IDs de otros acuerdos asociados
            "associatedTicketIds": []  # IDs de los tickets asociados
        }
    }

    # Hacer la solicitud POST utilizando la API de Hubspot
    url = 'https://api.hubapi.com/deals/v1/deal'
    response = requests.post(url, headers=headers,
                             data=json.dumps(deal_properties))

    # Imprimir el resultado de la solicitud
    print(response.status_code)
    print(response.content)
