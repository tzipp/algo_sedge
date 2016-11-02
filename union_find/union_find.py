class UnionFind:
    def __init__(self, n):
        self.ids = [i for i in range(0, n)]

    def connected(self, p, q):
        """To be implemented by subclasses."""
        return None

    def union(self, p, q):
        """To be implemented by subclasses."""
        return None


class QuickFind(UnionFind):
    def __init__(self, n):
        super().__init__(n)

    def connected(self, p, q):
        return self.ids[p] == self.ids[q]

    def union(self, p, q):
        q_id = self.ids[q]
        p_id = self.ids[p]
        for i, _id in enumerate(self.ids):
            if _id == p_id:
                self.ids[i] = q_id


def main():
    qf = QuickFind(5)
    print(qf.ids)

    qf.union(0, 1)
    qf.union(3, 4)

    print(qf.ids)


if __name__ == '__main__':
    main()
