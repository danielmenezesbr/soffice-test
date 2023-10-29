import uno
import pathlib
from com.sun.star.beans import PropertyValue
import os
 
def create_instance():
    localContext = uno.getComponentContext()
    resolver = localContext.ServiceManager.createInstanceWithContext(
        "com.sun.star.bridge.UnoUrlResolver", localContext )
    ctx = resolver.resolve("uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext" )
    smgr = ctx.ServiceManager
    desktop = smgr.createInstanceWithContext("com.sun.star.frame.Desktop",ctx)
 
    return desktop
 
def make_prop(name, val):
    return PropertyValue(Name=name, Value=val)
 
def file_url(path):
    path = os.path.abspath(path)
    return pathlib.Path(path).as_uri()
 
def export_pdf():
    desktop = create_instance()
 
    loadArgs = [
        make_prop("UpdateDocMode", 1),
        make_prop("Hidden", True)
    ]
 
    url = file_url("sample-docx-file-for-testing.docx")
 
    print(url)
 
    print("Loading...")
 
    doc = desktop.loadComponentFromURL(url, "_blank", 0, loadArgs)
 
    print("Loaded...")
 
    filterProps = [
        make_prop("IsSkipEmptyPages", False),
    ]
    filterProps = uno.Any("[]com.sun.star.beans.PropertyValue", filterProps)
 
    saveArgs = [
        make_prop("FilterName", "writer_pdf_Export"),
        make_prop("FilterData", filterProps),
    ]
 
    pdfName = file_url("sample-docx-file-for-testing.pdf")
 
    print("Saving PDF", pdfName)
 
    doc.storeToURL(pdfName, saveArgs)
 
    doc.dispose()
 
export_pdf()