import ast
import json

from django.http import HttpResponse
from v1.chatbot.combine_detection_logic import combine_output_of_detection_logic_and_tag
from v1.chatbot.tag_message import run_ner
from v1.constant import PARAMETER_MESSAGE, PARAMETER_ENTITY_NAME, PARAMETER_STRUCTURED_VALUE, \
    PARAMETER_STRUCTURED_VALUE_VERIFICATION, PARAMETER_FALLBACK_VALUE, PARAMETER_EXPERT_MESSAGE
from chatbot_ner.config import ner_logger
from v1.chatbot.entity_detection import get_text, get_location, get_phone_number, get_email, get_city, get_pnr, \
    get_number, get_shopping_size, get_time, get_date, get_budget, get_city_advance, \
    get_date_advance


def get_parameters_dictionary(request):
    """
    Returns the list of parameters require for NER
    :param request:
    :return:
    """
    if request.GET.get('structured_value_verification') == '':
        structured_value_verification = 0
    else:
        structured_value_verification = int(request.GET.get('structured_value_verification'))
    parameters_dict = {PARAMETER_MESSAGE: request.GET.get('message'),
                       PARAMETER_ENTITY_NAME: request.GET.get('entity_name'),
                       PARAMETER_STRUCTURED_VALUE: request.GET.get('structured_value'),
                       PARAMETER_STRUCTURED_VALUE_VERIFICATION: structured_value_verification,
                       PARAMETER_FALLBACK_VALUE: request.GET.get('fallback_value'),
                       PARAMETER_EXPERT_MESSAGE: request.GET.get('bot_message')}

    return parameters_dict


def text(request):
    """This functionality calls the get_text() functionality to detect textual entities. It is called through api call

    Attributes:
        request: url parameters

    """
    entity_name = None
    try:
        parameters_dict = get_parameters_dictionary(request)
        ner_logger.debug('Start: %s ' % entity_name)
        entity_output = get_text(parameters_dict[PARAMETER_MESSAGE], parameters_dict[PARAMETER_ENTITY_NAME],
                                 parameters_dict[PARAMETER_STRUCTURED_VALUE],
                                 parameters_dict[PARAMETER_STRUCTURED_VALUE_VERIFICATION],
                                 parameters_dict[PARAMETER_FALLBACK_VALUE],
                                 parameters_dict[PARAMETER_EXPERT_MESSAGE])
    except Exception, e:
        entity_output = {}
        ner_logger.debug('Exception for text_synonym: %s ' % e)

    ner_logger.debug('Finished %s : %s ' % (entity_name, entity_output))
    return HttpResponse(json.dumps({'data': entity_output}), content_type='application/json')


def location(request):
    """This functionality calls the get_location() functionality to detect location. It is called through api call

    Attributes:
        request: url parameters

    """
    entity_name = None
    try:
        parameters_dict = get_parameters_dictionary(request)
        ner_logger.debug('Start: %s ' % entity_name)
        entity_output = get_location(parameters_dict[PARAMETER_MESSAGE], parameters_dict[PARAMETER_ENTITY_NAME],
                                     parameters_dict[PARAMETER_STRUCTURED_VALUE],
                                     parameters_dict[PARAMETER_STRUCTURED_VALUE_VERIFICATION],
                                     parameters_dict[PARAMETER_FALLBACK_VALUE],
                                     parameters_dict[PARAMETER_EXPERT_MESSAGE])
    except Exception, e:
        entity_output = {}
        ner_logger.debug('Exception for location: %s ' % e)

    ner_logger.debug('Finished %s : %s ' % (entity_name, entity_output))
    return HttpResponse(json.dumps({'data': entity_output}), content_type='application/json')


def phone_number(request):
    """This functionality calls the get_phone_number() functionality to detect phone numbers. It is called through api call

    Attributes:
        request: url parameters

    """
    entity_name = None
    try:
        parameters_dict = get_parameters_dictionary(request)
        ner_logger.debug('Start: %s ' % entity_name)
        entity_output = get_phone_number(parameters_dict[PARAMETER_MESSAGE], parameters_dict[PARAMETER_ENTITY_NAME],
                                         parameters_dict[PARAMETER_STRUCTURED_VALUE],
                                         parameters_dict[PARAMETER_STRUCTURED_VALUE_VERIFICATION],
                                         parameters_dict[PARAMETER_FALLBACK_VALUE],
                                         parameters_dict[PARAMETER_EXPERT_MESSAGE])
    except Exception, e:
        entity_output = {}
        ner_logger.debug('Exception for phone_number: %s ' % e)

    ner_logger.debug('Finished %s : %s ' % (entity_name, entity_output))
    return HttpResponse(json.dumps({'data': entity_output}), content_type='application/json')


def email(request):
    """This functionality calls the get_email() functionality to detect email. It is called through api call

    Attributes:
        request: url parameters

    """
    entity_name = None
    try:
        parameters_dict = get_parameters_dictionary(request)
        ner_logger.debug('Start: %s ' % entity_name)
        entity_output = get_email(parameters_dict[PARAMETER_MESSAGE], parameters_dict[PARAMETER_ENTITY_NAME],
                                  parameters_dict[PARAMETER_STRUCTURED_VALUE],
                                  parameters_dict[PARAMETER_STRUCTURED_VALUE_VERIFICATION],
                                  parameters_dict[PARAMETER_FALLBACK_VALUE],
                                  parameters_dict[PARAMETER_EXPERT_MESSAGE])
    except Exception, e:
        entity_output = {}
        ner_logger.debug('Exception for email: %s ' % e)

    ner_logger.debug('Finished %s : %s ' % (entity_name, entity_output))
    return HttpResponse(json.dumps({'data': entity_output}), content_type='application/json')


def city(request):
    """This functionality calls the get_city() functionality to detect city. It is called through api call

    Attributes:
        request: url parameters

    """
    entity_name = None
    try:
        parameters_dict = get_parameters_dictionary(request)
        ner_logger.debug('Start: %s ' % entity_name)
        entity_output = get_city(parameters_dict[PARAMETER_MESSAGE], parameters_dict[PARAMETER_ENTITY_NAME],
                                 parameters_dict[PARAMETER_STRUCTURED_VALUE],
                                 parameters_dict[PARAMETER_STRUCTURED_VALUE_VERIFICATION],
                                 parameters_dict[PARAMETER_FALLBACK_VALUE],
                                 parameters_dict[PARAMETER_EXPERT_MESSAGE])
    except Exception, e:
        entity_output = {}
        ner_logger.debug('Exception for city: %s ' % e)

    ner_logger.debug('Finished %s : %s ' % (entity_name, entity_output))
    return HttpResponse(json.dumps({'data': entity_output}), content_type='application/json')


def pnr(request):
    """This functionality calls the get_pnr() functionality to detect pnr. It is called through api call

    Attributes:
        request: url parameters

    """
    entity_name = None
    try:
        parameters_dict = get_parameters_dictionary(request)
        ner_logger.debug('Start: %s ' % entity_name)
        entity_output = get_pnr(parameters_dict[PARAMETER_MESSAGE], parameters_dict[PARAMETER_ENTITY_NAME],
                                parameters_dict[PARAMETER_STRUCTURED_VALUE],
                                parameters_dict[PARAMETER_STRUCTURED_VALUE_VERIFICATION],
                                parameters_dict[PARAMETER_FALLBACK_VALUE],
                                parameters_dict[PARAMETER_EXPERT_MESSAGE])
    except Exception, e:
        entity_output = {}
        ner_logger.debug('Exception for pnr: %s ' % e)

    ner_logger.debug('Finished %s : %s ' % (entity_name, entity_output))
    return HttpResponse(json.dumps({'data': entity_output}), content_type='application/json')


def shopping_size(request):
    """This functionality calls the get_shopping_size() functionality to detect size. It is called through api call

    Attributes:
        request: url parameters

    """
    entity_name = None
    try:
        parameters_dict = get_parameters_dictionary(request)
        ner_logger.debug('Start: %s ' % entity_name)
        entity_output = get_shopping_size(parameters_dict[PARAMETER_MESSAGE], parameters_dict[PARAMETER_ENTITY_NAME],
                                          parameters_dict[PARAMETER_STRUCTURED_VALUE],
                                          parameters_dict[PARAMETER_STRUCTURED_VALUE_VERIFICATION],
                                          parameters_dict[PARAMETER_FALLBACK_VALUE],
                                          parameters_dict[PARAMETER_EXPERT_MESSAGE])
    except Exception, e:
        entity_output = {}
        ner_logger.debug('Exception for shopping_size: %s ' % e)

    ner_logger.debug('Finished %s : %s ' % (entity_name, entity_output))
    return HttpResponse(json.dumps({'data': entity_output}), content_type='application/json')


def number(request):
    """This functionality calls the get_numeric() functionality to detect numbers. It is called through api call

    Attributes:
        request: url parameters

    """
    entity_name = None
    try:
        parameters_dict = get_parameters_dictionary(request)
        ner_logger.debug('Start: %s ' % entity_name)
        entity_output = get_number(parameters_dict[PARAMETER_MESSAGE], parameters_dict[PARAMETER_ENTITY_NAME],
                                   parameters_dict[PARAMETER_STRUCTURED_VALUE],
                                   parameters_dict[PARAMETER_STRUCTURED_VALUE_VERIFICATION],
                                   parameters_dict[PARAMETER_FALLBACK_VALUE],
                                   parameters_dict[PARAMETER_EXPERT_MESSAGE])
    except Exception, e:
        entity_output = {}
        ner_logger.debug('Exception for numeric: %s ' % e)

    ner_logger.debug('Finished %s : %s ' % (entity_name, entity_output))
    return HttpResponse(json.dumps({'data': entity_output}), content_type='application/json')


def time(request):
    """This functionality calls the get_time() functionality to detect time. It is called through api call

    Attributes:
        request: url parameters

    """
    entity_name = None
    try:
        parameters_dict = get_parameters_dictionary(request)
        ner_logger.debug('Start: %s ' % entity_name)
        entity_output = get_time(parameters_dict[PARAMETER_MESSAGE], parameters_dict[PARAMETER_ENTITY_NAME],
                                 parameters_dict[PARAMETER_STRUCTURED_VALUE],
                                 parameters_dict[PARAMETER_STRUCTURED_VALUE_VERIFICATION],
                                 parameters_dict[PARAMETER_FALLBACK_VALUE],
                                 parameters_dict[PARAMETER_EXPERT_MESSAGE])
    except Exception, e:
        entity_output = {}
        ner_logger.debug('Exception for time: %s ' % e)

    ner_logger.debug('Finished %s : %s ' % (entity_name, entity_output))
    return HttpResponse(json.dumps({'data': entity_output}), content_type='application/json')


def date(request):
    """This functionality calls the get_date() functionality to detect date. It is called through api call

    Attributes:
        request: url parameters

    """
    entity_name = None
    try:
        parameters_dict = get_parameters_dictionary(request)
        ner_logger.debug('Start: %s ' % entity_name)
        entity_output = get_date(parameters_dict[PARAMETER_MESSAGE], parameters_dict[PARAMETER_ENTITY_NAME],
                                 parameters_dict[PARAMETER_STRUCTURED_VALUE],
                                 parameters_dict[PARAMETER_STRUCTURED_VALUE_VERIFICATION],
                                 parameters_dict[PARAMETER_FALLBACK_VALUE],
                                 parameters_dict[PARAMETER_EXPERT_MESSAGE])
    except Exception, e:
        entity_output = {}
        ner_logger.debug('Exception for date: %s ' % e)

    ner_logger.debug('Finished %s : %s ' % (entity_name, entity_output))
    return HttpResponse(json.dumps({'data': entity_output}), content_type='application/json')


def budget(request):
    """This functionality calls the get_budget() functionality to detect budget. It is called through api call

    Attributes:
        request: url parameters

    """
    entity_name = None
    try:
        parameters_dict = get_parameters_dictionary(request)
        ner_logger.debug('Start: %s ' % entity_name)
        entity_output = get_budget(parameters_dict[PARAMETER_MESSAGE], parameters_dict[PARAMETER_ENTITY_NAME],
                                   parameters_dict[PARAMETER_STRUCTURED_VALUE],
                                   parameters_dict[PARAMETER_STRUCTURED_VALUE_VERIFICATION],
                                   parameters_dict[PARAMETER_FALLBACK_VALUE],
                                   parameters_dict[PARAMETER_EXPERT_MESSAGE])
    except Exception, e:
        entity_output = {}
        ner_logger.debug('Exception for budget: %s ' % e)

    ner_logger.debug('Finished %s : %s ' % (entity_name, entity_output))
    return HttpResponse(json.dumps({'data': entity_output}), content_type='application/json')


def city_advance(request):
    """This functionality calls the get_city_advance() functionality to detect advance city attributes .
    It is called through api call

    Attributes:
        request: url parameters

    """
    entity_name = None
    try:
        parameters_dict = get_parameters_dictionary(request)
        ner_logger.debug('Start: %s ' % entity_name)
        entity_output = get_city_advance(parameters_dict[PARAMETER_MESSAGE], parameters_dict[PARAMETER_ENTITY_NAME],
                                         parameters_dict[PARAMETER_STRUCTURED_VALUE],
                                         parameters_dict[PARAMETER_STRUCTURED_VALUE_VERIFICATION],
                                         parameters_dict[PARAMETER_FALLBACK_VALUE],
                                         parameters_dict[PARAMETER_EXPERT_MESSAGE])
    except Exception, e:
        entity_output = {}
        ner_logger.debug('Exception for departure city: %s ' % e)

    ner_logger.debug('Finished %s : %s ' % (entity_name, entity_output))
    return HttpResponse(json.dumps({'data': entity_output}), content_type='application/json')


def date_advance(request):
    """This functionality calls the get_date_advance() functionality to detect advance date attributes .
    It is called through api call

    Attributes:
        request: url parameters

    """
    entity_name = None
    try:
        parameters_dict = get_parameters_dictionary(request)
        ner_logger.debug('Start: %s ' % entity_name)
        entity_output = get_date_advance(parameters_dict[PARAMETER_MESSAGE], parameters_dict[PARAMETER_ENTITY_NAME],
                                         parameters_dict[PARAMETER_STRUCTURED_VALUE],
                                         parameters_dict[PARAMETER_STRUCTURED_VALUE_VERIFICATION],
                                         parameters_dict[PARAMETER_FALLBACK_VALUE],
                                         parameters_dict[PARAMETER_EXPERT_MESSAGE])
    except Exception, e:
        entity_output = {}
        ner_logger.debug('Exception for date departure: %s ' % e)

    ner_logger.debug('Finished %s : %s ' % (entity_name, entity_output))
    return HttpResponse(json.dumps({'data': entity_output}), content_type='application/json')


def ner(request):
    """This functionality calls the run_ner() functionality to tag the message .
    It is called through api call

    Attributes:
        request: url parameters

    """
    message = request.GET.get('message')
    entities_data = request.GET.get('entities', [])
    entities = []
    if entities_data:
        entities = ast.literal_eval(entities_data)
    ner_logger.debug('Start: %s -- %s' % (message, entities))
    output = run_ner(entities=entities, message=message)
    ner_logger.debug('Finished %s : %s ' % (message, output))
    return HttpResponse(json.dumps({'data': output}), content_type='application/json')


def combine_output(request):
    """This functionality calls the combine_output_of_detection_logic_and_tag()  through api call

    Attributes:
        request: url parameters

    """
    message = request.GET.get('message')
    entity_data = request.GET.get('entity_data', '{}')
    entity_data_json = json.loads(entity_data)
    ner_logger.debug('Start: %s ' % message)
    output = combine_output_of_detection_logic_and_tag(entity_data=entity_data_json, text=message)
    ner_logger.debug('Finished %s : %s ' % (message, output))
    return HttpResponse(json.dumps({'data': output}), content_type='application/json')

