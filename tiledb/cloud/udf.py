from . import rest_api
from . import array
from . import client
from .rest_api import ApiException as GenApiException
from . import tiledb_cloud_error
from . import config

import cloudpickle

tiledb_cloud_protocol = 4

import base64
import sys

last_udf_task_id = None


def exec_async(
    func, arguments=None, namespace=None, image_name=None, http_compressor="deflate",
):
    """
     Run a user defined function


    :param func: user function to run
    :param arguments: arguments to pass to function
    :param namespace: namespace to run udf under
    :param image_name: udf image name to use, useful for testing beta features
    :param http_compressor: set http compressor for results
    :return: UDFResult object which is a future containing the results of the UDF
    """

    api_instance = client.client.udf_api

    # If the namespace is not set, we will default to the user's namespace
    if namespace is None:
        # Fetch the client profile for username if it is not already cached
        if config.user is None:
            config.user = client.user_profile()

        namespace = config.user.username

    if not callable(func):
        raise TypeError("First argument to `exec` must be callable!")

    pickledUDF = cloudpickle.dumps(func, protocol=tiledb_cloud_protocol)
    pickledUDF = base64.b64encode(pickledUDF).decode("ascii")

    if arguments != None:
        arguments = cloudpickle.dumps(arguments, protocol=tiledb_cloud_protocol)
        arguments = base64.b64encode(arguments).decode("ascii")

    if image_name is None:
        image_name = "default"
    try:

        kwargs = {"_preload_content": False, "async_req": True}
        if http_compressor is not None:
            kwargs["accept_encoding"] = http_compressor

        # _preload_content must be set to false to avoid trying to decode binary data
        response = api_instance.submit_generic_udf(
            namespace=namespace,
            udf=rest_api.models.GenericUDF(
                language=rest_api.models.UDFLanguage.PYTHON,
                _exec=pickledUDF,
                argument=arguments,
                result_format=rest_api.models.UDFResultType.NATIVE,
                version="{}.{}.{}".format(
                    sys.version_info.major,
                    sys.version_info.minor,
                    sys.version_info.micro,
                ),
                image_name=image_name,
            ),
            **kwargs
        )

        return array.UDFResult(response)

    except GenApiException as exc:
        raise tiledb_cloud_error.check_sql_exc(exc) from None


def exec(
    func, arguments=None, namespace=None, image_name=None, http_compressor="deflate",
):
    """
     Run a user defined function


    :param func: user function to run
    :param arguments: arguments to pass to function
    :param namespace: namespace to run udf under
    :param image_name: udf image name to use, useful for testing beta features
    :param http_compressor: set http compressor for results
    :return: UDFResult object which is a future containing the results of the UDF
    """
    return exec_async(
        func=func,
        arguments=arguments,
        namespace=namespace,
        image_name=image_name,
        http_compressor=http_compressor,
    ).get()


def register_udf(func, name, namespace=None, image_name=None, type=None):
    """

  :param func: function to register
  :param name: name of udf to register
  :param namespace: namespace to register in
  :param image_name: optional image name
  :param type: type of udf, generic or single_array
  :return:
  """

    try:
        api_instance = client.client.udf_api

        # If the namespace is not set, we will default to the user's namespace
        if namespace is None:
            # Fetch the client profile for username if it is not already cached
            if config.user is None:
                config.user = client.user_profile()

            namespace = config.user.username

        if not callable(func):
            raise TypeError("First argument to `exec` must be callable!")

        pickledUDF = cloudpickle.dumps(func, protocol=tiledb_cloud_protocol)
        pickledUDF = base64.b64encode(pickledUDF).decode("ascii")

        udf = rest_api.models.UDFRegistration(
            name=name,
            language=rest_api.models.UDFLanguage.PYTHON,
            version="{}.{}.{}".format(
                sys.version_info.major, sys.version_info.minor, sys.version_info.micro,
            ),
            image_name=image_name,
            type=type,
            _exec=pickledUDF,
            exec_raw=None,
        )

        api_instance.register_udf(namespace=namespace, name=name, udf=udf)

    except GenApiException as exc:
        raise tiledb_cloud_error.check_exc(exc) from None


def register_generic_udf(func, name, namespace=None, image_name=None):
    """

  :param func: function to register
  :param name: name of udf to register
  :param namespace: namespace to register in
  :param image_name: optional image name
  :return:
  """
    return register_udf(
        func=func,
        name=name,
        namespace=namespace,
        image_name=image_name,
        type=rest_api.models.UDFType.GENERIC,
    )


def register_single_array_udf(func, name, namespace=None, image_name=None):
    """

  :param func: function to register
  :param name: name of udf to register
  :param namespace: namespace to register in
  :param image_name: optional image name
  :return:
  """
    return register_udf(
        func=func,
        name=name,
        namespace=namespace,
        image_name=image_name,
        type=rest_api.models.UDFType.SINGLE_ARRAY,
    )


def update_udf(func, name, namespace=None, image_name=None, type=None):
    """

  :param func: function to register
  :param name: name of udf to register
  :param namespace: namespace to register in
  :param image_name: optional image name
  :param type: type of udf, generic or single_array
  :return:
  """

    try:
        api_instance = client.client.udf_api

        # If the namespace is not set, we will default to the user's namespace
        if namespace is None:
            # Fetch the client profile for username if it is not already cached
            if config.user is None:
                config.user = client.user_profile()

            namespace = config.user.username

        if not callable(func):
            raise TypeError("First argument to `exec` must be callable!")

        pickledUDF = cloudpickle.dumps(func, protocol=tiledb_cloud_protocol)
        pickledUDF = base64.b64encode(pickledUDF).decode("ascii")

        udf = rest_api.models.UDFRegistration(
            name=name,
            language=rest_api.models.UDFLanguage.PYTHON,
            version="{}.{}.{}".format(
                sys.version_info.major, sys.version_info.minor, sys.version_info.micro,
            ),
            image_name=image_name,
            type=type,
            _exec=pickledUDF,
            exec_raw=None,
        )

        api_instance.updated_registered_udf(namespace=namespace, name=name, udf=udf)

    except GenApiException as exc:
        raise tiledb_cloud_error.check_exc(exc) from None


def update_generic_udf(func, name, namespace=None, image_name=None):
    """

  :param func: function to register
  :param name: name of udf to register
  :param namespace: namespace to register in
  :param image_name: optional image name
  :return:
  """
    return update_udf(
        func=func,
        name=name,
        namespace=namespace,
        image_name=image_name,
        type=rest_api.models.UDFType.GENERIC,
    )


def update_single_array_udf(func, name, namespace=None, image_name=None):
    """

  :param func: function to register
  :param name: name of udf to register
  :param namespace: namespace to register in
  :param image_name: optional image name
  :return:
  """
    return update_udf(
        func=func,
        name=name,
        namespace=namespace,
        image_name=image_name,
        type=rest_api.models.UDFType.SINGLE_ARRAY,
    )


def info(name=None):
    """
  Fetch info on a registered udf
  :param name: name of udf in "namespace/name" format
  :return: registered udf details
  """
    try:
        api_instance = client.client.udf_api
        (namespace, udf_name) = name.split("/")

        if not (
            namespace is not None
            and udf_name is not None
            and namespace != ""
            and udf_name != ""
        ):
            # If the namespace is not set, we will default to the user's namespace
            # Fetch the client profile for username if it is not already cached
            if config.user is None:
                config.user = client.user_profile()

            namespace = config.user.username

        return api_instance.get_udf(namespace=namespace, name=name)
    except GenApiException as exc:
        raise tiledb_cloud_error.check_exc(exc) from None


def list_registered_udfs(namespace=None, search=None):
    """
  Fetch all registered udf user has access to
  :param namespace: namespace to filter to
  :param search: string search for udfs
  :return: registered udf details
  """
    try:
        api_instance = client.client.udf_api

        return api_instance.get_ud_fs(namespace=namespace, search=search)
    except GenApiException as exc:
        raise tiledb_cloud_error.check_exc(exc) from None
