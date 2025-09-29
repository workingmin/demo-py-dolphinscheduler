#!/bin/env python3
# -*- coding: utf-8 -*-

import os
import dotenv

def load_config():
    """
    Load configuration from environment variables
    
    Returns:
        Tuple of (server_url, user_token)
        
    Raises:
        ValueError if required configuration is missing
    """
    # Load .env file if exists
    dotenv.load_dotenv()
    
    server_url = os.getenv('DOLPHINSCHEDULER_SERVER_URL')
    user_token = os.getenv('DOLPHINSCHEDULER_USER_TOKEN')
    
    if not server_url:
        raise ValueError("Missing DolphinScheduler server URL (DOLPHINSCHEDULER_SERVER_URL)")
    if not user_token:
        raise ValueError("Missing user authentication token (DOLPHINSCHEDULER_USER_TOKEN)")
    
    return server_url, user_token