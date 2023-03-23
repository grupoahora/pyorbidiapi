from hubspot import HubSpot

api_client = HubSpot(
    access_token='pat-eu1-9492283a-09bc-4833-9dca-8c643d662007')

all_contacts = api_client.crm.contacts.get_all()

for contact in all_contacts:
    phone_number = contact.properties.get('phone')
    if phone_number is None:
        print(f"{contact.properties.get('firstname')} {contact.properties.get('lastname')} no tiene número de teléfono registrado. Aplicando número de respaldo...")
        updated_contact = api_client.crm.contacts.basic_api.update(
            contact_id=contact.id,
            simple_public_object_input={
                'properties': {
                    'phone': '660049971'
                }
            }
        )
        print(
            f"Teléfono actualizado para {updated_contact.properties.get('firstname')} {updated_contact.properties.get('lastname')} nuevo telefono {updated_contact.properties.get('phone')}")
