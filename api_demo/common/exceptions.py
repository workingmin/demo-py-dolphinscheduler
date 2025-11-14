#!/bin/env python3
# -*- coding: utf-8 -*-

class APIException(Exception):
    """Base exception for DolphinScheduler API errors"""
    pass

class APIRequestError(APIException):
    """Exception for API request failures"""
    pass

class APIResponseError(APIException):
    """Exception for API response errors"""
    def __init__(self, message, code=None):
        super().__init__(message)
        self.code = code