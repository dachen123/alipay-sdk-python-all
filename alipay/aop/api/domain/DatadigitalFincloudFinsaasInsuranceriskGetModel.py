#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DatadigitalFincloudFinsaasInsuranceriskGetModel(object):

    def __init__(self):
        self._cert_no_code = None
        self._data_type = None
        self._telephone_num = None

    @property
    def cert_no_code(self):
        return self._cert_no_code

    @cert_no_code.setter
    def cert_no_code(self, value):
        self._cert_no_code = value
    @property
    def data_type(self):
        return self._data_type

    @data_type.setter
    def data_type(self, value):
        self._data_type = value
    @property
    def telephone_num(self):
        return self._telephone_num

    @telephone_num.setter
    def telephone_num(self, value):
        self._telephone_num = value


    def to_alipay_dict(self):
        params = dict()
        if self.cert_no_code:
            if hasattr(self.cert_no_code, 'to_alipay_dict'):
                params['cert_no_code'] = self.cert_no_code.to_alipay_dict()
            else:
                params['cert_no_code'] = self.cert_no_code
        if self.data_type:
            if hasattr(self.data_type, 'to_alipay_dict'):
                params['data_type'] = self.data_type.to_alipay_dict()
            else:
                params['data_type'] = self.data_type
        if self.telephone_num:
            if hasattr(self.telephone_num, 'to_alipay_dict'):
                params['telephone_num'] = self.telephone_num.to_alipay_dict()
            else:
                params['telephone_num'] = self.telephone_num
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DatadigitalFincloudFinsaasInsuranceriskGetModel()
        if 'cert_no_code' in d:
            o.cert_no_code = d['cert_no_code']
        if 'data_type' in d:
            o.data_type = d['data_type']
        if 'telephone_num' in d:
            o.telephone_num = d['telephone_num']
        return o


