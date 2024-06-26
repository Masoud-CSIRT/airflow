 .. Licensed to the Apache Software Foundation (ASF) under one
    or more contributor license agreements.  See the NOTICE file
    distributed with this work for additional information
    regarding copyright ownership.  The ASF licenses this file
    to you under the Apache License, Version 2.0 (the
    "License"); you may not use this file except in compliance
    with the License.  You may obtain a copy of the License at

 ..   http://www.apache.org/licenses/LICENSE-2.0

 .. Unless required by applicable law or agreed to in writing,
    software distributed under the License is distributed on an
    "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
    KIND, either express or implied.  See the License for the
    specific language governing permissions and limitations
    under the License.

Deprecated REST API
===================

.. warning::

  This REST API is deprecated since version 2.0. Please consider using the :doc:`stable REST API <stable-rest-api-ref>`.
  For more information on migration, see `UPDATING.md <https://airflow.apache.org/docs/apache-airflow/stable/howto/upgrading-from-1-10/>`_

.. warning::

  Please note that these API endpoints do not have access control. An authenticated user has full access.


Before Airflow 2.0 this REST API was known as the "experimental" API, but now that the :doc:`stable REST API <stable-rest-api-ref>` is available, it has been renamed.

The endpoints for this API are available at ``/api/experimental/``.

.. versionchanged:: 2.0

  This REST API is disabled by default. To restore these APIs while migrating to
  the stable REST API, set ``enable_experimental_api`` option in ``[api]`` section to ``True``.

Endpoints
---------

.. http:post:: /api/experimental/dags/<DAG_ID>/dag_runs

  Creates a dag_run for a given DAG id.
  Note: If execution_date is not specified in the body, Airflow by default creates only one DAG per second for a given DAG_ID.
  In order to create multiple DagRun within one second, you should set parameter ``"replace_microseconds"`` to ``"false"`` (boolean as string).

  The execution_date must be specified with the format ``YYYY-mm-DDTHH:MM:SS.ssssss``.

  **Trigger DAG with config, example:**

  .. code-block:: bash

    curl -X POST \
        'http://localhost:8080/api/experimental/dags/<DAG_ID>/dag_runs' \
        --header 'Cache-Control: no-cache' \
        --header 'Content-Type: application/json' \
        --data '{"conf":"{\"key\":\"value\"}"}'

  **Trigger DAG with milliseconds precision, example:**

  .. code-block:: bash

    curl -X POST  \
        'http://localhost:8080/api/experimental/dags/<DAG_ID>/dag_runs' \
        --header 'Content-Type: application/json' \
        --header 'Cache-Control: no-cache' \
        --data '{"replace_microseconds":"false"}'

.. http:get:: /api/experimental/dags/<DAG_ID>/dag_runs

  Returns a list of Dag Runs for a specific DAG ID.


.. http:get:: /api/experimental/dags/<string:dag_id>/dag_runs/<string:execution_date>

  Returns a JSON with a dag_run's public instance variables. The format for the ``<string:execution_date>`` is expected to be ``YYYY-mm-DDTHH:MM:SS``, for example: ``"2016-11-16T11:34:15"``.


.. http:get:: /api/experimental/test

  To check REST API server correct work. Return status 'OK'.


.. http:get:: /api/experimental/dags/<DAG_ID>/tasks/<TASK_ID>

  Returns info for a task.


.. http:get:: /api/experimental/dags/<DAG_ID>/dag_runs/<string:execution_date>/tasks/<TASK_ID>

  Returns a JSON with a task instance's public instance variables. The format for the ``<string:execution_date>`` is expected to be ``YYYY-mm-DDTHH:MM:SS``, for example: ``"2016-11-16T11:34:15"``.


.. http:get:: /api/experimental/dags/<DAG_ID>/paused/<string:paused>

  '<string:paused>' must be a 'true' to pause a DAG and 'false' to unpause.


.. http:get:: /api/experimental/dags/<DAG_ID>/paused

  Returns the paused state of a DAG


.. http:get:: /api/experimental/latest_runs

  Returns the latest DagRun for each DAG formatted for the UI.


.. http:get:: /api/experimental/pools

  Get all pools.


.. http:get:: /api/experimental/pools/<string:name>

  Get pool by a given name.


.. http:post:: /api/experimental/pools

  Create a pool.


.. http:delete:: /api/experimental/pools/<string:name>

  Delete pool.

.. http:get:: /api/experimental/lineage/<DAG_ID>/<string:execution_date>/

  Returns the lineage information for the DAG.
