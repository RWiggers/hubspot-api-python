import hubspot
from hubspot.crm.contacts import BasicApi, AssociationsApi, BatchApi, SearchApi


def test_is_discoverable():
    apis = hubspot.Client.create().crm.contacts
    assert isinstance(apis.basic_api, BasicApi)
    assert isinstance(apis.associations_api, AssociationsApi)
    assert isinstance(apis.batch_api, BatchApi)
    assert isinstance(apis.search_api, SearchApi)
