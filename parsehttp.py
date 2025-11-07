def parse_http_request(raw_data: bytes):

    text = raw_data.decode('utf-8', errors='ignore')        #decoding raw data
    data_parts = text.split('\r\n\r\n', 1)              #spliting in 2 parts
    header_lines = data_parts[0].split('\r\n')                             # first part is header and second part is out http body
    body = data_parts[1].encode() if len(data_parts) > 1 else b''

    if len(header_lines) ==0:
        return None, None, {},body

    parts = header_lines[0].split()
    if len(parts) != 3:
        return None, None, {},body


    method, path, version = parts

    headers = {}
    for line in header_lines[1:]:
        if ": " in line:
            key, value = line.split(': ', 1)
            headers[key] = value

    return method, path, headers, body