'''
Basic lazy request document

parts:
    method
    auth
    json

sample request:
GET||api-3743394573473||{"username":"sabit","password":"34453"}


'''


def parse_lazy_request(raw_data: bytes):
    text = raw_data.decode('utf-8', errors='ignore')
    splitedparts = text.split('||')

    return splitedparts

