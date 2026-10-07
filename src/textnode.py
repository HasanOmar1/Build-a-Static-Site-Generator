from enum import Enum

class TextType(Enum):
    TEXT = "Plain"
    BOLD = "Bold"
    ITALIC = "Italic"
    CODE = "Code"
    LINK = "Link"
    IMG = "Image"
    
    
    
    
class TextNode:
    
    def __init__(self,text:str, text_type:TextType , url:str | None = None):
        self.text = text
        self.text_type = text_type
        self.url  = url
        
    def __eq__(self, other: TextNode):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    
    def __repr__(self):
        if self.url is not None:
            return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
        
        return f"TextNode({self.text}, {self.text_type.value})"