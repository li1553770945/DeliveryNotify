import time

import json
import logging
from delivery.delivery import Delivery
from delivery.ems_apple import EmsApple
from notify.notify import Notify

logger = logging.getLogger(__name__)
logger.setLevel("INFO")
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


def read_json(filename):
    with open(filename, 'r', encoding='utf-8') as fp:
        return json.load(fp)


def send_notification():
    pass


def main():
    deliveries = read_json("json/deliveries.json")
    settings = read_json("json/settings.json")

    if len(deliveries) == 0:
        logger.warning("快递信息为空")
        return

    query_list = list()
    for deliver in deliveries:
        deliver_type = deliver['type']
        number = deliver['number']

        if deliver_type not in delivery_classes:
            logger.critical("快递类型：\"{}\"未知".format(deliver_type))
            return
        query_list.append(delivery_classes[deliver_type](number))

    notify_list = list()
    for notify in settings["notifications"]:
        notify_type = notify['type']
        key = notify['key']

        if notify_type not in notify_classes:
            logger.critical("通知类型：\"{}\"未知".format(notify_type))
            return
        notify_list.append(notify_classes[notify_type](key))

    while True:
        logger.info("查询中...")
        for query in query_list:
            result = query.get_notification()
            error = result.error
            have_update = result.have_update
            latest_msg = result.latest_msg
            if result.error != "":
                logger.critical("{}查询失败:{}".format(query.number, error))
                return

            if have_update:
                logger.info("{}变更通知:{}".format(query.number, latest_msg))
                for notify in notify_list:
                    notify.send("{}变更通知".format(query.number), latest_msg)
            else:
                logger.info("{}无变更，目前最新消息：:{}".format(query.number, latest_msg))

        time.sleep(settings['query_interval'])


if __name__ == '__main__':
    notify_classes = {
        "console": Notify,
    }
    delivery_classes = {
        "test": Delivery,
        "ems-apple": EmsApple,
    }
    main()
