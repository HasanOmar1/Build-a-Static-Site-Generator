
class HTMLNode():
    def __init__(self, tag: str = None, value: str = None, children: list[HTMLNode] = None, props: dict[str, str] = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):
        raise NotImplementedError()
    

    def props_to_html(self) -> str:
        res = ""
        
        if self.props is not None:
            for key,value in self.props.items():
                res += f' {key}="{value}"'
        
        return res
        
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
    
    
    
class LeafNode(HTMLNode):
    def __init__(self, tag , value , props = None):
        super().__init__(tag, value, None, props)
        
    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        
        if self.tag is None:
            return self.value
        
        if self.props is not None:
            return f"<{self.tag} {super().props_to_html}>{self.value}</{self.tag}>"
        
        return f"<{self.tag}>{self.value}</{self.tag}>"
    
    
    def __repr__(self):
         return f"LeafNode({self.tag}, {self.value}, {self.props})"