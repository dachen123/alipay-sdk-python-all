#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustryNucleicremindSubscribeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryNucleicremindSubscribeQueryResponse, self).__init__()
        self._effective_hour = None
        self._result_time = None
        self._status = None

    @property
    def effective_hour(self):
        return self._effective_hour

    @effective_hour.setter
    def effective_hour(self, value):
        self._effective_hour = value
    @property
    def result_time(self):
        return self._result_time

    @result_time.setter
    def result_time(self, value):
        self._result_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryNucleicremindSubscribeQueryResponse, self).parse_response_content(response_content)
        if 'effective_hour' in response:
            self.effective_hour = response['effective_hour']
        if 'result_time' in response:
            self.result_time = response['result_time']
        if 'status' in response:
            self.status = response['status']
