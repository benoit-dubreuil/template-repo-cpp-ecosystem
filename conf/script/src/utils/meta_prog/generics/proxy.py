import itertools

from utils.meta_prog.generics.data import GenericsData
from utils.meta_prog.generics.mixin import GenericClassMixin


class GenericClassProxy(GenericsData):
    from typing import TypeVar, Generic, Final

    _TAlias_generic_cls = type[GenericClassMixin, Generic]

    wrapped_generic_cls: Final[_TAlias_generic_cls]

    def __init__(self,
                 generic_cls: _TAlias_generic_cls,
                 *args,
                 generics: tuple[type] = tuple(),
                 **kwargs) -> None:
        self.wrapped_generic_cls = generic_cls
        generics_by_type_vars = self.__create_generics_by_type_vars(generic_cls=generic_cls, generics=generics)

        super().__init__(*args, generics_by_type_vars=generics_by_type_vars, **kwargs)

    def __call__(self, *args, **kwargs):
        return self.wrapped_generic_cls(*args, generics_by_type_vars=self.generics_by_type_vars, **kwargs)

    @property
    def __class__(self) -> _TAlias_generic_cls:
        return self.wrapped_generic_cls

    @classmethod
    def __create_generics_by_type_vars(cls, generic_cls: _TAlias_generic_cls, generics: tuple[type]) -> GenericsData.TAlias_Generics_By_TypeVars:
        type_vars = cls.__detect_type_vars(generic_cls=generic_cls)
        generics_by_type_vars = dict(itertools.zip_longest(type_vars, generics, fillvalue=None))

        return generics_by_type_vars

    @classmethod
    def __detect_type_vars(cls, generic_cls: _TAlias_generic_cls) -> tuple[TypeVar]:
        from typing import TypeVar, Generic, get_args, get_origin

        type_vars: list[TypeVar] = []

        for orig_base in generic_cls.__orig_bases__:
            if get_origin(orig_base) is Generic:
                base_type_args = get_args(orig_base)

                if len(base_type_args) > 0:
                    for type_arg in base_type_args:
                        if isinstance(type_arg, TypeVar):
                            type_vars.append(type_arg)
                else:
                    type_vars += cls.__detect_type_vars(generic_cls=orig_base)

        return tuple(type_vars)
