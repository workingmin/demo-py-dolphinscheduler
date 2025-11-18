#!/bin/env python3
# -*- coding: utf-8 -*-

from common.api.base_api import BaseAPI
from typing import Dict, List, Optional, Union

class DatasourceAPI(BaseAPI):
    def create_datasource(self, 
                         datasource_type: str,
                         name: str,
                         host: str,
                         port: int,
                         username: str,
                         password: str,
                         database: str,
                         note: str = "",
                         other: Optional[Dict] = None) -> Dict:
        """
        Create a new datasource
        
        Args:
            datasource_type: Type of datasource (e.g. MYSQL)
            name: Datasource name (must be unique)
            host: Database host
            port: Database port
            username: Database username
            password: Database password
            database: Database name
            note: Optional description
            other: Additional connection parameters
            
        Returns:
            Created datasource data with ID
        """
        endpoint = "datasources"
        json_data = {
            "type": datasource_type,
            "name": name,
            "note": note,
            "host": host,
            "port": port,
            "userName": username,
            "password": password,
            "database": database,
            "other": other or {}
        }
        return self._post_request(endpoint, json_data=json_data, operation_name="Datasource creation")

    def get_datasource(self, datasource_id: Union[str, int]) -> Dict:
        """
        Get datasource information by ID
        
        Args:
            datasource_id: Datasource identifier (numeric ID or string)
            
        Returns:
            Datasource details including type, connection info, etc.
        """
        endpoint = f"datasources/{datasource_id}"
        return self._get_request(endpoint, operation_name=f"Query datasource {datasource_id}")

    def update_datasource(self, 
                         datasource_id: Union[str, int],
                         datasource_type: str,
                         name: str,
                         host: str,
                         port: int,
                         username: str,
                         password: str,
                         database: str,
                         note: str = "",
                         other: Optional[Dict] = None) -> Dict:
        """
        Update datasource information
        
        Args:
            datasource_id: Datasource identifier
            datasource_type: Type of datasource (e.g. MYSQL)
            name: Datasource name
            host: Database host
            port: Database port
            username: Database username
            password: Database password
            database: Database name
            note: Optional description
            other: Additional connection parameters
            
        Returns:
            Updated datasource data
        """
        endpoint = f"datasources/{datasource_id}"
        json_data = {
            "type": datasource_type,
            "name": name,
            "note": note,
            "host": host,
            "port": port,
            "userName": username,
            "password": password,
            "database": database,
            "other": other or {}
        }
        return self._put_request(endpoint, json_data=json_data, operation_name=f"Update datasource {datasource_id}")

    def delete_datasource(self, datasource_id: Union[str, int]) -> Dict:
        """
        Delete a datasource by ID
        
        Args:
            datasource_id: Datasource identifier
            
        Returns:
            Delete operation result with success status
        """
        endpoint = f"datasources/{datasource_id}"
        return self._delete_request(endpoint, operation_name=f"Delete datasource {datasource_id}")

    def list_datasources_by_type(self, datasource_type: str) -> List[Dict]:
        """
        List datasources by database type
        
        Args:
            datasource_type: Type of datasource (e.g. MYSQL, POSTGRESQL)
            
        Returns:
            List of datasources with basic info
        """
        endpoint = "datasources/list"
        params = {"type": datasource_type}
        return self._get_request(endpoint, params=params, operation_name=f"List {datasource_type} datasources")

    def connect_test_datasource(self, datasource_id: Union[str, int]) -> Dict:
        """
        Test connection to a datasource
        
        Args:
            datasource_id: Datasource identifier
            
        Returns:
            Connection test result with success status
        """
        endpoint = f"datasources/{datasource_id}/connect-test"
        return self._get_request(endpoint, operation_name=f"Test connection for datasource {datasource_id}")

    def connect_datasource(self, datasource_param: Dict) -> Dict:
        """
        Test connection to a datasource with provided parameters
        
        Args:
            datasource_param: Complete datasource parameters including:
                - type: Database type (e.g. MYSQL, POSTGRESQL)
                - name: Datasource name (optional for connection test)
                - host: Database host
                - port: Database port
                - userName: Database username
                - password: Database password
                - database: Database name
                - other: Additional connection parameters
                
        Returns:
            Connection test result with success status and detailed error information if failed
        """
        endpoint = "datasources/connect"
        return self._post_request(endpoint, json_data=datasource_param, operation_name="Test datasource connection")

    def verify_datasource_name(self, name: str) -> Dict:
        """
        Verify if a datasource name is available
        
        Args:
            name: Datasource name to verify
            
        Returns:
            Dictionary with verification result and availability status
        """
        endpoint = "datasources/verify-name"
        params = {"name": name}
        return self._get_request(endpoint, params=params, operation_name=f"Verify datasource name '{name}'")

    def list_databases(self, datasource_id: Union[str, int]) -> List[str]:
        """
        List all databases available in the datasource
        
        Args:
            datasource_id: ID of the datasource (can be string or integer)
            
        Returns:
            List of database names with additional metadata
            
        Raises:
            APIError: If the request fails or datasource doesn't exist
        """
        endpoint = "datasources/databases"
        params = {"datasourceId": datasource_id}
        return self._get_request(endpoint, params=params, operation_name=f"List databases for datasource {datasource_id}")
    def list_tables(self, datasource_id: Union[str, int], database_name: str) -> List[Dict]:
        """
        List all tables in a specific database of the datasource
        
        Args:
            datasource_id: ID of the datasource (can be string or integer)
            database_name: Name of the database to query
            
        Returns:
            List of table names with additional metadata
            
        Raises:
            APIError: If the请求失败或数据源/数据库不存在
        """
        endpoint = "datasources/tables"
        params = {
            "datasourceId": datasource_id,
            "database": database_name
        }
        return self._get_request(endpoint, params=params, operation_name=f"List tables in {database_name}")

    def list_columns(self, datasource_id: Union[str, int], database_name: str, table_name: str) -> List[Dict]:
        """
        List all columns of a specific table
        
        Args:
            datasource_id: ID of the datasource (can be string or integer)
            database_name: Name of the database containing the table
            table_name: Name of the table to inspect
            
        Returns:
            List of column definitions with detailed metadata
            
        Raises:
            APIError: If the request fails or table doesn't exist
        """
        endpoint = "datasources/tableColumns"
        params = {
            "datasourceId": datasource_id,
            "database": database_name,
            "tableName": table_name
        }
        return self._get_request(endpoint, params=params, operation_name=f"List columns in table {table_name}")