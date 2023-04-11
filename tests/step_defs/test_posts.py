import json
import os

import pytest
from pytest_bdd import when, then, scenarios, parsers

from tests.utils.api_request import ApiRequests

scenarios('../features/posts.feature')


@pytest.fixture()
def api_requests_instance(base_url):
    headers = {'Accept': 'application/json', 'Content-type': 'application/json;charset=UTF-8'}
    return ApiRequests(headers, base_url)


@when(parsers.parse("I send a {request_type} request to {endpoint}"))
def send_request(step_context, request_type, endpoint, api_requests_instance):
    if request_type == 'GET':
        get_response = api_requests_instance.get_request(endpoint)
        step_context['response_from_get'] = get_response.json()
        step_context['get_request_status_code'] = get_response.status_code
    elif request_type == 'POST':
        create_post_payload = __read_json('create_post')
        post_response = api_requests_instance.post_request(endpoint, create_post_payload)
        step_context['response_from_post'] = post_response.json()
        step_context['post_request_status_code'] = post_response.status_code
    elif request_type == 'PUT':
        create_put_payload = __read_json('update_post')
        put_response = api_requests_instance.put_request(endpoint, create_put_payload)
        step_context['response_from_put'] = put_response.json()
        step_context['put_request_status_code'] = put_response.status_code
    elif request_type == 'PATCH':
        create_patch_payload = __read_json('patch_post')
        patch_response = api_requests_instance.patch_request(endpoint, create_patch_payload)
        step_context['response_from_patch'] = patch_response.json()
        step_context['patch_request_status_code'] = patch_response.status_code
    elif request_type == 'DELETE':
        delete_response = api_requests_instance.delete_request(endpoint)
        step_context['response_from_delete'] = delete_response.json()
        step_context['delete_request_status_code'] = delete_response.status_code


@then("I see all the posts in the response")
def verify_response_length(step_context):
    assert len(step_context['response_from_get']) > 0


@then(parsers.parse("I post id from {request_type} response is {post_id}"))
def verify_post_ids(step_context, request_type, post_id):
    if request_type == 'GET':
        assert step_context['response_from_get']['id'] == int(post_id)
    elif request_type == 'POST':
        assert step_context['response_from_post']['id'] == int(post_id)
    elif request_type == 'PUT':
        assert step_context['response_from_put']['id'] == int(post_id)
    elif request_type == 'PATCH':
        assert step_context['response_from_patch']['id'] == int(post_id)


@then(parsers.parse("I get a {code} status code from {req_type} request"))
def verify_response_code(step_context, code, req_type):
    if req_type == 'GET':
        assert step_context['get_request_status_code'] == int(code)
    elif req_type == 'POST':
        assert step_context['post_request_status_code'] == int(code)
    elif req_type == 'PUT':
        assert step_context['put_request_status_code'] == int(code)
    elif req_type == 'PATCH':
        assert step_context['patch_request_status_code'] == int(code)
    elif req_type == 'DELETE':
        assert step_context['delete_request_status_code'] == int(code)


def __read_json(file_name: str) -> dict:
    """
    Reads a json file and returns as a dict.
    :param file_name (str): The name of the file to be read.
    :return:dict: The contents of the file as a dict.
    """
    try:
        folder_path = os.path.abspath(os.path.dirname(__file__))
        data_directory = os.path.join(folder_path, '../../tests/data')
        json_file = os.path.join(data_directory, f'{file_name}.json')

        with open(json_file, mode='r', encoding='utf-8', errors='ignore') as payload_file:
            return json.load(payload_file)
    except Exception as e:
        raise Exception(f'Error reading json file: {str(e)}')
