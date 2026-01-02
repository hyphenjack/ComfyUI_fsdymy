# Fix Node Recognition Issue in ComfyUI 0.6.0

The investigation revealed that the `fsdymy` extension fails to load entirely because of a missing `zhipuai` dependency. When ComfyUI attempts to import the extension, the `ModuleNotFoundError` in [GLM.py](file:///c:/Users/USER/Documents/ComfyUI/custom_nodes/comfyui_fsdymy/nodes/GLM.py) propagates up, causing ComfyUI to skip the extension.

## User Review Required

> [!IMPORTANT]
> You need to install the `zhipuai` package in your ComfyUI Python environment.
> If you are using the portable version of ComfyUI, run:
> ```bash
> ..\..\..\python_embedded\python.exe -m pip install zhipuai
> ```
> Or if you have a system-wide Python that ComfyUI uses:
> ```bash
> pip install zhipuai
> ```

## Proposed Changes

### [Component Name] Core Extension Loading

#### [MODIFY] [__init__.py](file:///c:/Users/USER/Documents/ComfyUI/custom_nodes/comfyui_fsdymy/__init__.py)

Refactor [__init__.py](file:///c:/Users/USER/Documents/ComfyUI/custom_nodes/comfyui_fsdymy/__init__.py) to use try-except blocks for each module import. This ensures that:
1. If the `zhipuai` nodes fail to load, other nodes (like Image Utils and IPAdapter weights) still show up.
2. ComfyUI produces a clear warning message in the console rather than silently skipping the extension.

```python
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
    print(f"[fsdymy] Error loading GLM nodes: {e}. Please install requirements.")

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
```

## Verification Plan

### Automated Tests
- Run `python -c "import zhipuai"` to verify installation.
- Check ComfyUI console output to ensure no extension loading errors.

### Manual Verification
- Restart ComfyUI and check if "fsdymy" category appears in the node menu.
