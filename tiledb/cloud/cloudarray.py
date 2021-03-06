from . import array

last_udf_task_id = None


class CloudArray(object):
    def apply_async(
        self,
        func=None,
        ranges=None,
        name=None,
        attrs=None,
        layout=None,
        image_name=None,
        http_compressor="deflate",
        task_name=None,
    ):
        """
        Apply a user defined function to an array asynchronous

        :param func: user function to run
        :param ranges: ranges to issue query on
        :param attrs: list of attributes or dimensions to fetch in query
        :param layout: tiledb query layout
        :param image_name: udf image name to use, useful for testing beta features
        :param http_compressor: set http compressor for results
        :param str task_name: optional name to assign the task for logging and audit purposes
        :return: UDFResult object which is a future containing the results of the UDF

        **Example**
        >>> import tiledb, tiledb.cloud, numpy
        >>> def median(df):
        ...   return numpy.median(df["a"])
        >>> # Open the array then run the UDF
        >>> with tiledb.SparseArray("tiledb://TileDB-Inc/quickstart_dense", ctx=tiledb.cloud.ctx()) as A:
        ...   A.apply(median, [(0,5), (0,5)], attrs=["a", "b", "c"])
        2.0

        """
        return array.apply_async(
            uri=self.uri,
            func=func,
            ranges=ranges,
            name=name,
            attrs=attrs,
            layout=layout,
            image_name=image_name,
            http_compressor=http_compressor,
            task_name=task_name,
        )

    def apply(
        self,
        func=None,
        ranges=None,
        name=None,
        attrs=None,
        layout=None,
        image_name=None,
        http_compressor="deflate",
        task_name=None,
    ):
        """
        Apply a user defined function to an array
        :param func: user function to run
        :param ranges: ranges to issue query on
        :param attrs: list of attributes or dimensions to fetch in query
        :param layout: tiledb query layout
        :param image_name: udf image name to use, useful for testing beta features
        :param http_compressor: set http compressor for results
        :param str task_name: optional name to assign the task for logging and audit purposes
        :return: results of the UDF
        """
        return self.apply_async(
            func=func,
            ranges=ranges,
            name=name,
            attrs=attrs,
            layout=layout,
            image_name=image_name,
            http_compressor=http_compressor,
            task_name=task_name,
        ).get()
