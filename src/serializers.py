from src.config import logger

def __reformat_message(row: str) -> dict:
    data: dict = {}
    try:

        row_splitted = row.split(",", 4)

        received_at, raw_message = row_splitted[-1].split("\r\n")

        data = {
            "id": row_splitted[0].replace("+CMGL: ", ''),
            "folder": row_splitted[1].replace('"', ""),
            "sent_by": row_splitted[2].replace('"', ""),
            "received_at": received_at.replace('"', ""),
            "raw_message": raw_message,
        }
        try:
            byte_data = bytes.fromhex(raw_message)
            decoded_text = byte_data.decode("utf-16BE")
            data["message_decoded"] = decoded_text
        except Exception as error:
            logger.error(error)
        return data
    except Exception as error:
        logger.exception(error)
        return {}


def serialize_all_messages(data: str) -> list[dict[str, str]]:
    """
    :param data:
    "AT+CMGL=\"ALL\"\r\r\n
    +CMGL: 1,\"REC READ\",\"+380505718633\",\"\",\"25/03/:37+08\"\r\ntest
    \r\n\r\n
    +CMGL: 7,\"REC READ\",\"robota.ua\",\"\",\"25/03/24,14:54:03+08\"\r\nVash kod dostupu - 7706. Kod diisnyylyn.
    \r\n\r\n
    OK\r\n"

    :return:
    [
        {
            "id": 1,
            "folder": "all, rec unread, rec read"
            "sent_by": "phone or naming of sender, 380505718633, rabota.ua, etc"
            "received_at": "25/03/23,18:02:45+08"
            "message_body": message_body
        }, ...
    ]
    """
    messages: list[dict]
    message_splitter = '\r\n\r\n'

    data_split = data.split('\r\r\n')
    header, second_message_part = data_split

    raw_messages_in_str_format = second_message_part.split(message_splitter)[:-1]

    messages = [
        __reformat_message(row) for row in raw_messages_in_str_format
    ]
    return messages


def serialize_single_message(data: str):
    """
    :param data:
    AT+CMGR=1\r\r\n
    +CMGR: \"REC READ\",\"+380505718633\",\"\",\"25/03/23\"\r\ntest\r\n\r\nOK\r\n

    :return:
    {
        "id": 1,
        "folder": "all, rec unread, rec read"
        "sent_by": "phone or naming of sender, 380505718633, rabota.ua, etc"
        "received_at": "25/03/23,18:02:45+08"
        "message_body": message_body
    }
    """
    message: dict = {}
    header, rest_of_message = data.split('\r\r\n')
    message['id'] = header.replace('AT+CMGR=', '')

    data = rest_of_message.replace('"', '').split(',', 4)
    message['folder'] = data[0].replace('+CMGR: ', '')
    message['sent_by'] = data[1]
    message['received_at'] = data[-1].split('\r\n')[0]
    encoded = data[-1].split('\r\n')[1]
    message['raw_message'] = encoded

    try:
        byte_data = bytes.fromhex(encoded)
        decoded_text = byte_data.decode("utf-16BE")
        message['message_decoded'] = decoded_text
    except Exception as error:
        logger.error(error)

    return message
