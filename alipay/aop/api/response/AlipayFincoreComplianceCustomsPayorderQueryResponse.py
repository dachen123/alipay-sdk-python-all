#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFincoreComplianceCustomsPayorderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFincoreComplianceCustomsPayorderQueryResponse, self).__init__()
        self._cert_no = None
        self._cert_type = None
        self._email = None
        self._mobile = None
        self._user_name = None

    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayFincoreComplianceCustomsPayorderQueryResponse, self).parse_response_content(response_content)
        if 'cert_no' in response:
            self.cert_no = response['cert_no']
        if 'cert_type' in response:
            self.cert_type = response['cert_type']
        if 'email' in response:
            self.email = response['email']
        if 'mobile' in response:
            self.mobile = response['mobile']
        if 'user_name' in response:
            self.user_name = response['user_name']
