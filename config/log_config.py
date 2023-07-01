import logging

log = logging.getLogger(__name__)
logging.basicConfig(
    filename='test.log',
    level=logging.DEBUG,
    format='%(asctime)s:%(levelname)s:%(message)s'
)
