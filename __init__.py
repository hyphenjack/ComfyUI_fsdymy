NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}

# Load GLM nodes
try:
    from .nodes.GLM import ZhiPuAiNode, ShowText
    NODE_CLASS_MAPPINGS["ZhiPuAiNode"] = ZhiPuAiNode
    NODE_CLASS_MAPPINGS["ShowText"] = ShowText
    NODE_DISPLAY_NAME_MAPPINGS["ZhiPuAiNode"] = "ZhiPu Ai Node (fsdymy)"
    NODE_DISPLAY_NAME_MAPPINGS["ShowText"] = "Show Text (fsdymy)"
except ImportError as e:
    print(f"[fsdymy] Error loading GLM nodes: {e}. Please install zhipuai.")

# Load IPAdapter nodes
try:
    from .nodes.IPAdapterLayerWeight import IPAdapterLayerWeight
    NODE_CLASS_MAPPINGS["IPAdapterLayerWeight"] = IPAdapterLayerWeight
    NODE_DISPLAY_NAME_MAPPINGS["IPAdapterLayerWeight"] = "IPAdapter Layer Weight (fsdymy)"
except ImportError as e:
    print(f"[fsdymy] Error loading IPAdapter nodes: {e}")

# Load Image Utils
try:
    from .nodes.imageUtils import SaveImageWithoutMetadata, PreviewImageWithoutMetadata
    NODE_CLASS_MAPPINGS["SaveImageWithoutMetadata"] = SaveImageWithoutMetadata
    NODE_CLASS_MAPPINGS["PreviewImageWithoutMetadata"] = PreviewImageWithoutMetadata
    NODE_DISPLAY_NAME_MAPPINGS["SaveImageWithoutMetadata"] = "Save Image Without Metadata (fsdymy)"
    NODE_DISPLAY_NAME_MAPPINGS["PreviewImageWithoutMetadata"] = "Preview Image Without Metadata (fsdymy)"
except ImportError as e:
    print(f"[fsdymy] Error loading Image Utils: {e}")

WEB_DIRECTORY = "./web"
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
