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
import os

# License header text
header = """# Copyright 2025 Nilesh Suthar
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
"""

# Directory to scan (current directory)
project_dir = "."

# Directories to exclude
exclude_dirs = {"venv", ".git", "__pycache__"}

for root, dirs, files in os.walk(project_dir):
    # Skip excluded directories
    dirs[:] = [d for d in dirs if d not in exclude_dirs]

    for file in files:
        if file.endswith(".py"):
            file_path = os.path.join(root, file)
            with open(file_path, "r+") as f:
                content = f.read()
                if not content.startswith("# Copyright"):
                    f.seek(0, 0)
                    f.write(header + content)
                    print(f"Added header to {file_path}")
