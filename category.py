class CategoryTree:

    def __init__(self):
        self.category={}

    def add_category(self, category, parent):
        if category in self.category:
            raise KeyError('exist')
        if parent is not None and parent not in self.category:
            raise KeyError('exist')     
        else:
            self.category[category]=parent

    def get_children(self, parent):
        if len(self.category)==0:
            return []
        ans=[]
        for category, p in self.category.items():
            if p==parent:
                ans.append(category)
        return ans

if __name__ == "__main__":
    c = CategoryTree()
    c.add_category('A', None)
    c.add_category('B', 'A')
    c.add_category('C', 'A')
    print(','.join(c.get_children('A') or []))