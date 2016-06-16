# -*- coding: utf-8 -*-
from openprocurement.api.models import get_now
from openprocurement.api.utils import (
    opresource
)
from openprocurement.tender.openeu.views.bid_document import TenderEUBidDocumentResource
from openprocurement.tender.openeu.utils import (
    bid_financial_documents_resource, bid_eligibility_documents_resource,
    bid_qualification_documents_resource,
)


@opresource(
    name='Competitive Dialogue EU Bid Documents',
    collection_path='/tenders/{tender_id}/bids/{bid_id}/documents',
    path='/tenders/{tender_id}/bids/{bid_id}/documents/{document_id}',
    procurementMethodType='competitiveDialogue.aboveThresholdEU',
    description="Competitive Dialogue EU bidder documents")
class CompetitiveDialogueEUBidDocumentResource(TenderEUBidDocumentResource):
    pass


@opresource(
    name='Competitive Dialogue UA Bid Documents',
    collection_path='/tenders/{tender_id}/bids/{bid_id}/documents',
    path='/tenders/{tender_id}/bids/{bid_id}/documents/{document_id}',
    procurementMethodType='competitiveDialogue.aboveThresholdUA',
    description="Competitive Dialogue UA bidder documents")
class CompetitiveDialogueUaBidDocumentResource(TenderEUBidDocumentResource):
    pass