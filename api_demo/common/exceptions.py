#!/bin/env python3
# -*- coding: utf-8 -*-

class DolphinSchedulerError(Exception):
    """Base exception for DolphinScheduler API errors"""
    pass

class APIRequestError(DolphinSchedulerError):
    """Exception for API request failures"""
    pass

class APIResponseError(DolphinSchedulerError):
    """Exception for API response errors"""
    def __init__(self, message, code=None):
        super().__init__(message)
        self.code = code