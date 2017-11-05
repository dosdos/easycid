import hashlib
from datetime import datetime

import requests


def primo_pagamento_ssl(amount=100):
    amount = str(amount)
    apikey = "ALIAS_WEB_00001427"
    secretkey = "C6WRL5VG178ZAED7COEOHE8Y0Y3SOQZ5"
    group = "GRP_01231"
    request_url = "https://int-ecommerce.cartasi.it/ecomm/api/recurring/primoPagamentoSSL"
    code_trans = "TESTPS_{}".format(datetime.utcnow().strftime('%Y%m%d%H%M%S'))
    divisa = "978"  # divisa 978 indica EUR
    card_pan = "4539970000000006"
    card_expiration = "122030"
    card_cvv = "123"
    contract_number = "TESTPS_{}".format(datetime.utcnow().strftime('%Y%m%d%H%M%S'))
    contract_expiration = "31/12/2020"
    timestamp = datetime.utcnow().strftime('%Y%m%d%H%M%S%f')
    cf = "RSSNDR80A01H501L"
    description = "Descrizione Autorizzazione"
    email = "cardHolder@mail.it"
    hash_string = "apiKey={}numeroContratto={}codiceTransazione={}importo={}divisa={}pan={}cvv={}scadenza={}timeStamp={}{}".format(
        apikey, contract_number, code_trans, amount, divisa, card_pan, card_cvv, card_expiration, timestamp, secretkey
    )
    hash_object = hashlib.sha1(hash_string)
    mac = hash_object.hexdigest()

    request_params = {
        'apiKey': apikey,
        'numeroContratto': contract_number,
        'codiceGruppo': group,
        'codiceTransazione': code_trans,
        'importo': amount,
        'divisa': divisa,
        'pan': card_pan,
        'scadenza': card_expiration,
        'cvv': card_cvv,
        'timeStamp': timestamp,
        'mac': mac,
        # optional fields
        'scadenzaContratto': contract_expiration,
        'mail': email,
        'descrizione': description,
        'codiceFiscale': cf,
    }
    r = requests.post(request_url, data=request_params)
    return r.status_code, r.text
