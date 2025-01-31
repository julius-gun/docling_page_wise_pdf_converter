# docling-page-wise-pdf-converter/format_converters/base_converter.py
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Dict

class BaseConverter(ABC):
    """
    Abstract base class for format converters.
    """
    @abstractmethod
    def convert_to_format(self, doc, pdf_path: Path, output_dir: Path) -> Dict[int, str]:
        """
        Converts the document to a specific format and returns page contents.

        Args:
            doc: The document object from docling.
            pdf_path: Path to the input PDF file.
            output_dir: Directory for output files.

        Returns:
            A dictionary where keys are page numbers and values are page contents in the target format.
        """
        pass

    def save_with_original_extension(self, page_contents: Dict[int, str], pdf_path: Path, output_dir: Path, doc): # Added 'doc' here
        """
        Saves the converted content to files with the original format extension (e.g., .html, .md).
        This is an optional method and can be overridden by subclasses if needed.
        """
        pass # Optional method to save with original extension