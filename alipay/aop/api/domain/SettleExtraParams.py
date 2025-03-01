#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SettleExtraParams(object):

    def __init__(self):
        self._quit_type = None
        self._settle_adjust_reason = None

    @property
    def quit_type(self):
        return self._quit_type

    @quit_type.setter
    def quit_type(self, value):
        self._quit_type = value
    @property
    def settle_adjust_reason(self):
        return self._settle_adjust_reason

    @settle_adjust_reason.setter
    def settle_adjust_reason(self, value):
        self._settle_adjust_reason = value


    def to_alipay_dict(self):
        params = dict()
        if self.quit_type:
            if hasattr(self.quit_type, 'to_alipay_dict'):
                params['quit_type'] = self.quit_type.to_alipay_dict()
            else:
                params['quit_type'] = self.quit_type
        if self.settle_adjust_reason:
            if hasattr(self.settle_adjust_reason, 'to_alipay_dict'):
                params['settle_adjust_reason'] = self.settle_adjust_reason.to_alipay_dict()
            else:
                params['settle_adjust_reason'] = self.settle_adjust_reason
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SettleExtraParams()
        if 'quit_type' in d:
            o.quit_type = d['quit_type']
        if 'settle_adjust_reason' in d:
            o.settle_adjust_reason = d['settle_adjust_reason']
        return o


