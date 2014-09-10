import requests


class DataSet(object):

    base_url = 'http://www.bea.gov/api/data?'

    def __init__(self, api_key, data_set_name, result_format='json'):
        # data_set_name is read-only
        self._data_set_name = data_set_name

        self.api_key = api_key
        self.result_format = result_format

    @property
    def data_set_name(self):
        return self._data_set_name

    @property
    def parameter_list(self):
        tmp_query = {'UserID': self.api_key,
                     'Method': 'GetParameterList',
                     'DataSetName': self.data_set_name,
                     'ResultFormat': self.result_format}
        tmp_response = requests.get(url=self.base_url, params=tmp_query)
        return tmp_response

    def grab_data(self, **kwargs):
        base_query = {'UserID': self.api_key,
                      'Method': 'GetData',
                      'DataSetName': self.data_set_name,
                      'ResultFormat': self.result_format}
        tmp_query = base_query.update(kwargs)
        tmp_response = requests.get(url=self.base_url, params=tmp_query)
        return tmp_response

    def grab_parameter_values(self, parameter):
        tmp_query = {'UserID': self.api_key,
                     'Method': 'GetParameterValues',
                     'DataSetName': self.data_set_name,
                     'ParameterName': parameter,
                     'ResultFormat': self.result_format}
        tmp_response = requests.get(url=self.base_url, params=tmp_query)
        return tmp_response


class MetaData(object):

    base_url = 'http://www.bea.gov/api/data?'

    def __init__(self, api_key, result_format='json'):
        self.api_key = api_key
        self.result_format = result_format

    @property
    def data_set_list(self):
        tmp_query = {'UserID': self.api_key,
                     'Method': 'GetDataSetList',
                     'ResultFormat': self.result_format}
        tmp_response = requests.get(url=self.base_url, params=tmp_query)
        return tmp_response


class RegionalData(DataSet):

    def __init__(self, api_key, result_format='json'):
        super(RegionalData, self).__init__(api_key, 'RegionalData', result_format)


class NIPA(DataSet):

    def __init__(self, api_key, result_format='json'):
        super(RegionalData, self).__init__(api_key, 'NIPA', result_format)


class NIUnderlyingDetail(DataSet):

    def __init__(self, api_key, result_format='json'):
        super(RegionalData, self).__init__(api_key, 'NIUnderlyingDetail', result_format)


class FixedAssets(DataSet):

    def __init__(self, api_key, result_format='json'):
        super(RegionalData, self).__init__(api_key, 'FixedAssets', result_format)
