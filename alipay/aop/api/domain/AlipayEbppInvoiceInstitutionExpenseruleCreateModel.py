#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ExpenseCtrRuleInfo import ExpenseCtrRuleInfo
from alipay.aop.api.domain.StandardConditionInfo import StandardConditionInfo


class AlipayEbppInvoiceInstitutionExpenseruleCreateModel(object):

    def __init__(self):
        self._account_id = None
        self._agreement_no = None
        self._consume_mode = None
        self._enterprise_id = None
        self._expense_ctrl_rule_info_list = None
        self._expense_type_sub_category = None
        self._institution_id = None
        self._open_rule_id = None
        self._payment_policy = None
        self._standard_condition_info_list = None
        self._standard_desc = None
        self._standard_name = None

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value
    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def consume_mode(self):
        return self._consume_mode

    @consume_mode.setter
    def consume_mode(self, value):
        self._consume_mode = value
    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def expense_ctrl_rule_info_list(self):
        return self._expense_ctrl_rule_info_list

    @expense_ctrl_rule_info_list.setter
    def expense_ctrl_rule_info_list(self, value):
        if isinstance(value, ExpenseCtrRuleInfo):
            self._expense_ctrl_rule_info_list = value
        else:
            self._expense_ctrl_rule_info_list = ExpenseCtrRuleInfo.from_alipay_dict(value)
    @property
    def expense_type_sub_category(self):
        return self._expense_type_sub_category

    @expense_type_sub_category.setter
    def expense_type_sub_category(self, value):
        self._expense_type_sub_category = value
    @property
    def institution_id(self):
        return self._institution_id

    @institution_id.setter
    def institution_id(self, value):
        self._institution_id = value
    @property
    def open_rule_id(self):
        return self._open_rule_id

    @open_rule_id.setter
    def open_rule_id(self, value):
        self._open_rule_id = value
    @property
    def payment_policy(self):
        return self._payment_policy

    @payment_policy.setter
    def payment_policy(self, value):
        self._payment_policy = value
    @property
    def standard_condition_info_list(self):
        return self._standard_condition_info_list

    @standard_condition_info_list.setter
    def standard_condition_info_list(self, value):
        if isinstance(value, list):
            self._standard_condition_info_list = list()
            for i in value:
                if isinstance(i, StandardConditionInfo):
                    self._standard_condition_info_list.append(i)
                else:
                    self._standard_condition_info_list.append(StandardConditionInfo.from_alipay_dict(i))
    @property
    def standard_desc(self):
        return self._standard_desc

    @standard_desc.setter
    def standard_desc(self, value):
        self._standard_desc = value
    @property
    def standard_name(self):
        return self._standard_name

    @standard_name.setter
    def standard_name(self, value):
        self._standard_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_id:
            if hasattr(self.account_id, 'to_alipay_dict'):
                params['account_id'] = self.account_id.to_alipay_dict()
            else:
                params['account_id'] = self.account_id
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.consume_mode:
            if hasattr(self.consume_mode, 'to_alipay_dict'):
                params['consume_mode'] = self.consume_mode.to_alipay_dict()
            else:
                params['consume_mode'] = self.consume_mode
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        if self.expense_ctrl_rule_info_list:
            if hasattr(self.expense_ctrl_rule_info_list, 'to_alipay_dict'):
                params['expense_ctrl_rule_info_list'] = self.expense_ctrl_rule_info_list.to_alipay_dict()
            else:
                params['expense_ctrl_rule_info_list'] = self.expense_ctrl_rule_info_list
        if self.expense_type_sub_category:
            if hasattr(self.expense_type_sub_category, 'to_alipay_dict'):
                params['expense_type_sub_category'] = self.expense_type_sub_category.to_alipay_dict()
            else:
                params['expense_type_sub_category'] = self.expense_type_sub_category
        if self.institution_id:
            if hasattr(self.institution_id, 'to_alipay_dict'):
                params['institution_id'] = self.institution_id.to_alipay_dict()
            else:
                params['institution_id'] = self.institution_id
        if self.open_rule_id:
            if hasattr(self.open_rule_id, 'to_alipay_dict'):
                params['open_rule_id'] = self.open_rule_id.to_alipay_dict()
            else:
                params['open_rule_id'] = self.open_rule_id
        if self.payment_policy:
            if hasattr(self.payment_policy, 'to_alipay_dict'):
                params['payment_policy'] = self.payment_policy.to_alipay_dict()
            else:
                params['payment_policy'] = self.payment_policy
        if self.standard_condition_info_list:
            if isinstance(self.standard_condition_info_list, list):
                for i in range(0, len(self.standard_condition_info_list)):
                    element = self.standard_condition_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.standard_condition_info_list[i] = element.to_alipay_dict()
            if hasattr(self.standard_condition_info_list, 'to_alipay_dict'):
                params['standard_condition_info_list'] = self.standard_condition_info_list.to_alipay_dict()
            else:
                params['standard_condition_info_list'] = self.standard_condition_info_list
        if self.standard_desc:
            if hasattr(self.standard_desc, 'to_alipay_dict'):
                params['standard_desc'] = self.standard_desc.to_alipay_dict()
            else:
                params['standard_desc'] = self.standard_desc
        if self.standard_name:
            if hasattr(self.standard_name, 'to_alipay_dict'):
                params['standard_name'] = self.standard_name.to_alipay_dict()
            else:
                params['standard_name'] = self.standard_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppInvoiceInstitutionExpenseruleCreateModel()
        if 'account_id' in d:
            o.account_id = d['account_id']
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'consume_mode' in d:
            o.consume_mode = d['consume_mode']
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'expense_ctrl_rule_info_list' in d:
            o.expense_ctrl_rule_info_list = d['expense_ctrl_rule_info_list']
        if 'expense_type_sub_category' in d:
            o.expense_type_sub_category = d['expense_type_sub_category']
        if 'institution_id' in d:
            o.institution_id = d['institution_id']
        if 'open_rule_id' in d:
            o.open_rule_id = d['open_rule_id']
        if 'payment_policy' in d:
            o.payment_policy = d['payment_policy']
        if 'standard_condition_info_list' in d:
            o.standard_condition_info_list = d['standard_condition_info_list']
        if 'standard_desc' in d:
            o.standard_desc = d['standard_desc']
        if 'standard_name' in d:
            o.standard_name = d['standard_name']
        return o


