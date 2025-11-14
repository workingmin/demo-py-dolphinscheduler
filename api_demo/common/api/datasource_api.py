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
            name: Datasource name
            host: Database host
            port: Database port
            username: Database username
            password: Database password
            database: Database name
            note: Optional description
            other: Additional connection parameters
            
        Returns:
            Created datasource data
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
            datasource_id: Datasource identifier
            
        Returns:
            Datasource information
        """
        endpoint = f"datasources/{datasource_id}"
        return self._get_request(endpoint, f"Query datasource {datasource_id}")

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
            Delete operation result
        """
        endpoint = f"datasources/{datasource_id}"
        return self._delete_request(endpoint, f"Delete datasource {datasource_id}")

    def list_datasources_by_type(self, datasource_type: str) -> List[Dict]:
        """
        List datasources by database type
        
        Args:
            datasource_type: Type of datasource (e.g. MYSQL)
            
        Returns:
            List of datasources
        """
        endpoint = f"datasources/list/{datasource_type}"
        return self._get_request(endpoint, f"List {datasource_type} datasources")

    def verify_datasource(self, datasource_id: Union[str, int]) -> Dict:
        """
        Verify datasource connection
        
        Args:
            datasource_id: Datasource identifier
            
        Returns:
            Verification result
        """
        endpoint = f"datasources/{datasource_id}/verify"
        return self._get_request(endpoint, f"Verify datasource {datasource_id}")

    def get_datasource_databases(self, datasource_id: Union[str, int]) -> List[str]:
        """
        Get databases available in datasource
        
        Args:
            datasource_id: Datasource identifier
            
        Returns:
            List of database names
        """
        endpoint = f"datasources/{datasource_id}/databases"
        return self._get_request(endpoint, f"Get databases for datasource {datasource_id}")

    def get_datasource_tables(self, datasource_id: Union[str, int], database_name: str) -> List[str]:
        """
        Get tables in a database
        
        Args:
            datasource_id: Datasource identifier
            database_name: Database name
            
        Returns:
            List of table names
        """
        endpoint = f"datasources/{datasource_id}/tables"
        params = {"database": database_name}
        return self._get_request(endpoint, f"Get tables for database {database_name}", params=params)

    def get_table_columns(self, datasource_id: Union[str, int], database_name: str, table_name: str) -> List[Dict]:
        """
        Get columns in a table
        
        Args:
            datasource_id: Datasource identifier
            database_name: Database name
            table_name: Table name
            
        Returns:
            List of column definitions
        """
        endpoint = f"datasources/{datasource_id}/columns"
        params = {"database": database_name, "table": table_name}
        return self._get_request(endpoint, f"Get columns for table {table_name}", params=params)