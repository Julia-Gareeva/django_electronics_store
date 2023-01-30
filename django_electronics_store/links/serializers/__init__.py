from .dealerships import DealershipsSerializer, DealershipsCreateSerializer, DealershipsDeleteSerializer
from .distributors import DistributorsSerializer, DistributorsCreateSerializer, DistributorsDeleteSerializer
from .factories import FactoriesSerializer, FactoriesCreateSerializer, FactoriesDeleteSerializer, ProductsSerializer, \
    ProductsCreateSerializer, ProductsDeleteSerializer

from .individual_entrepreneurs import IndividualEntrepreneursSerializer, IndividualEntrepreneursCreateSerializer, \
    IndividualEntrepreneursDeleteSerializer

from .retail_chains import RetailChainsSerializer, RetailChainsCreateSerializer, RetailChainsDeleteSerializer

from .supplier import SupplierSerializer

__all__ = [
    "FactoriesSerializer",
    "FactoriesCreateSerializer",
    "FactoriesDeleteSerializer",
    "ProductsSerializer",
    "ProductsCreateSerializer",
    "ProductsDeleteSerializer",
    "DistributorsSerializer",
    "DistributorsCreateSerializer",
    "DistributorsDeleteSerializer",
    "DealershipsSerializer",
    "DealershipsCreateSerializer",
    "DealershipsDeleteSerializer",
    "RetailChainsSerializer",
    "RetailChainsCreateSerializer",
    "RetailChainsDeleteSerializer",
    "IndividualEntrepreneursSerializer",
    "IndividualEntrepreneursCreateSerializer",
    "IndividualEntrepreneursDeleteSerializer",
    "SupplierSerializer",
]
