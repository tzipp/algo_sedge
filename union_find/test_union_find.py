import pytest

from union_find import UnionFind, QuickFind


class TestBaseUF:
    def setup(self):
        self.uf = UnionFind(10)

    def test_initialized_uf(self):
        for i in range(0, 10):
            assert self.uf.ids[i] == i

    def test_union(self):
        assert self.uf.union(1, 2) is None

    def test_connected(self):
        assert self.uf.connected(1, 2) is None


class TestQuickFind:
    def setup(self):
        self.qf = QuickFind(10)

    def test_none_connected(self):
        for i in range(0, 10):
            assert self.qf.ids[i] == i

    def test_0_1_joined(self):
        self.qf.union(0, 1)

        # Test connectedness by direct inspection.
        assert self.qf.ids[0] == 1
        assert self.qf.ids[1] == 1
        for i in range(2, 10):
            assert self.qf.ids[i] != 0 and self.qf.ids[i] != 1

        # Test connectedness by the QF API
        assert self.qf.connected(0,1)

    def test_0_1_then_7_9_union(self):
        self.qf.union(0, 1)
        self.qf.union(7, 9)
        joined = {0, 1, 7, 9}

        # Test connectedness by directly comparing data.
        assert self.qf.ids[0] == 1
        assert self.qf.ids[1] == 1
        assert self.qf.ids[7] == 9
        assert self.qf.ids[9] == 9
        for i in range(0, 10):
            if i not in joined:
                assert self.qf.ids[i] not in joined

        # Test using connected function
        assert self.qf.connected(0, 1)
        assert self.qf.connected(7, 9)

    def test_0_1_then_7_9_then_0_9_union(self):
        pass

