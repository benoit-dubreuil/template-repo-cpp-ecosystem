class GenericClassMixin:
    from typing import Final

    generics: Final[tuple[type]]

    def __init__(self, *args, generics: tuple[type] = None, **kwargs):
        self.generics = generics if generics is not None else tuple()
        super().__init__(*args, **kwargs)

    def has_generics(self) -> bool:
        return len(self.generics) > 0