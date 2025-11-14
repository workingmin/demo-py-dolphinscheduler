#!/bin/env python3
# -*- coding: utf-8 -*-

from common.api.base_api import BaseAPI
from typing import Dict, List, Optional, Union

class ProjectAPI(BaseAPI):
    def create_project(self, project_name: str, description: str = "", version: str = "v1") -> Dict:
        """
        Create a new project
        
        Args:
            project_name: Name of the project
            description: Project description (optional)
            version: API version to use (v1 or v2)
        
        Returns:
            Created project data
        
        Raises:
            ValueError: If invalid version is provided
        """
        endpoint = f"{version}/projects" if version == "v2" else "projects"
        
        if version == "v1":
            params = {"projectName": project_name, "description": description}
            return self._post_request(endpoint, params=params, operation_name="Project creation")
        else:
            json_data = {"projectName": project_name, "description": description}
            return self._post_request(endpoint, json_data=json_data, operation_name="Project creation (v2)")

    def get_project(self, project_code: Union[str, int], version: str = "v1") -> Dict:
        """
        Get project information by project code
        
        Args:
            project_code: Project code identifier
            version: API version to use (v1 or v2)
        
        Returns:
            Project information
        """
        endpoint = f"{version}/projects/{project_code}" if version == "v2" else f"projects/{project_code}"
        return self._get_request(endpoint, f"Query project {project_code}")

    def delete_project(self, project_code: Union[str, int], version: str = "v1") -> Dict:
        """
        Delete a project by project code
        
        Args:
            project_code: Project code identifier
            version: API version to use (v1 or v2)
        
        Returns:
            Delete operation result
        """
        endpoint = f"{version}/projects/{project_code}" if version == "v2" else f"projects/{project_code}"
        return self._delete_request(endpoint, f"Delete project {project_code}")

    def update_project(self, project_code: Union[str, int],
                       project_name: Optional[str] = None, 
                       description: Optional[str] = None,
                       version: str = "v1") -> Dict:
        """
        Update project information
        
        Args:
            project_code: Project code identifier
            project_name: New project name (optional)
            description: New description (optional)
            version: API version to use (v1 or v2)
        
        Returns:
            Updated project data
        """
        if project_name is None and description is None:
            raise ValueError("At least one of project_name or description must be provided")
        
        endpoint = f"{version}/projects/{project_code}" if version == "v2" else f"projects/{project_code}"
        
        if version == "v1":
            params = {}
            if project_name is not None:
                params["projectName"] = project_name
            if description is not None:
                params["description"] = description
            return self._put_request(endpoint, params=params, operation_name=f"Update project {project_code}")
        else:
            json_data = {}
            if project_name is not None:
                json_data["projectName"] = project_name
            if description is not None:
                json_data["description"] = description
            return self._put_request(endpoint, json_data=json_data, operation_name=f"Update project {project_code}")

    def list_all_projects(self, version: str = "v1") -> List[Dict]:
        """
        List all projects (requires admin privileges)
        
        Args:
            version: API version to use (v1 or v2)
        
        Returns:
            List of all projects
        """
        endpoint = f"{version}/projects/list" if version == "v2" else "projects/list"
        return self._get_request(endpoint, "List all projects")

    def list_user_projects(self, version: str = "v1") -> List[Dict]:
        """
        List projects created by and authorized to the current user
        
        Args:
            version: API version to use (v1 or v2)
        
        Returns:
            List of authorized projects
        """
        endpoint = f"{version}/projects/created-and-authed" if version == "v2" else "projects/created-and-authed"
        return self._get_request(endpoint, "List user projects")
