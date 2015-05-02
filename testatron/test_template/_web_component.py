__author__ = 'anupama'
# Copyright 2014 Anupama Kattiparambil Prakasan
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.


import os

from testatron.test_template._component_loader import ComponentLoader
import _project_suite_globals as project_suite_globals
from robot.api import logger


class WebComponent(object):
    def __init__(self, class_path, json_path):
        package_name, class_name = get_package_and_class(class_path)
        logger.debug("package_name %s class_name : %s " % (package_name, class_name))
        logger.debug("cwd :%s " % os.getcwd())
        logger.debug("project_suite_globals.web_app :%s " % project_suite_globals.web_app)
        web_component_json_path = os.path.join(json_path)

        self.component_loader = ComponentLoader(web_component_json_path, package_name+".json", class_name)
        self.component_loader.load()
        logger.debug("component_loader.props "+str(self.component_loader.props))
        for key, element in self.component_loader.props.items():
            logger.debug(("key %s element %s" ) % (key, element))
            self.objectify(key, self.component_loader.props)
        logger.debug("self.__dict__ " +str(self.__dict__))
        self.s2l = self.component_loader.s2l
        self.driver = self.component_loader.driver
        # logger.debug(self.username

    def objectify(self, key, dict):
        self.__dict__[key] = dict [key]


def get_package_and_class(class_path):
    class_path = str(class_path)
    class_name = class_path[class_path.rfind('.')+1:-2]
    logger.debug("class_name "+class_name)
    module_name_without_class = class_path[:class_path.rfind('.')]
    logger.debug("module_name_without_class "+module_name_without_class)
    module_name = module_name_without_class[module_name_without_class .rfind('.')+1:]
    logger.debug("module_name "+module_name)
    package_name_without_module = module_name_without_class[:module_name_without_class.rfind('.')]
    logger.debug("package_name_without_module " +package_name_without_module)
    package_name = package_name_without_module[package_name_without_module .rfind('.')+1:]
    logger.debug("package_name "+package_name)
    return package_name, class_name



