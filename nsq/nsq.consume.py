import nsq


def handler(message):
    print message
    print message.body
    return True


r = nsq.Reader(message_handler=handler, nsqd_tcp_addresses=['10.255.175.48:4150'], topic='test_topic', channel='asdfxx',
               lookupd_poll_interval=15)

nsq.run()  # tornado.ioloop.IOLoop.instance().start()