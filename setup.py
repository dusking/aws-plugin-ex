########
# Copyright (c) 2015 GigaSpaces Technologies Ltd. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
#    * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    * See the License for the specific language governing permissions and
#    * limitations under the License.


from setuptools import setup

# Replace the place holders with values for your project

setup(

    # Do not use underscores in the plugin name.
    name='cloudify-aws-ext',
    author='dusking',
    author_email='',

    version='0.0.2',
    description='Cloudify plugin for AWS infrastructure.',

    # This must correspond to the actual packages in the plugin.
    packages=[
        'cloudify_aws_ec2_ext'
    ],

    license='LICENSE',
    install_requires=[
        'cloudify-plugins-common>=3.3.1',
        'boto==2.38.0',
        'pycrypto==2.6.1'
        # 'cloudify-aws-plugin==1.4.3'
    ]
)