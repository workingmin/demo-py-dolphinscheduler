#!/bin/env python3
# -*- coding: utf-8 -*-

import os
import requests
from urllib.parse import urljoin
from common.exceptions import APIRequestError, APIResponseError
from typing import Dict, Optional, Any
import dotenv

class BaseAPI:
    def __init__(self, server_url: Optional[str] = None, user_token: Optional[str] = None):
        """
        Base API client for DolphinScheduler
        
        Args:
            server_url: DolphinScheduler server URL
            user_token: User authentication token
        """
        # Load .env file if exists
        dotenv.load_dotenv()
        
        self.server_url = server_url or os.getenv('DOLPHINSCHEDULER_SERVER_URL')
        self.user_token = user_token or os.getenv('DOLPHINSCHEDULER_USER_TOKEN')
        self.headers = {'token': self.user_token} if self.user_token else {}
        
        if not self.server_url:
            raise ValueError("Missing DolphinScheduler server URL")
        if not self.user_token:
            raise ValueError("Missing user authentication token")
    
    def _request(self, method: str, endpoint: str, 
                 params: Optional[Dict] = None, 
                 json_data: Optional[Dict] = None) -> Dict:
        """
        Internal method for making API requests
        
        Args:
            method: HTTP method (GET, POST, PUT, DELETE)
            endpoint: API endpoint (relative path)
            params: Query parameters
            json_data: JSON payload for POST/PUT requests
            
        Returns:
            Parsed JSON response
            
        Raises:
            APIRequestError: For network or HTTP errors
        """
        url = urljoin(f"{self.server_url}/", endpoint)
        
        try:
            response = requests.request(
                method=method,
                url=url,
                headers=self.headers,
                params=params,
                json=json_data
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            status_code = e.response.status_code if e.response else "N/A"
            raise APIRequestError(
                f"API request to {url} failed [Status: {status_code}]: {str(e)}"
            ) from e
        except ValueError as e:
            raise APIRequestError(
                f"Failed to parse JSON response from {url}: {str(e)}"
            ) from e

    def _handle_response(self, response: Dict, operation_name: str) -> Any:
        """
        Handle API response and check for errors
        
        Args:
            response: API response JSON
            operation_name: Name of the operation for error messages
            
        Returns:
            Response data if successful
            
        Raises:
            APIResponseError: If API indicates failure
        """
        if not isinstance(response, dict):
            raise APIResponseError(
                f"{operation_name} failed: Invalid response format"
            )
        
        if 'success' not in response:
            raise APIResponseError(
                f"{operation_name} failed: Missing 'success' field in response"
            )
        
        if not response.get('success') or response.get('failed'):
            code = response.get('code', 'UNKNOWN')
            msg = response.get('msg', 'No error message provided')
            raise APIResponseError(
                f"{operation_name} failed [Code: {code}]: {msg}",
                code=code
            )
        
        return response.get('data')
    
    def _post_request(self, endpoint: str,
                      params: Optional[Dict] = None, 
                      json_data: Optional[Dict] = None, 
                      operation_name: str = "Operation") -> Dict:
        """
        Internal method for POST requests
        
        Args:
            endpoint: API endpoint
            params: Query parameters
            json_data: JSON payload
            operation_name: Operation name for error messages
        
        Returns:
            Response data
        """
        try:
            response = self._request('POST', endpoint, params=params, json_data=json_data)
            return self._handle_response(response, operation_name)
        except (APIRequestError, APIResponseError) as e:
            raise type(e)(f"{operation_name} failed: {str(e)}") from e

    def _get_request(self, endpoint: str, 
                     params: Optional[Dict] = None, 
                     operation_name: str = "Operation") -> Dict:
        """
        Internal method for GET requests
        
        Args:
            endpoint: API endpoint
            params: Query parameters
            operation_name: Operation name for error messages
        
        Returns:
            Response data
        """
        try:
            response = self._request('GET', endpoint, params=params)
            return self._handle_response(response, operation_name)
        except (APIRequestError, APIResponseError) as e:
            raise type(e)(f"{operation_name} failed: {str(e)}") from e

    def _put_request(self, endpoint: str, 
                     params: Optional[Dict] = None, 
                     json_data: Optional[Dict] = None, 
                     operation_name: str = "Operation") -> Dict:
        """
        Internal method for PUT requests
        
        Args:
            endpoint: API endpoint
            params: Query parameters
            json_data: JSON payload
            operation_name: Operation name for error messages
        
        Returns:
            Response data
        """
        try:
            response = self._request('PUT', endpoint, params=params, json_data=json_data)
            return self._handle_response(response, operation_name)
        except (APIRequestError, APIResponseError) as e:
            raise type(e)(f"{operation_name} failed: {str(e)}") from e

    def _delete_request(self, endpoint: str, operation_name: str = "Operation") -> Dict:
        """
        Internal method for DELETE requests
        
        Args:
            endpoint: API endpoint
            operation_name: Operation name for error messages
        
        Returns:
            Response data
        """
        try:
            response = self._request('DELETE', endpoint)
            return self._handle_response(response, operation_name)
        except (APIRequestError, APIResponseError) as e:
            raise type(e)(f"{operation_name} failed: {str(e)}") from e