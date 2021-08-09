# from get_path import get_path
# path = get_path()
# print(path.get_project_root())

import  os
# import win32print, win32api
#
# def pdf_printer(pdf_name):
#     path = os.getcwd()
#     path = str(path.replace("\\", "\\\\"))
#
#     GHOSTSCRIPT_PATH = path + "\\GHOSTSCRIPT\\bin\\gswin32.exe"
#     GSPRINT_PATH = path + "\\\GSPRINT\\gsprint.exe"
#
#     # YOU CAN PUT HERE THE NAME OF YOUR SPECIFIC PRINTER INSTEAD OF DEFAULT
#     currentprinter = win32print.GetDefaultPrinter()
#
#     print_pdf = pdf_name
#
#     win32api.ShellExecute(0, 'open', GSPRINT_PATH,
#                           '-ghostscript "' + GHOSTSCRIPT_PATH + '" -printer "' + currentprinter + '" "+ print_pdf +"',
#                           '.', 0)
#
# pdf_printer("account-modification-form")


# path = os.getcwd()
# path = str(path.replace("\\", "\\\\"))
#
# GHOSTSCRIPT_PATH = path + "\\GHOSTSCRIPT\\bin\\gswin32.exe"
# GSPRINT_PATH = path + "\\\GSPRINT\\gsprint.exe"
#
# #YOU CAN PUT HERE THE NAME OF YOUR SPECIFIC PRINTER INSTEAD OF DEFAULT
# currentprinter = win32print.GetDefaultPrinter()
#
# print_pdf = "account-modification-form"
#
# win32api.ShellExecute(0, 'open', GSPRINT_PATH, '-ghostscript "'+GHOSTSCRIPT_PATH+'" -printer "'+currentprinter+'" "+ print_pdf +"', '.', 0)

##########################################################################################################################################################################

# import  os
#
# # file_path = "docs/account-modification-form.pdf"
# file_path = "docs/account-modification-form.pdf"
# os.startfile( file_path, "print")
import pathlib

#GHOSTSCRIPT_PATH = "C:\\Users\\kadam\\Documents\\Data Science\\Projects\\KB\\code\\GHOSTSCRIPT\\bin\\gswin32.exe"
# GSPRINT_PATH = "C:\\Users\\kadam\\Documents\\Data Science\\Projects\\KB\\code\\GSPRINT\\gsprint.exe"
from pathlib import Path
# import pathlib
# pth = Path(__file__).parent.parent
# p = pathlib.PureWindowsPath(__file__).parent.parent
# print(str(p.as_posix()))
# s = str(p.as_posix())
# print(s, type(s))
# print(str(pth))
import os
#path = pathlib.PureWindowsPath("C:\gswin32.exe")
# win32api.ShellExecute(0, "print","account-modification-form", None, ".", 0)
# pth.replace()
# print(str(pth), type(pth))
# import site
#
# site.addsitedir("../../../PDFNetC/Lib")
# import sys
# from PDFNetPython import *
#
#
# # The following sample illustrates how to print PDF document using currently selected
# # default printer.
# #
# # The first example uses the new PDF::Print::StartPrintJob function to send a rasterization
# # of the document with optimal compression to the printer. If the OS is Windows 7, then the
# # XPS print path will be used to preserve vector quality. For earlier Windows versions
# # the GDI print path will be used. On other operating systems this will be a no-op
# #
# # The second example uses PDFDraw send unoptimized rasterized data via awt.print API.
# #
# # If you would like to rasterize page at high resolutions (e.g. more than 600 DPI), you
# should use PDFRasterizer or PDFNet vector output instead of PDFDraw.

# def main():
#     PDFNet.Initialize()
#
#     # Relative path to the folder containing the test files.
#     input_path = "../../TestFiles/"
#
#     doc = PDFDoc(input_path + "tiger.pdf")
#     doc.InitSecurityHandler()
#
#     # Set our PrinterMode options
#     printerMode = PrinterMode()
#     printerMode.SetCollation(True)
#     printerMode.SetCopyCount(1)
#     printerMode.SetDPI(100);  # regardless of ordering, an explicit DPI setting overrides the OutputQuality setting
#     printerMode.SetDuplexing(PrinterMode.e_Duplex_Auto)

#     # If the XPS print path is being used, then the printer spooler file will
#     # ignore the grayscale option and be in full color
#     printerMode.SetOutputColor(PrinterMode.e_OutputColor_Grayscale)
#     printerMode.SetOutputQuality(PrinterMode.e_OutputQuality_Medium)
#     # printerMode.SetNUp(2,1)
#     # printerMode.SetScaleType(PrinterMode.e_ScaleType_FitToOutPage)
#
#     # Print the PDF document to the default printer, using "tiger.pdf" as the document
#     # name, send the file to the printer not to an output file, print all pages, set the printerMode
#     # and don't provide a cancel flag.
#     Print.StartPrintJob(doc, "", doc.GetFileName(), "", None, printerMode, None)
#
#
# if __name__ == '__main__':
#     main()
# import os
# #path = pathlib.PureWindowsPath("C:\gswin32.exe")
# path = os.getcwd()
# print(str(path.replace("\\", "\\\\")))
#
# if os.path.exists(path + "//details.csv"):
#     print("File exists")
# else:
#     print("No such file")