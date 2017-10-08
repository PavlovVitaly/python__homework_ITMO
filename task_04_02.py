import json

KEYS_OF_HEADER_OF_GET_REQ = ("method", "uri", "protocol")
KEYS_OF_HEADER_OF_POST_REQ = ("protocol", "status_code", "status_message")


def __is_post_request(first_string):
    if first_string[0].find("HTTP/") != -1:
        return True
    return False


def __parse_header(first_string, header):
    key_header_of_post_request, value_header_of_post_request = list(), list()
    end_of_first_string = first_string.copy()
    for item in range(2):
        key_header_of_post_request.append(header[item])
        value_header_of_post_request.append(first_string[item])
        end_of_first_string.pop(0)
    end_of_first_string = ' '.join(end_of_first_string)
    key_header_of_post_request.append(header[2])
    value_header_of_post_request.append(end_of_first_string)
    return key_header_of_post_request, value_header_of_post_request


def __parse_header_of_get_request(first_string):
    return __parse_header(first_string, KEYS_OF_HEADER_OF_GET_REQ)


def __parse_header_of_post_request(first_string):
    return __parse_header(first_string, KEYS_OF_HEADER_OF_POST_REQ)


def __parse_header_of_request(first_string):
    first_string = first_string.replace('\n', '').split(' ')

    if __is_post_request(first_string):
        return __parse_header_of_post_request(first_string)
    return __parse_header_of_get_request(first_string)


def __read_file_with_request(headers):
    with open(headers) as input_file:
        content = input_file.readlines()
    return content


def __create_dictionary(key_dict, value_dict):
    output_dict = {}
    for x, y in zip(key_dict, value_dict):
        output_dict[x] = y
    return output_dict


def __parse_content_of_request(content):
    key_dict, value_dict = __parse_header_of_request(content[0])
    for item in range(1, len(content)):
        temp = content[item]
        key_and_value = temp.replace('\n', '')
        if key_and_value == '':
            continue
        key_and_value = key_and_value.split(':')
        key_dict.append(key_and_value[0].strip(' '))
        key_and_value.pop(0)
        key_and_value = ':'.join(key_and_value).strip(' ')
        value_dict.append(key_and_value)
    return __create_dictionary(key_dict, value_dict)


def write_json_file(file, data):
    with open(file, 'w') as result_json:
        json.dump(data, result_json)


def http_headers_to_json(headers, results):
    content = __read_file_with_request(headers)
    output_dict = __parse_content_of_request(content)
    write_json_file(results, output_dict)
