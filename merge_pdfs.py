#!/usr/bin/env python3
"""
Merge all PDF files from QP folder into a single combined PDF
Run this script from the repository root directory
"""

from pypdf import PdfMerger
from pathlib import Path
import sys

# Define all PDF files in order (by session and paper)
pdf_files = [
    # Summer 2021
    "QP/S21/9708_s21_qp_12.pdf", "QP/S21/9708_s21_qp_13.pdf",
    "QP/S21/9708_s21_qp_21.pdf", "QP/S21/9708_s21_qp_22.pdf", "QP/S21/9708_s21_qp_23.pdf",
    "QP/S21/9708_s21_qp_31.pdf", "QP/S21/9708_s21_qp_32.pdf", "QP/S21/9708_s21_qp_33.pdf",
    "QP/S21/9708_s21_qp_41.pdf", "QP/S21/9708_s21_qp_42.pdf", "QP/S21/9708_s21_qp_43.pdf",
    # Summer 2022
    "QP/S22/9708_s22_qp_11.pdf", "QP/S22/9708_s22_qp_12.pdf", "QP/S22/9708_s22_qp_13.pdf", "QP/S22/9708_s22_qp_14.pdf",
    "QP/S22/9708_s22_qp_21.pdf", "QP/S22/9708_s22_qp_22.pdf", "QP/S22/9708_s22_qp_23.pdf",
    "QP/S22/9708_s22_qp_31.pdf", "QP/S22/9708_s22_qp_32.pdf", "QP/S22/9708_s22_qp_33.pdf",
    "QP/S22/9708_s22_qp_41.pdf", "QP/S22/9708_s22_qp_42.pdf", "QP/S22/9708_s22_qp_43.pdf",
    # Summer 2023
    "QP/S23/9708_s23_qp_11.pdf", "QP/S23/9708_s23_qp_12.pdf", "QP/S23/9708_s23_qp_13.pdf",
    "QP/S23/9708_s23_qp_21.pdf", "QP/S23/9708_s23_qp_22.pdf", "QP/S23/9708_s23_qp_23.pdf",
    "QP/S23/9708_s23_qp_31.pdf", "QP/S23/9708_s23_qp_32.pdf", "QP/S23/9708_s23_qp_33.pdf",
    "QP/S23/9708_s23_qp_41.pdf", "QP/S23/9708_s23_qp_42.pdf", "QP/S23/9708_s23_qp_43.pdf",
    # Summer 2024
    "QP/S24/9708_s24_qp_11.pdf", "QP/S24/9708_s24_qp_12.pdf", "QP/S24/9708_s24_qp_13.pdf",
    "QP/S24/9708_s24_qp_21.pdf", "QP/S24/9708_s24_qp_22.pdf", "QP/S24/9708_s24_qp_23.pdf",
    "QP/S24/9708_s24_qp_31.pdf", "QP/S24/9708_s24_qp_32.pdf", "QP/S24/9708_s24_qp_33.pdf",
    "QP/S24/9708_s24_qp_41.pdf", "QP/S24/9708_s24_qp_42.pdf", "QP/S24/9708_s24_qp_43.pdf",
    # Summer 2025
    "QP/S25/9708_s25_qp_11.pdf", "QP/S25/9708_s25_qp_12.pdf", "QP/S25/9708_s25_qp_13.pdf", "QP/S25/9708_s25_qp_14.pdf",
    "QP/S25/9708_s25_qp_21.pdf", "QP/S25/9708_s25_qp_22.pdf", "QP/S25/9708_s25_qp_23.pdf", "QP/S25/9708_s25_qp_24.pdf",
    "QP/S25/9708_s25_qp_31.pdf", "QP/S25/9708_s25_qp_32.pdf", "QP/S25/9708_s25_qp_33.pdf", "QP/S25/9708_s25_qp_34.pdf",
    "QP/S25/9708_s25_qp_41.pdf", "QP/S25/9708_s25_qp_42.pdf", "QP/S25/9708_s25_qp_43.pdf", "QP/S25/9708_s25_qp_44.pdf",
    # Winter 2021
    "QP/W21/9708_w21_qp_11.pdf", "QP/W21/9708_w21_qp_12.pdf", "QP/W21/9708_w21_qp_13.pdf",
    "QP/W21/9708_w21_qp_21.pdf", "QP/W21/9708_w21_qp_22.pdf", "QP/W21/9708_w21_qp_23.pdf",
    "QP/W21/9708_w21_qp_31.pdf", "QP/W21/9708_w21_qp_32.pdf", "QP/W21/9708_w21_qp_33.pdf",
    "QP/W21/9708_w21_qp_41.pdf", "QP/W21/9708_w21_qp_42.pdf", "QP/W21/9708_w21_qp_43.pdf",
    # Winter 2022
    "QP/W22/9708_w22_qp_11.pdf", "QP/W22/9708_w22_qp_12.pdf", "QP/W22/9708_w22_qp_13.pdf",
    "QP/W22/9708_w22_qp_21.pdf", "QP/W22/9708_w22_qp_22.pdf", "QP/W22/9708_w22_qp_23.pdf",
    "QP/W22/9708_w22_qp_31.pdf", "QP/W22/9708_w22_qp_32.pdf", "QP/W22/9708_w22_qp_33.pdf",
    "QP/W22/9708_w22_qp_41.pdf", "QP/W22/9708_w22_qp_42.pdf", "QP/W22/9708_w22_qp_43.pdf",
    # Winter 2023
    "QP/W23/9708_w23_qp_11.pdf", "QP/W23/9708_w23_qp_12.pdf", "QP/W23/9708_w23_qp_13.pdf",
    "QP/W23/9708_w23_qp_21.pdf", "QP/W23/9708_w23_qp_22.pdf", "QP/W23/9708_w23_qp_23.pdf",
    "QP/W23/9708_w23_qp_31.pdf", "QP/W23/9708_w23_qp_32.pdf", "QP/W23/9708_w23_qp_33.pdf",
    "QP/W23/9708_w23_qp_41.pdf", "QP/W23/9708_w23_qp_42.pdf", "QP/W23/9708_w23_qp_43.pdf",
    # Winter 2024
    "QP/W24/9708_w24_qp_11.pdf", "QP/W24/9708_w24_qp_12.pdf", "QP/W24/9708_w24_qp_13.pdf",
    "QP/W24/9708_w24_qp_21.pdf", "QP/W24/9708_w24_qp_22.pdf", "QP/W24/9708_w24_qp_23.pdf",
    "QP/W24/9708_w24_qp_31.pdf", "QP/W24/9708_w24_qp_32.pdf", "QP/W24/9708_w24_qp_33.pdf",
    "QP/W24/9708_w24_qp_41.pdf", "QP/W24/9708_w24_qp_42.pdf", "QP/W24/9708_w24_qp_43.pdf",
    # Winter 2025
    "QP/W25/9708_w25_qp_11.pdf", "QP/W25/9708_w25_qp_12.pdf", "QP/W25/9708_w25_qp_13.pdf",
    "QP/W25/9708_w25_qp_21.pdf", "QP/W25/9708_w25_qp_22.pdf", "QP/W25/9708_w25_qp_23.pdf", "QP/W25/9708_w25_qp_24.pdf",
    "QP/W25/9708_w25_qp_31.pdf", "QP/W25/9708_w25_qp_32.pdf", "QP/W25/9708_w25_qp_33.pdf", "QP/W25/9708_w25_qp_34.pdf",
    "QP/W25/9708_w25_qp_41.pdf", "QP/W25/9708_w25_qp_42.pdf", "QP/W25/9708_w25_qp_43.pdf", "QP/W25/9708_w25_qp_44.pdf",
]

def merge_pdfs():
    """Merge all PDFs into a single file"""
    merger = PdfMerger()
    failed = []
    
    print(f"Starting merge of {len(pdf_files)} PDF files...\n")
    
    for i, pdf_path in enumerate(pdf_files, 1):
        pdf_file = Path(pdf_path)
        
        if not pdf_file.exists():
            print(f"[{i}/{len(pdf_files)}] ✗ NOT FOUND: {pdf_path}")
            failed.append(pdf_path)
            continue
        
        try:
            merger.append(str(pdf_file))
            print(f"[{i}/{len(pdf_files)}] ✓ {pdf_file.name}")
        except Exception as e:
            print(f"[{i}/{len(pdf_files)}] ✗ ERROR: {pdf_path} - {e}")
            failed.append(pdf_path)
    
    if failed:
        print(f"\n⚠️  {len(failed)} file(s) failed to merge")
    
    output_file = "A_LEVEL_ECON_CIE_ALL_QP_MERGED.pdf"
    print(f"\nWriting merged PDF to: {output_file}")
    
    try:
        merger.write(output_file)
        merger.close()
        print(f"✓ Successfully created: {output_file}")
        return True
    except Exception as e:
        print(f"✗ Failed to write output: {e}")
        return False

if __name__ == "__main__":
    merge_pdfs()
