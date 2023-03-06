from get_some_advice import main_get_advice
from yandex_translate import translate
import logging


def get_advice(amount_advice: int) -> list[str]:
    logging.info('start get_advice')
    advice = main_get_advice(amount_advice)
    logging.info(f'complete get_advice\nresult: {advice}')
    return advice


def translate_advice(en_advice: list[str]) -> list[str]:
    logging.info('start translate_advice')
    ru_advice = translate(en_advice)
    logging.info(f'complete get_advice\nresult: {ru_advice}')
    return ru_advice


def print_advice(ru_advice: list[str]) -> None:
    logging.info('start print_advice')
    for advice in ru_advice:
        logging.info(f'advice: {advice}')
        print(advice)
    logging.info('complete print_advice')


def ret_advice(ru_advice: list[str]) -> str:
    text_advice = ''
    for i, advice in enumerate(ru_advice):
        text_advice += f'Совет {i+1}:\n{advice}\n\n'
    return text_advice

def main(amount_advice=1):
    if not isinstance(amount_advice, int):
        logging.warning('input error in f main\nvalue amount_advice was change: amount_advice = 1')
        amount_advice = 1
    return ret_advice(translate_advice(get_advice(amount_advice)))



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filename='py_log.log', filemode='w')
    main(3)
