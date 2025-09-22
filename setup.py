# Copyright 2025 Nilesh Suthar
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from setuptools import setup, find_packages

setup(
    name="prism",
    version="0.1.0",
    description="Prism: an event-driven backtesting engine for trading strategies",
    author="Nilesh Suthar",
    license="Apache 2.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pandas",
        "numpy",
        "pydantic",
        "matplotlib",
        "pytest"
    ],
    python_requires=">=3.9",
)
