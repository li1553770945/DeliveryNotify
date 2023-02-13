import json
import logging

logger = logging.getLogger(__name__)
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

        if deliver_type not in query_classes:
            logger.critical("快递类型：\"{}\"未知".format(deliver_type))
            return
        query_list.append(query_classes[deliver_type](number))

    notify_list = list()
    for notify in settings["notifications"]:
        notify_type = notify['type']
        key = notify['key']

        if notify_type not in notify_classes:
            logger.critical("通知类型：\"{}\"未知".format(notify_type))
            return
        query_list.append(query_classes[notify_type](key))

    while True:
        for query in query_list:
            result = query.get_notification()
            if result.error_msg != "":
                logger.critical("{}查询失败:{}".format(query.main_no,result.error_msg))
                return

            if result.msg != "":
                for notify in notify_list:
                    notify.send("{}变更通知".format(query.main_no),result.msg)



if __name__ == '__main__':
    notify_classes = {

    }
    query_classes = {

    }
    main()
