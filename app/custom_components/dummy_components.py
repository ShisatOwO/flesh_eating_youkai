from fey import FeyBaseComponent


class DummyComponentA(FeyBaseComponent):
    def __init__(self, pname: str, *args, **kwargs):
        self._name = pname
        super().__init__(*args, **kwargs)


class DummyComponentB(FeyBaseComponent):
    def __init__(self, pname: str, *args, **kwargs):
        self._name = pname
        super().__init__(*args, **kwargs)


class DummyComponentC(FeyBaseComponent):
    def __init__(self, pname: str, *args, **kwargs):
        self._name = pname
        super().__init__(*args, **kwargs)


"""FeyGlobalComponentTable([
    DummyComponentA(pname="Component: A\tDepth: 0", name="root1", comps=[
        DummyComponentB(pname="Component: B\tDepth: 1", name="c1"),
        DummyComponentB(pname="Component: B\tDepth: 1", name="c2"),
    ]),
    DummyComponentA(pname="Component: A\tDepth: 0", name="root2", comps=[
        DummyComponentC(pname="Component: C\tDepth: 1", name="c1", comps=[
            DummyComponentB(pname="Component: B\tDepth: 2", name="c2")
        ]),
    ]),
])
print(FeyGlobalComponentTable().qget("root2").qsearch("c2").name)"""
