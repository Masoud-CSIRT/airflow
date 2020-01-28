# -*- coding: utf-8 -*-
# flake8: noqa
# Disable Flake8 because of all the sphinx imports
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.


# Airflow documentation build configuration file, created by
# sphinx-quickstart on Thu Oct  9 20:50:01 2014.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.
"""Configuration of Airflow Docs"""
import os
import sys
from typing import Dict

import airflow
from airflow.configuration import default_config_yaml

try:
    import sphinx_airflow_theme  # pylint: disable=unused-import
    airflow_theme_is_available = True
except ImportError:
    airflow_theme_is_available = False

autodoc_mock_imports = [
    'MySQLdb',
    'adal',
    'analytics',
    'azure',
    'azure.cosmos',
    'azure.datalake',
    'azure.mgmt',
    'boto3',
    'botocore',
    'bson',
    'cassandra',
    'celery',
    'cloudant',
    'cryptography',
    'cx_Oracle',
    'datadog',
    'distributed',
    'docker',
    'google',
    'google_auth_httplib2',
    'googleapiclient',
    'grpc',
    'hdfs',
    'httplib2',
    'jaydebeapi',
    'jenkins',
    'jira',
    'kubernetes',
    'msrestazure',
    'pandas',
    'pandas_gbq',
    'paramiko',
    'pinotdb',
    'psycopg2',
    'pydruid',
    'pyhive',
    'pyhive',
    'pymongo',
    'pymssql',
    'pysftp',
    'qds_sdk',
    'redis',
    'simple_salesforce',
    'slackclient',
    'smbclient',
    'snowflake',
    'sshtunnel',
    'tenacity',
    'vertica_python',
    'winrm',
    'zdesk',
]

# Hack to allow changing for piece of the code to behave differently while
# the docs are being built. The main objective was to alter the
# behavior of the utils.apply_default that was hiding function headers
os.environ['BUILDING_AIRFLOW_DOCS'] = 'TRUE'

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

sys.path.append(os.path.join(os.path.dirname(__file__), 'exts'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
    'sphinx.ext.graphviz',
    'sphinxarg.ext',
    'sphinxcontrib.httpdomain',
    'sphinxcontrib.jinja',
    'sphinx.ext.intersphinx',
    'autoapi.extension',
    'exampleinclude',
    'docroles',
    'removemarktransform',
]

autodoc_default_options = {
    'show-inheritance': True,
    'members': True
}

jinja_contexts = {
    'config_ctx': {"configs": default_config_yaml()}
}

viewcode_follow_imported_members = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Airflow'
# copyright = ''

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
# version = '1.0.0'
version = airflow.__version__
# The full version, including alpha/beta/rc tags.
# release = '1.0.0'
release = airflow.__version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = [
    '_api/airflow/_vendor',
    '_api/airflow/api',
    '_api/airflow/bin',
    '_api/airflow/cli',
    '_api/airflow/cli/command',
    '_api/airflow/config_templates',
    '_api/airflow/configuration',
    '_api/airflow/contrib/auth',
    '_api/airflow/contrib/example_dags',
    '_api/airflow/contrib/index.rst',
    '_api/airflow/contrib/kubernetes',
    '_api/airflow/contrib/task_runner',
    '_api/airflow/contrib/utils',
    '_api/airflow/dag',
    '_api/airflow/default_login',
    '_api/airflow/example_dags',
    '_api/airflow/exceptions',
    '_api/airflow/index.rst',
    '_api/airflow/jobs',
    '_api/airflow/lineage',
    '_api/airflow/typing_compat',
    '_api/airflow/logging_config',
    '_api/airflow/macros',
    '_api/airflow/migrations',
    '_api/airflow/plugins_manager',
    '_api/airflow/security',
    '_api/airflow/serialization',
    '_api/airflow/settings',
    '_api/airflow/sentry',
    '_api/airflow/stats',
    '_api/airflow/task',
    '_api/airflow/kubernetes',
    '_api/airflow/ti_deps',
    '_api/airflow/utils',
    '_api/airflow/version',
    '_api/airflow/www',
    '_api/main',
    '_api/airflow/gcp/index.rst',
    '_api/airflow/gcp/example_dags',
    '_api/airflow/gcp/utils',
    '_api/airflow/providers/amazon/aws/example_dags',
    '_api/airflow/providers/amazon/aws/index.rst',
    '_api/airflow/providers/amazon/index.rst',
    '_api/airflow/providers/apache/cassandra/index.rst',
    '_api/airflow/providers/apache/druid/index.rst',
    '_api/airflow/providers/apache/hdfs/index.rst',
    '_api/airflow/providers/apache/hive/index.rst',
    '_api/airflow/providers/apache/index.rst',
    '_api/airflow/providers/apache/pig/index.rst',
    '_api/airflow/providers/apache/pinot/index.rst',
    '_api/airflow/providers/apache/spark/index.rst',
    '_api/airflow/providers/apache/sqoop/index.rst',
    '_api/airflow/providers/celery/index.rst',
    '_api/airflow/providers/cloudant/index.rst',
    '_api/airflow/providers/cncf/index.rst',
    '_api/airflow/providers/cncf/kubernetes/index.rst',
    '_api/airflow/providers/databricks/index.rst',
    '_api/airflow/providers/datadog/index.rst',
    '_api/airflow/providers/dingding/index.rst',
    '_api/airflow/providers/discord/index.rst',
    '_api/airflow/providers/docker/index.rst',
    '_api/airflow/providers/email/index.rst',
    '_api/airflow/providers/ftp/index.rst',
    '_api/airflow/providers/google/cloud/example_dags',
    '_api/airflow/providers/google/cloud/index.rst',
    '_api/airflow/providers/google/index.rst',
    '_api/airflow/providers/google/marketing_platform/example_dags',
    '_api/airflow/providers/google/marketing_platform/index.rst',
    '_api/airflow/providers/google/suite/index.rst',
    '_api/airflow/providers/grpc/index.rst',
    '_api/airflow/providers/http/index.rst',
    '_api/airflow/providers/imap/index.rst',
    '_api/airflow/providers/index.rst',
    '_api/airflow/providers/jdbc/index.rst',
    '_api/airflow/providers/jenkins/index.rst',
    '_api/airflow/providers/jira/index.rst',
    '_api/airflow/providers/microsoft/azure/index.rst',
    '_api/airflow/providers/microsoft/index.rst',
    '_api/airflow/providers/microsoft/mssql/index.rst',
    '_api/airflow/providers/microsoft/winrm/index.rst',
    '_api/airflow/providers/mongo/index.rst',
    '_api/airflow/providers/mssql/index.rst',
    '_api/airflow/providers/mysql/index.rst',
    '_api/airflow/providers/odbc/index.rst',
    '_api/airflow/providers/openfass/index.rst',
    '_api/airflow/providers/opsgenie/index.rst',
    '_api/airflow/providers/oracle/index.rst',
    '_api/airflow/providers/pagerduty/index.rst',
    '_api/airflow/providers/papermill/index.rst',
    '_api/airflow/providers/postgres/index.rst',
    '_api/airflow/providers/presto/index.rst',
    '_api/airflow/providers/qubole/index.rst',
    '_api/airflow/providers/redis/index.rst',
    '_api/airflow/providers/salesforce/index.rst',
    '_api/airflow/providers/samba/index.rst',
    '_api/airflow/providers/segment/index.rst',
    '_api/airflow/providers/sftp/index.rst',
    '_api/airflow/providers/slack/index.rst',
    '_api/airflow/providers/snowflake/index.rst',
    '_api/airflow/providers/sqlite/index.rst',
    '_api/airflow/providers/ssh/index.rst',
    '_api/airflow/providers/vertica/index.rst',
    '_api/airflow/providers/zendesk/index.rst',
    '_api/base_serialization/index.rst',
    '_api/enums/index.rst',
    '_api/json_schema/index.rst',
    '_api/serialized_baseoperator/index.rst',
    '_api/serialized_dag/index.rst',
    'autoapi_templates',
    'howto/operator/gcp/_partials',
]

# The reST default role (used for this markup: `text`) to use for all
# documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
keep_warnings = True


intersphinx_mapping = {
    'boto3': ('https://boto3.amazonaws.com/v1/documentation/api/latest/', None),
    'mongodb': ('https://api.mongodb.com/python/current/', None),
    'pandas': ('https://pandas.pydata.org/pandas-docs/stable/', None),
    'python': ('https://docs.python.org/3/', None),
    'requests': ('https://requests.readthedocs.io/en/master/', None),
    'sqlalchemy': ('https://docs.sqlalchemy.org/en/latest/', None),
    'hdfs': ('https://hdfscli.readthedocs.io/en/latest/', None),
    # google-cloud-python
    'google-cloud-automl': ('https://googleapis.dev/python/automl/latest', None),
    'google-cloud-bigquery': ('https://googleapis.dev/python/bigquery/latest', None),
    'google-cloud-bigquery-datatransfer': ('https://googleapis.dev/python/bigquerydatatransfer/latest', None),
    'google-cloud-bigquery-storage': ('https://googleapis.dev/python/bigquerystorage/latest', None),
    'google-cloud-bigtable': ('https://googleapis.dev/python/bigtable/latest', None),
    'google-cloud-container': ('https://googleapis.dev/python/container/latest', None),
    'google-cloud-core': ('https://googleapis.dev/python/google-cloud-core/latest', None),
    'google-cloud-datastore': ('https://googleapis.dev/python/datastore/latest', None),
    'google-cloud-dlp': ('https://googleapis.dev/python/dlp/latest', None),
    'google-cloud-kms': ('https://googleapis.dev/python/cloudkms/latest', None),
    'google-cloud-language': ('https://googleapis.dev/python/language/latest', None),
    'google-cloud-pubsub': ('https://googleapis.dev/python/pubsub/latest', None),
    'google-cloud-redis': ('https://googleapis.dev/python/redis/latest', None),
    'google-cloud-spanner': ('https://googleapis.dev/python/spanner/latest', None),
    'google-cloud-speech': ('https://googleapis.dev/python/speech/latest', None),
    'google-cloud-storage': ('https://googleapis.dev/python/storage/latest', None),
    'google-cloud-tasks': ('https://googleapis.dev/python/cloudtasks/latest', None),
    'google-cloud-texttospeech': ('https://googleapis.dev/python/texttospeech/latest', None),
    'google-cloud-translate': ('https://googleapis.dev/python/translation/latest', None),
    'google-cloud-videointelligence': ('https://googleapis.dev/python/videointelligence/latest', None),
    'google-cloud-vision': ('https://googleapis.dev/python/vision/latest', None),
}

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'

if airflow_theme_is_available:
    html_theme = 'sphinx_airflow_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {}

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "Airflow Documentation"

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = ""

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = None

html_favicon = "../airflow/www/static/pin_32.png"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
# html_extra_path = []

# A list of JavaScript filename. The entry must be a filename string or a
# tuple containing the filename string and the attributes dictionary. The
# filename must be relative to the html_static_path, or a full URI with
# scheme like http://example.org/script.js.
html_js_files = ['jira-links.js']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
if airflow_theme_is_available:
    html_sidebars = {
        '**': [
            'version-selector.html',
            'searchbox.html',
            'globaltoc.html',
        ]
    }

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = False

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'Airflowdoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    # 'preamble': '',
}  # type: Dict[str,str]

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    ('index', 'Airflow.tex', 'Airflow Documentation',
     'Apache Airflow', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'airflow', 'Airflow Documentation',
     ['Apache Airflow'], 1)
]

# If true, show URL addresses after external links.
# man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [(
    'index', 'Airflow', 'Airflow Documentation',
    'Apache Airflow', 'Airflow',
    'Airflow is a system to programmatically author, schedule and monitor data pipelines.',
    'Miscellaneous'
), ]

# Documents to append as an appendix to all manuals.
# texinfo_appendices = []

# If false, no module index is generated.
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
# texinfo_no_detailmenu = False

# sphinx-autoapi configuration
# See:
# https://sphinx-autoapi.readthedocs.io/en/latest/config.html

# Paths (relative or absolute) to the source code that you wish to generate
# your API documentation from.
autoapi_dirs = [
    os.path.abspath('../airflow'),
]

# A directory that has user-defined templates to override our default templates.
autoapi_template_dir = 'autoapi_templates'

# A list of patterns to ignore when finding files
autoapi_ignore = [
    # These modules are backcompat shims, don't build docs for them
    '*/airflow/contrib/operators/s3_to_gcs_transfer_operator.py',
    '*/airflow/contrib/operators/gcs_to_gcs_transfer_operator.py',
    '*/airflow/contrib/operators/gcs_to_gcs_transfer_operator.py',
    '*/airflow/kubernetes/kubernetes_request_factory/*',
    '*/airflow/contrib/sensors/*',
    '*/airflow/contrib/hooks/*',

    '*/node_modules/*',
    '*/migrations/*',
]
# Keep the AutoAPI generated files on the filesystem after the run.
# Useful for debugging.
autoapi_keep_files = True

# Relative path to output the AutoAPI files into. This can also be used to place the generated documentation
# anywhere in your documentation hierarchy.
autoapi_root = '_api'

# -- Options for example include ------------------------------------------
exampleinclude_sourceroot = os.path.abspath('..')

# -- Additional HTML Context variable
html_context = {
    # Google Analytics ID.
    # For more information look at:
    # https://github.com/readthedocs/sphinx_rtd_theme/blob/master/sphinx_rtd_theme/layout.html#L222-L232
    'theme_analytics_id': 'UA-140539454-1',
    # Variables used to build a button for editing the source code
    #
    # The path is created according to the following template:
    #
    # https://{{ github_host|default("github.com") }}/{{ github_user }}/{{ github_repo }}/
    # {{ theme_vcs_pageview_mode|default("blob") }}/{{ github_version }}{{ conf_py_path }}
    # {{ pagename }}{{ suffix }}
    #
    # More information:
    # https://github.com/readthedocs/readthedocs.org/blob/master/readthedocs/doc_builder/templates/doc_builder/conf.py.tmpl#L100-L103
    # https://github.com/readthedocs/sphinx_rtd_theme/blob/master/sphinx_rtd_theme/breadcrumbs.html#L45
    #
    'theme_vcs_pageview_mode': 'edit',
    'conf_py_path': '/docs/',
    'github_user': 'apache',
    'github_repo': 'airflow',
    'github_version': os.environ.get('GITHUB_TREE', None),
    'display_github': os.environ.get('GITHUB_TREE', None) is not None,
}
