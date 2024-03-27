from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.blank_enum import BlankEnum
from ..models.detail_type_enum import DetailTypeEnum
from ..models.price_unit_type_enum import PriceUnitTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PricingSerialzier")


@_attrs_define
class PricingSerialzier:
    """
    Attributes:
        get_detail_type_display (str):
        model_name (Union[Unset, str]): Model name, default to 'default' if no models to chose from
        price (Union[Unset, str]):
        price_unit_quantity (Union[Unset, int]):
        min_price_quantity (Union[None, Unset, int]):
        price_unit_type (Union[Unset, PriceUnitTypeEnum]): * `file` - File
            * `image` - Image
            * `page` - Page
            * `size` - Size
            * `request` - Request
            * `seconde` - Second
            * `minute` - Minute
            * `free` - Free
            * `hour` - Hour
            * `char` - Characters
            * `token` - Token
            * `exec_time` - Execution Time
            * `unknown` - Unknown
        detail_type (Union[BlankEnum, DetailTypeEnum, None, Unset]): (Optional) type of extra value, MUST be the same
            name as the feature parameter name. eg: resolution

            * `resolution` - Resolution
            * `document_type` - Document Type
        detail_value (Union[None, Unset, str]): (Optional) extra value for detailed pricing, eg: 250x250 for resolution
        is_post_call (Union[Unset, bool]):
    """

    get_detail_type_display: str
    model_name: Union[Unset, str] = UNSET
    price: Union[Unset, str] = UNSET
    price_unit_quantity: Union[Unset, int] = UNSET
    min_price_quantity: Union[None, Unset, int] = UNSET
    price_unit_type: Union[Unset, PriceUnitTypeEnum] = UNSET
    detail_type: Union[BlankEnum, DetailTypeEnum, None, Unset] = UNSET
    detail_value: Union[None, Unset, str] = UNSET
    is_post_call: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        get_detail_type_display = self.get_detail_type_display

        model_name = self.model_name

        price = self.price

        price_unit_quantity = self.price_unit_quantity

        min_price_quantity: Union[None, Unset, int]
        if isinstance(self.min_price_quantity, Unset):
            min_price_quantity = UNSET
        else:
            min_price_quantity = self.min_price_quantity

        price_unit_type: Union[Unset, str] = UNSET
        if not isinstance(self.price_unit_type, Unset):
            price_unit_type = self.price_unit_type.value

        detail_type: Union[None, Unset, str]
        if isinstance(self.detail_type, Unset):
            detail_type = UNSET
        elif isinstance(self.detail_type, DetailTypeEnum):
            detail_type = self.detail_type.value
        elif isinstance(self.detail_type, BlankEnum):
            detail_type = self.detail_type.value
        else:
            detail_type = self.detail_type

        detail_value: Union[None, Unset, str]
        if isinstance(self.detail_value, Unset):
            detail_value = UNSET
        else:
            detail_value = self.detail_value

        is_post_call = self.is_post_call

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "get_detail_type_display": get_detail_type_display,
            }
        )
        if model_name is not UNSET:
            field_dict["model_name"] = model_name
        if price is not UNSET:
            field_dict["price"] = price
        if price_unit_quantity is not UNSET:
            field_dict["price_unit_quantity"] = price_unit_quantity
        if min_price_quantity is not UNSET:
            field_dict["min_price_quantity"] = min_price_quantity
        if price_unit_type is not UNSET:
            field_dict["price_unit_type"] = price_unit_type
        if detail_type is not UNSET:
            field_dict["detail_type"] = detail_type
        if detail_value is not UNSET:
            field_dict["detail_value"] = detail_value
        if is_post_call is not UNSET:
            field_dict["is_post_call"] = is_post_call

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        get_detail_type_display = d.pop("get_detail_type_display")

        model_name = d.pop("model_name", UNSET)

        price = d.pop("price", UNSET)

        price_unit_quantity = d.pop("price_unit_quantity", UNSET)

        def _parse_min_price_quantity(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        min_price_quantity = _parse_min_price_quantity(d.pop("min_price_quantity", UNSET))

        _price_unit_type = d.pop("price_unit_type", UNSET)
        price_unit_type: Union[Unset, PriceUnitTypeEnum]
        if isinstance(_price_unit_type, Unset):
            price_unit_type = UNSET
        else:
            price_unit_type = PriceUnitTypeEnum(_price_unit_type)

        def _parse_detail_type(data: object) -> Union[BlankEnum, DetailTypeEnum, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                detail_type_type_0 = DetailTypeEnum(data)

                return detail_type_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                detail_type_type_1 = BlankEnum(data)

                return detail_type_type_1
            except:  # noqa: E722
                pass
            return cast(Union[BlankEnum, DetailTypeEnum, None, Unset], data)

        detail_type = _parse_detail_type(d.pop("detail_type", UNSET))

        def _parse_detail_value(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        detail_value = _parse_detail_value(d.pop("detail_value", UNSET))

        is_post_call = d.pop("is_post_call", UNSET)

        pricing_serialzier = cls(
            get_detail_type_display=get_detail_type_display,
            model_name=model_name,
            price=price,
            price_unit_quantity=price_unit_quantity,
            min_price_quantity=min_price_quantity,
            price_unit_type=price_unit_type,
            detail_type=detail_type,
            detail_value=detail_value,
            is_post_call=is_post_call,
        )

        pricing_serialzier.additional_properties = d
        return pricing_serialzier

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
