from __future__ import absolute_import

import os
from . import BaseProxy
from ..requests import Request, FileRequest, POST
from ..exceptions import CoprValidationException


class ProjectProxy(BaseProxy):

    def get(self, ownername, projectname):
        endpoint = "/project"
        params = {
            "ownername": ownername,
            "projectname": projectname,
        }
        request = Request(endpoint, api_base_url=self.api_base_url, params=params)
        response = request.send()
        return response.munchify()

    def get_list(self, ownername, pagination=None):
        endpoint = "/project/list"
        params = {
            "ownername": ownername,
        }
        params.update(pagination.to_dict() if pagination else {})
        request = Request(endpoint, api_base_url=self.api_base_url, params=params)
        response = request.send()
        return response.munchify()

    def search(self, query, pagination=None):
        endpoint = "/project/search"
        params = {
            "query": query,
        }
        params.update(pagination.to_dict() if pagination else {})
        request = Request(endpoint, api_base_url=self.api_base_url, params=params)
        response = request.send()
        return response.munchify()

    def add(self, ownername, projectname, chroots, description=None, instructions=None, repos=None,
            disable_createrepo=False, unlisted_on_hp=False, enable_net=True, persistent=False,
            auto_prune=True, use_bootstrap_container=False):
        endpoint = "/project/add"
        params = {
            "ownername": ownername,
        }
        data = {
            "name": projectname,
            "chroots": chroots,
            "description": description,
            "instructions": instructions,
            "repos": repos,
            "disable_createrepo": disable_createrepo,
            "unlisted_on_hp": unlisted_on_hp,
            "enable_net": enable_net,
            "persistent": persistent,
            "auto_prune": auto_prune,
            "use_bootstrap_container": use_bootstrap_container,
        }
        request = Request(endpoint, api_base_url=self.api_base_url, method=POST,
                          params=params, data=data, auth=self.auth)
        response = request.send()
        return response.munchify()

    def edit(self, ownername, projectname, chroots=None, description=None, instructions=None, repos=None,
            disable_createrepo=False, unlisted_on_hp=False, enable_net=True, persistent=False,
            auto_prune=True, use_bootstrap_container=False):
        endpoint = "/project/edit"
        params = {
            "ownername": ownername,
            "projectname": projectname,
        }
        data = {
            "chroots": chroots,
            "description": description,
            "instructions": instructions,
            "repos": repos,
            "disable_createrepo": disable_createrepo,
            "unlisted_on_hp": unlisted_on_hp,
            "enable_net": enable_net,
            "persistent": persistent,
            "auto_prune": auto_prune,
            "use_bootstrap_container": use_bootstrap_container,
        }
        request = Request(endpoint, api_base_url=self.api_base_url, method=POST,
                          params=params, data=data, auth=self.auth)
        response = request.send()
        return response.munchify()

    def delete(self, ownername, projectname):
        endpoint = "/project/delete"
        params = {
            "ownername": ownername,
            "projectname": projectname,
        }
        data = {
            "verify": True,
        }
        request = Request(endpoint, api_base_url=self.api_base_url, method=POST,
                          params=params, data=data, auth=self.auth)
        response = request.send()
        return response.munchify()