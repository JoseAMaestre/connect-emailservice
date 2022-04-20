# -*- coding: utf-8 -*-
#
# Copyright (c) 2022, Jose Antonio Maestre
# All rights reserved.
#

from emailservice_connect_ext.extension import EmailServiceExtension


def test_process_asset_purchase_request(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = EmailServiceExtension(client, logger, config)
    result = ext.process_asset_purchase_request(request)
    assert result.status == 'success'
