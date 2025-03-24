import httpx

from src import serializers


def test_serializers():
    data = '"AT+CMGL=\"ALL\"\r\r\n+CMGL: 1,\"REC READ\",\"+380505718633\",\"\",\"25/03/:37+08\"\r\ntest\r\n\r\nOK\r\n"'
    serialized_answer: list[dict] = serializers.serialize_all_messages(data)
    print(serialized_answer)
    assert serialized_answer[0]['id'] == '1'
    assert serialized_answer[0]['sent_by'] == '+380505718633'
    assert serialized_answer[0]['received_at'] == '25/03/:37+08'
    assert serialized_answer[0]['raw_message'] == 'test'


def test_single_message():
    data = 'AT+CMGR=1\r\r\n+CMGR: \"REC READ\",\"+380505718633\",\"\",\"25/03/23\"\r\ntest\r\n\r\nOK\r\n'
    answer = serializers.serialize_single_message(data)

    print(answer)
    assert answer['id'] == '1'
    assert answer['sent_by'] == '+380505718633'
    assert answer['received_at'] == '25/03/23'
    assert answer['raw_message'] == 'test'

def test_decode_message_body():
    data = httpx.get('http://alex-desktop.netis.cc:8081/messages/2')
    data = data.json()

    print(data)
