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


from testatron.test_template.web_component import WebComponent


class LoginSpan(WebComponent):
    def __init__(self ):
        super(LoginSpan, self).__init__(self.__class__)

    def login(self, username, password):
        self.username.send_keys(username)
        self.password.send_keys(password)
        self.login_button.click()

# login = Login ("pre_login_home.json", "login-span")
# login.login("netsgr8_4us@yahoo.com" , "thisispassword")

